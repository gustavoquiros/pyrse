
import json
import sys
import pyrse_continuations as pyrse

expressions = {
	'ws-char': [[ord(' ')],[ord('\t')],[ord('\r')],[ord('\n')]],
	'ws': [['ws-char','ws'],[]],
	'digit': [[(ord('0'),ord('9'))]],
	'num': [['digit'],['num','digit']],
	'op': [[ord('+')],[ord('*')],[ord('-')],[ord('/')]],
	'expr': [ 
		['num'] ,
		['expr-ws','op','expr-ws'] ,
		[ord('('),'expr-ws',ord(')')],
		],
	'expr-ws': [['ws','expr','ws']]
}

# print('grammar',expressions)

input = sys.stdin.readline().rstrip('\n').rstrip('\r')

for x in pyrse.parse(expressions,'expr-ws',input,False):
	print(json.dumps(x,indent=2))
	#print(x)
	sys.stdin.readline()
