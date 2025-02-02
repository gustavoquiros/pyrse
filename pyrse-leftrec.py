
def parse(grammar,nonterm,input,verbose=False):
	for x in parse_nonterm(grammar,[ord(c) for c in input],nonterm,0,[],verbose):
		if x['end'] == len(input):
			yield x
		else:
			print('backtracking',x) if verbose else None

def parse_nonterm(grammar,input,nonterm,ipos=0,leftstack=[],verbose=False):
	rules = grammar[nonterm]
	rules = sorted(rules,key=len,reverse=True)
	for r in rules:
		for x in parse_rule(r,grammar,input,nonterm,leftstack,ipos,0,verbose):
			yield x

def parse_rule(rule,grammar,input,nonterm,leftstack,ipos,rpos=0,verbose=False):
	if rpos == 0:
		print('trying', nonterm + ' -> ' + str(rule), '@' + str(ipos)) if verbose else None
	if rpos == len(rule):
		print('accepting', nonterm + ' -> ' + str(rule), '@' + str(ipos)) if verbose else None
		yield {'nonterm': nonterm, 'rule': rule, 'start': ipos, 'end': ipos, 'children': []}
	elif type(rule[rpos]) is int:
		if ipos < len(input) and input[ipos] == rule[rpos]:
			for x in parse_rule(rule,grammar,input,nonterm,leftstack,ipos+1,rpos+1,verbose):
				sym = { 'symbol': chr(rule[rpos]) }
				yield {'nonterm': nonterm, 'rule': rule, 'start': ipos, 'end': x['end'], 'children': [sym] + x['children'] }
	elif type(rule[rpos]) is str:
		if (rpos == 0) and (rule in leftstack):
			print('skipping', nonterm + ' -> ' + str(rule), '@' + str(ipos)) if verbose else None
		else:
			nls = (leftstack + [rule]) if rpos == 0 else leftstack
			for x in parse_nonterm(grammar,input,rule[rpos],ipos,nls,verbose):
				for y in parse_rule(rule,grammar,input,nonterm,leftstack,x['end'],rpos+1,verbose):
					yield {'nonterm': nonterm, 'rule': rule, 'start': ipos, 'end': y['end'], 'children': [x] + y['children'] }
