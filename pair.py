from itertools import combinations, permutations
from checkers import checkGroups, iterCheckGroups

_elementsNum = 12
_defaultElements = tuple(int(i) for i in range(1, _elementsNum + 1))

pairs = list(combinations(_defaultElements, 2))
groups = list(combinations(pairs, _elementsNum // 2))
checkedGroups = []
for group in groups: 
	b = []
	for i in group:
		b += list(i)
	if len(b) == len(set(b)):
		checkedGroups.append(group)
result = []
print(len(list(combinations(checkedGroups, _elementsNum - 1))))
# for plan in combinations(checkedGroups, _elementsNum - 1):
# 	b = []
# 	for i in plan:
# 		b += list(i)
# 	if len(b) == len(set(b)):
# 		result.append(plan)
# 		break
print(plan)