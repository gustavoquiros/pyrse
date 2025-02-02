
import json
import sys
import pyrsegen

isla = {
    'ws_char': [[ord(' ')],[ord('\t')],[ord('\r')],[ord('\n')]],
    'ws': [['ws_char','ws'],[]],
    'digit': [[(ord('0'),ord('9'))]],
    'num': [['digit'],['digit','num']],
    'symchar': [[ord('+')],[ord('*')],[ord('-')],[ord('/')],[(ord('a'),ord('z'))],[(ord('A'),ord('Z'))]],
    'sym': [['symchar'],['sym','symchar']],
    'expr': [ 
	['ws','num','ws'] ,
        ['ws','sym','ws'] ,
	['ws',ord('('),'ws','expr','ws',ord(')'),'ws'],
        ['ws','expr','ws','expr','ws'] ,
	['ws','expr','ws','sym','ws','expr','ws'],
        ['ws','expr','ws',ord(','),'ws','tail','ws'],
    ],
    'tail': [
        ['ws','expr','ws'],
        ['ws','expr','ws',ord(','),'ws','tail','ws'],
    ] 
}

pyrsegen.generate_parser(isla,'expr')
