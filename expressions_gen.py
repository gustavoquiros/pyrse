
import json
import sys
import pyrsegen

expressions = {
	'ws_char': [[ord(' ')],[ord('\t')],[ord('\r')],[ord('\n')]],
	'ws': [['ws_char','ws'],[]],
	'digit': [[(ord('0'),ord('9'))]],
	'num': [['digit'],['digit','num']],
	'op': [[ord('+')],[ord('*')],[ord('-')],[ord('/')]],
	'expr': [ 
		['ws','num','ws'] ,
		['ws',ord('('),'ws','expr','ws',ord(')'),'ws'],
		['ws','expr','ws','op','ws','expr','ws'] ,
		]
}

pyrsegen.generate_parser(expressions,'expr')
