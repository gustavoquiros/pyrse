
DEFAULT_MAXDEPTH = 100

def parse(grammar,nonterm,input,verbose=False,maxdepth=DEFAULT_MAXDEPTH):
	sorted_grammar = { nt : sorted(grammar[nt],key=len,reverse=True) for nt in grammar } 
	for x in parse_nonterm(sorted_grammar,[ord(c) for c in input],nonterm,0,0,verbose,maxdepth):
		if x['end'] == len(input):
			yield x
		else:
			print('backtracking',x) if verbose else None

def parse_nonterm(grammar,input,nonterm,ipos=0,depth=0,verbose=False,maxdepth=DEFAULT_MAXDEPTH):
	if depth < maxdepth:
		rules = grammar[nonterm]
		for r in rules:
			for x in parse_rule(r,grammar,input,nonterm,depth,ipos,0,verbose,maxdepth):
				yield x

def parse_rule(rule,grammar,input,nonterm,depth,ipos,rpos=0,verbose=False,maxdepth=DEFAULT_MAXDEPTH):
	if rpos == 0:
		print('trying', depth, nonterm + ' -> ' + str(rule), '@' + str(ipos)) if verbose else None
	if rpos == len(rule):
		print('accepting', depth, nonterm + ' -> ' + str(rule), '@' + str(ipos)) if verbose else None
		yield {'nonterm': nonterm, 'rule': rule, 'start': ipos, 'end': ipos, 'children': []}
	elif type(rule[rpos]) is int:
		if ipos < len(input) and input[ipos] == rule[rpos]:
			for x in parse_rule(rule,grammar,input,nonterm,depth,ipos+1,rpos+1,verbose,maxdepth):
				sym = { 'symbol': chr(input[ipos]) }
				yield {'nonterm': nonterm, 'rule': rule, 'start': ipos, 'end': x['end'], 'children': [sym] + x['children'] }
	elif type(rule[rpos]) is tuple:
		if ipos < len(input) and input[ipos] >= rule[rpos][0] and input[ipos] <= rule[rpos][1]:
			for x in parse_rule(rule,grammar,input,nonterm,depth,ipos+1,rpos+1,verbose,maxdepth):
				sym = { 'symbol': chr(input[ipos]) }
				yield {'nonterm': nonterm, 'rule': rule, 'start': ipos, 'end': x['end'], 'children': [sym] + x['children'] }
	elif type(rule[rpos]) is str:
		for x in parse_nonterm(grammar,input,rule[rpos],ipos,depth+1,verbose,maxdepth):
			for y in parse_rule(rule,grammar,input,nonterm,depth,x['end'],rpos+1,verbose,maxdepth):
				yield {'nonterm': nonterm, 'rule': rule, 'start': ipos, 'end': y['end'], 'children': [x] + y['children'] }
