import os, sys, subprocess, argparse

def getArgs():
    parser = argparse.ArgumentParser(description='Export SVG cards to PNG files')
    parser.add_argument('source', help='source sprite file path')
    parser.add_argument('folder', help='parent directory for png folder')
    parser.add_argument('-s', '--sprite', action='store_true', help='create sprite sheet also')
    parser.add_argument('-o', '--sprite_only', action='store_true', help='create sprite sheet only')
    parser.add_argument('-w', '--width', type = int, default=75, help='image width (default 75 pixels)')
    parser.add_argument('-i', '--inkscape', default = '', help = 'path to inkscape')
    return parser.parse_args(sys.argv[1:])
    
def getInkscape():
    # If inkscape is somewhere else on your system, change the return
    # value for your platform to the path to the inkscape executable.
    # Alternatively, put inkscape in your path, and change this function to:
    # return 'inkscape'
    
    if sys.platform == 'darwin':          # Mac
        return '/Applications/Inkscape.app/Contents/Resources/bin/inkscape'
    if sys.platform == 'win32':            # Windows
        return 'C:\Progra~1\Inkscape\inkscape.com'
    return 'inkscape'                            # other
    
def main():
    args = getArgs()    
    print(os.getcwd())
    source = os.path.abspath(args.source)
    if not os.path.exists(source):
        print('File not found: %s'%source)
        exit()
    target = os.path.abspath(args.folder) 
    if not os.path.exists(target):
        print('File not found: %s'%target)
        exit()    
    try:       
        target = os.path.join(target,'pngs')
        os.mkdir(target)
    except OSError:
        # python 2 raises OSError
        # python 3 raises FileExistsError, a subclass of OSError
        pass    
    width = args.width
    if not args.inkscape:
        inkscape = getInkscape()
    else:
        inkscape = args.inkscape    
    print('source', source)
    print('target', target)
    suits = ['spade','heart','diamond','club']
    ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    others =  ['blueBack','redBack','redJoker','blackJoker']
    cards = [s+r for s in suits for r in ranks ] + others   
    if args.sprite_only: 
        cards = []
    try:
        for card in cards:
            png = os.path.join(target,card+'.png')
            cmd = [inkscape, source,
                        '--export-id=%s'%card,
                         '--export-filename=%s'%png,
                        '--export-width=%s'%width]   
            subprocess.call(cmd, universal_newlines=True) 
            #print(cmd)
        if args.sprite or args.sprite_only:
            sprite = os.path.split(source)[-1]
            png = os.path.join(target,os.path.splitext(sprite)[0]+'.png')
            width *= 14
            cmd = [inkscape, source,
                        '--export-filename=%s'%png,
                       '--export-width=%s'%width]
            subprocess.call(cmd, universal_newlines=True) 
            #print(cmd)
    except OSError:
        print('Inkscape program not found.  \nUse --inkscape option or edit the source.')
        
if __name__ == '__main__':
    print(sys.argv[1:])
    main()
    
    