
import functools
import operator

DEFAULT_MAXDEPTH = 100

def empty_nonterms(grammar):
	ents = { nt: False for nt in grammar }
	again = True
	while again:
		again = False
		for nt in grammar:
			for r in grammar[nt]:
				if functools.reduce(operator.and_,[(t in ents and ents[t]) for t in r],True):
					again = (ents[nt] != True)
					ents[nt] = True
	return ents

def first_symbols(grammar,ents):
	firsts = { nt: [] for nt in grammar }
	again = True
	while again:
		again = False
		for nt in grammar:
			for r in grammar[nt]:
				i = 0
				while i < len(r): # and type(r[i]) is str:
					if r[i] not in firsts[nt]:
						firsts[nt].append(r[i])
						again = True
					for f in firsts[r[i]]:
						if f not in firsts[nt]:
							firsts[nt].append(f)
							again = True
					if r[i] in ents and ents[r[i]]:
						i = i + 1
					else:
						break
	return firsts

def is_left_rec(nonterm,rule,ents,firsts):
	i = 0
	while i < len(rule) and type(rule[i]) is str:
		if nonterm in firsts[rule[i]]:
			return True
		if rule[i] in ents:
			i = i + 1
		else:
			return False

LEFTREC = []

def sort_rules(grammar,nonterm,rules,ents,firsts):
	nonleftrec = filter(lambda r: not is_left_rec(nonterm,r,ents,firsts),rules)
	leftrec = filter(lambda r: is_left_rec(nonterm,r,ents,firsts),rules)
	global LEFTREC
	LEFTREC = leftrec
	return sorted(nonleftrec,key=len,reverse=True) + sorted(leftrec,key=len,reverse=True)

ENTS = None
FIRSTS = None

def parse(grammar,nonterm,input,verbose=False,maxdepth=DEFAULT_MAXDEPTH):
	global ENTS, FIRSTS
	ents = empty_nonterms(grammar)
	ENTS = ents
	firsts = first_symbols(grammar,ents)
	FIRSTS = firsts
	sorted_grammar = { nt : sort_rules(grammar,nt,grammar[nt],ents,firsts) for nt in grammar } 
	for x in parse_nonterm(sorted_grammar,[ord(c) for c in input],nonterm,0,0,verbose,maxdepth):
		if x['end'] == len(input):
			yield x
		else:
			print('backtracking',x) if verbose else None

def parse_nonterm(grammar,input,nonterm,ipos=0,depth=0,verbose=False,maxdepth=DEFAULT_MAXDEPTH):
	print('nonterm',nonterm,depth)
	if depth < maxdepth:
		rules = grammar[nonterm]
		for r in rules:
			for x in parse_rule(r,grammar,input,nonterm,depth,ipos,0,verbose,maxdepth):
				yield x
	else:
		print('max depth reached',depth,nonterm)

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
