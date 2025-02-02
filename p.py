
def parse_ws_char(i,p=0,d=0):
	if d < 100:
		for x in parse_ws_char_rule0(i,p,d+1):
			yield x
		for x in parse_ws_char_rule1(i,p,d+1):
			yield x
		for x in parse_ws_char_rule2(i,p,d+1):
			yield x
		for x in parse_ws_char_rule3(i,p,d+1):
			yield x

def parse_ws_char_rule0(i,p,d):
	if p < len(i) and i[p] == 32:
		x0 = i[p]
		yield ('ws_char','rule0',p,p+1,[x0])

def parse_ws_char_rule1(i,p,d):
	if p < len(i) and i[p] == 9:
		x0 = i[p]
		yield ('ws_char','rule1',p,p+1,[x0])

def parse_ws_char_rule2(i,p,d):
	if p < len(i) and i[p] == 13:
		x0 = i[p]
		yield ('ws_char','rule2',p,p+1,[x0])

def parse_ws_char_rule3(i,p,d):
	if p < len(i) and i[p] == 10:
		x0 = i[p]
		yield ('ws_char','rule3',p,p+1,[x0])

def parse_ws(i,p=0,d=0):
	if d < 100:
		for x in parse_ws_rule0(i,p,d+1):
			yield x
		for x in parse_ws_rule1(i,p,d+1):
			yield x

def parse_ws_rule0(i,p,d):
	for x0 in parse_ws_char(i,p,d+1):
		for x1 in parse_ws(i,x0[3],d+1):
			yield ('ws','rule0',p,x1[3],[x0,x1])

def parse_ws_rule1(i,p,d):
	yield ('ws','rule1',p,p,[])

def parse_digit(i,p=0,d=0):
	if d < 100:
		for x in parse_digit_rule0(i,p,d+1):
			yield x

def parse_digit_rule0(i,p,d):
	if p < len(i) and i[p] in range(48,57+1):
		x0 = i[p]
		yield ('digit','rule0',p,p+1,[x0])

def parse_num(i,p=0,d=0):
	if d < 100:
		for x in parse_num_rule0(i,p,d+1):
			yield x
		for x in parse_num_rule1(i,p,d+1):
			yield x

def parse_num_rule0(i,p,d):
	for x0 in parse_digit(i,p,d+1):
		yield ('num','rule0',p,x0[3],[x0])

def parse_num_rule1(i,p,d):
	for x0 in parse_digit(i,p,d+1):
		for x1 in parse_num(i,x0[3],d+1):
			yield ('num','rule1',p,x1[3],[x0,x1])

def parse_symchar(i,p=0,d=0):
	if d < 100:
		for x in parse_symchar_rule0(i,p,d+1):
			yield x
		for x in parse_symchar_rule1(i,p,d+1):
			yield x
		for x in parse_symchar_rule2(i,p,d+1):
			yield x
		for x in parse_symchar_rule3(i,p,d+1):
			yield x
		for x in parse_symchar_rule4(i,p,d+1):
			yield x
		for x in parse_symchar_rule5(i,p,d+1):
			yield x

def parse_symchar_rule0(i,p,d):
	if p < len(i) and i[p] == 43:
		x0 = i[p]
		yield ('symchar','rule0',p,p+1,[x0])

def parse_symchar_rule1(i,p,d):
	if p < len(i) and i[p] == 42:
		x0 = i[p]
		yield ('symchar','rule1',p,p+1,[x0])

def parse_symchar_rule2(i,p,d):
	if p < len(i) and i[p] == 45:
		x0 = i[p]
		yield ('symchar','rule2',p,p+1,[x0])

def parse_symchar_rule3(i,p,d):
	if p < len(i) and i[p] == 47:
		x0 = i[p]
		yield ('symchar','rule3',p,p+1,[x0])

def parse_symchar_rule4(i,p,d):
	if p < len(i) and i[p] in range(97,122+1):
		x0 = i[p]
		yield ('symchar','rule4',p,p+1,[x0])

def parse_symchar_rule5(i,p,d):
	if p < len(i) and i[p] in range(65,90+1):
		x0 = i[p]
		yield ('symchar','rule5',p,p+1,[x0])

def parse_sym(i,p=0,d=0):
	if d < 100:
		for x in parse_sym_rule0(i,p,d+1):
			yield x
		for x in parse_sym_rule1(i,p,d+1):
			yield x

def parse_sym_rule0(i,p,d):
	for x0 in parse_symchar(i,p,d+1):
		yield ('sym','rule0',p,x0[3],[x0])

def parse_sym_rule1(i,p,d):
	for x0 in parse_sym(i,p,d+1):
		for x1 in parse_symchar(i,x0[3],d+1):
			yield ('sym','rule1',p,x1[3],[x0,x1])

def parse_expr(i,p=0,d=0):
	if d < 100:
		for x in parse_expr_rule0(i,p,d+1):
			yield x
		for x in parse_expr_rule1(i,p,d+1):
			yield x
		for x in parse_expr_rule2(i,p,d+1):
			yield x
		for x in parse_expr_rule3(i,p,d+1):
			yield x
		for x in parse_expr_rule4(i,p,d+1):
			yield x
		for x in parse_expr_rule5(i,p,d+1):
			yield x

def parse_expr_rule0(i,p,d):
	for x0 in parse_ws(i,p,d+1):
		for x1 in parse_num(i,x0[3],d+1):
			for x2 in parse_ws(i,x1[3],d+1):
				yield ('expr','rule0',p,x2[3],[x0,x1,x2])

def parse_expr_rule1(i,p,d):
	for x0 in parse_ws(i,p,d+1):
		for x1 in parse_sym(i,x0[3],d+1):
			for x2 in parse_ws(i,x1[3],d+1):
				yield ('expr','rule1',p,x2[3],[x0,x1,x2])

def parse_expr_rule2(i,p,d):
	for x0 in parse_ws(i,p,d+1):
		if x0[3] < len(i) and i[x0[3]] == 40:
			x1 = i[x0[3]]
			for x2 in parse_ws(i,x0[3]+1,d+1):
				for x3 in parse_expr(i,x2[3],d+1):
					for x4 in parse_ws(i,x3[3],d+1):
						if x4[3] < len(i) and i[x4[3]] == 41:
							x5 = i[x4[3]]
							for x6 in parse_ws(i,x4[3]+1,d+1):
								yield ('expr','rule2',p,x6[3],[x0,x1,x2,x3,x4,x5,x6])

def parse_expr_rule3(i,p,d):
	for x0 in parse_ws(i,p,d+1):
		for x1 in parse_expr(i,x0[3],d+1):
			for x2 in parse_ws(i,x1[3],d+1):
				for x3 in parse_expr(i,x2[3],d+1):
					for x4 in parse_ws(i,x3[3],d+1):
						yield ('expr','rule3',p,x4[3],[x0,x1,x2,x3,x4])

def parse_expr_rule4(i,p,d):
	for x0 in parse_ws(i,p,d+1):
		for x1 in parse_expr(i,x0[3],d+1):
			for x2 in parse_ws(i,x1[3],d+1):
				for x3 in parse_sym(i,x2[3],d+1):
					for x4 in parse_ws(i,x3[3],d+1):
						for x5 in parse_expr(i,x4[3],d+1):
							for x6 in parse_ws(i,x5[3],d+1):
								yield ('expr','rule4',p,x6[3],[x0,x1,x2,x3,x4,x5,x6])

def parse_expr_rule5(i,p,d):
	for x0 in parse_ws(i,p,d+1):
		for x1 in parse_expr(i,x0[3],d+1):
			for x2 in parse_ws(i,x1[3],d+1):
				if x2[3] < len(i) and i[x2[3]] == 44:
					x3 = i[x2[3]]
					for x4 in parse_ws(i,x2[3]+1,d+1):
						for x5 in parse_tail(i,x4[3],d+1):
							for x6 in parse_ws(i,x5[3],d+1):
								yield ('expr','rule5',p,x6[3],[x0,x1,x2,x3,x4,x5,x6])

def parse_tail(i,p=0,d=0):
	if d < 100:
		for x in parse_tail_rule0(i,p,d+1):
			yield x
		for x in parse_tail_rule1(i,p,d+1):
			yield x

def parse_tail_rule0(i,p,d):
	for x0 in parse_ws(i,p,d+1):
		for x1 in parse_expr(i,x0[3],d+1):
			for x2 in parse_ws(i,x1[3],d+1):
				yield ('tail','rule0',p,x2[3],[x0,x1,x2])

def parse_tail_rule1(i,p,d):
	for x0 in parse_ws(i,p,d+1):
		for x1 in parse_expr(i,x0[3],d+1):
			for x2 in parse_ws(i,x1[3],d+1):
				if x2[3] < len(i) and i[x2[3]] == 44:
					x3 = i[x2[3]]
					for x4 in parse_ws(i,x2[3]+1,d+1):
						for x5 in parse_tail(i,x4[3],d+1):
							for x6 in parse_ws(i,x5[3],d+1):
								yield ('tail','rule1',p,x6[3],[x0,x1,x2,x3,x4,x5,x6])

import sys
import json

i = sys.stdin.readline().rstrip('\n').rstrip('\r')
c = [ord(x) for x in list(i)]
for x in parse_expr(c):
	print(json.dumps(x,indent=2))
	sys.stdin.readline()
