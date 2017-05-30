def checkGroups(groupList):
	''' Returns list of groups w/o repeats'''
	nList = list()
	for group in groupList:
		b = []
		for i in group:
			b += list(i)
		if len(b) == len(set(b)):
				nList.append(group)
	return nList


def iterCheckGroups(itergroups):
	''' Returns one group w/o repeats'''
	for i in itergroups:
		b = []
		for j in i:
			b += list(i)
		print(b)
		if (len(b)) == len(set(b)):
			return b