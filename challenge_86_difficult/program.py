import sys

encoded_2_sat = [(1,-3),(2,3),(1,-2)]

def solve(inst, context):
	inst_list = list(inst)
	
	if len(inst_list) == 0: return True
	
	clause = inst_list[0]
	inst_list.remove(clause)
	
	if clause[0] in context and clause[1] in context:
		if context.get(clause[0]) is False and context.get(clause[1]) is False: return False
		return solve(inst_list, context)
	elif context.get(clause[0]) is True or context.get(clause[1]) is True:
		return solve(inst_list, context)
	for var in filter(lambda x: x not in context, clause):
		context[var] = True
		context[var * -1] = False
		if solve(inst_list, context) is True: return True
	return False

print solve(encoded_2_sat, {})