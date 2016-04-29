import argparse, sys, re, os

def hexColor(rgb):
    if len(rgb) != 6:
        msg = '%s should be 6 characters long' % rgb
        raise argparse.ArgumentTypeError(msg)
    try:
        _ = int(rgb, 16)
        return rgb
    except ValueError:
        msg = '%s is not a valid hex string' % rgb
        raise argparse.ArgumentTypeError(msg)
    
def getArgs():
    parser = argparse.ArgumentParser(description='Change cards colors', argument_default=argparse.SUPPRESS)
    parser.add_argument('oldFile', help='source sprite file path')
    parser.add_argument('newFile', help='target sprite file path')
    parser.add_argument('-C','--clubs',dest='club',
                        help = 'New club color', type = hexColor, action = 'append')
    parser.add_argument('-D','--diamonds',dest='diamond',
                        help='New diamond color', type = hexColor, action = 'append')
    parser.add_argument('-H','--hearts',dest='heart',
                        help='New heart color', type = hexColor, action = 'append')
    parser.add_argument('-S','--spades',dest='spade',
                        help='New spade color', type = hexColor, action = 'append')
    parser.add_argument('-B','--background',dest='background',
                        help = 'New card background color', type = hexColor, action = 'append')
    
    args = vars(parser.parse_args(sys.argv[1:]))
    if len(args) == 2:
        print("You must change at least one color.")
        exit()
    for key in {'club', 'diamond', 'heart', 'spade', 'background'}:
        if key in args:
            if len(args[key]) > 1:
                print("Multiple new colors specified for %ss"%key)
                exit()
            else:
                args[key] = args[key][0]
    return args

def getRGB(suit,text):
    fillPattern = r':#(.*?);'
    if suit != 'background':
        colorPattern = r'<path[^<]*?%sPip.*?>'%suit
    else:
        colorPattern = r'<rect[^<]*?cardBackground.*?>'
    subText=re.search(colorPattern, text, re.DOTALL).group(0)
    color = re.search(fillPattern, subText, re.DOTALL).groups()[0]
    return color

def main():
    args = getArgs()
    try:
        fin = open(args['oldFile'])
    except OSError:
        print('Cannot read file: %s'%args['oldFile'])
        exit()
    try:
        fout = open(args['newFile'],'w')
    except OSError:
        print('Cannot create file: %s for writing'%args['newFile'])
        exit()

    with fin, fout:
        text = fin.read()
        for color in args:
            if 'File' in color:continue
            oldColor = getRGB(color, text)
            newColor = args[color]
            print(color, oldColor, newColor)
            text = re.sub(oldColor, newColor, text)
        fout.write(text)
                    
if __name__ == '__main__':
    main()
    







