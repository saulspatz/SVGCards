import os, sys, re, subprocess, argparse

def getArgs():
    parser = argparse.ArgumentParser(description='Extract individual SVG cards')
    parser.add_argument('source', help='source sprite file path')
    parser.add_argument('folder', help='parent directory for svg folder')
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
    source = os.path.abspath(args.source)
    if not os.path.exists(source):
        print('File not found: %s'%source)
        exit()
    target = os.path.abspath(args.folder) 
    if not os.path.exists(target):
        print('File not found: %s'%target)
        exit()    
    try:       
        target = os.path.join(target,'svgs')
        os.mkdir(target)
    except OSError:
        # python 2 raises OSError
        # python 3 raises FileExistsError, a subclass of OSError
        pass    
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
    for card in cards:
        svg= os.path.join(target,card+'.svg')
        cmd = [inkscape, source, '--without-gui',
                    '--export-id=%s'%card,
                    '--export-plain-svg=%s'%svg,
                    '--export-id-only']              
        print('Extracting %s.svg'%card)
        subprocess.call(cmd, universal_newlines=True) 
          
if __name__ == '__main__':
    main()
    