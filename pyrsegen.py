
import sys

MAX_DEPTH = 100

def generate_parser(g,s,d=MAX_DEPTH):
    for nt in g:
        print('\ndef parse_{}(i,p=0,d=0):'.format(nt))
        print('\tif d < {}:'.format(d))
        i = 0
        for r in g[nt]:
            print('\t\tfor x in parse_{}_rule{}(i,p,d+1):'.format(nt,i))
            print('\t\t\tyield x')
            i = i + 1
        i = 0
        for r in g[nt]:
            print('\ndef parse_{}_rule{}(i,p,d):'.format(nt,i))
            generate_rule(g,nt,r,i,0)
            i = i + 1
    print('\nimport sys')
    print('import json')
    print('\ni = sys.stdin.readline().rstrip(\'\\n\').rstrip(\'\\r\')')
    print('c = [ord(x) for x in list(i)]')
    print('for x in parse_{}(c):'.format(s))
    print('\tprint(json.dumps(x,indent=2))')
    print('\tsys.stdin.readline()')

            
def generate_rule(g,nt,r,ri,i,e='p'):
    if i == len(r):
        c = '[{}]'.format(','.join(['x{}'.format(j) for j in range(i)]))
        print('{}yield (\'{}\',\'rule{}\',p,{},{})'.format('\t'*(i+1),nt,ri,e,c))
    else:
        if type(r[i]) is str:
            print('{}for x{} in parse_{}(i,{},d+1):'.format('\t'*(i+1),i,r[i],e))
            generate_rule(g,nt,r,ri,i+1,'x{}[3]'.format(i))
        elif type(r[i]) is int:
            print('{}if {} < len(i) and i[{}] == {}:'.format('\t'*(i+1),e,e,r[i]))
            print('{}x{} = i[{}]'.format('\t'*(i+2),i,e))
            generate_rule(g,nt,r,ri,i+1,'{}+1'.format(e))
        elif type(r[i]) is tuple:
            print('{}if {} < len(i) and i[{}] in range({},{}+1):'.format('\t'*(i+1),e,e,r[i][0],r[i][1]))
            print('{}x{} = i[{}]'.format('\t'*(i+2),i,e))
            generate_rule(g,nt,r,ri,i+1,'{}+1'.format(e))
