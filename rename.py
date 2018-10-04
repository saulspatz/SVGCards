import argparse
import sys
import os
'''
Rename all card files in a directory

For example, diamondKing.png will be renamed KD.png
'''

suits = { }
for suit in {'spade', 'heart', 'diamond', 'club'}:
    suits[suit] = suit[0].upper()
ranks = { }
for rank in {'Ace','King', 'Queen', 'Jack'}:
    ranks[rank] = rank[0]
ranks['10']='T'
for rank in '23456789':
    ranks[rank]=rank
    
def rename(src, dest):
    contents = os.listdir(src)
    for rank in ranks:
        for suit in suits:
            prefix = suit+rank
            p = len(prefix)
            alias = ranks[rank]+suits[suit]
            for f in [f for f in contents if f.startswith(prefix)]:
                os.rename(os.path.join(src,f), os.path.join(dest,alias+f[p:]))
                
def getArgs():
    parser = argparse.ArgumentParser(description=
                    'Rename card files')
    parser.add_argument('source', help='source directory')
    parser.add_argument('target', help='target directory')
    args = vars(parser.parse_args(sys.argv[1:]))
    return args['source'], args['target']

if __name__=='__main__':
    src, dest = getArgs()
    rename(src, dest)
    