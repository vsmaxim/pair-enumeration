from itertools import combinations

def permutatePairs(a, i): 
	for j in range(0, len(a), 2):
		a[(j + i) % len(a)], a[(j + i + 1) % len(a)] = a[(j + i + 1) % len(a)], a[(j + i) % len(a)]
	return a

def rTalkPairs(a):
	return [tuple(sorted(a[i:i+2])) for i in range(len(a))]

def lTalkPairs(a):
	res = []
	for i in range(0, len(a), 2):
		res.append(tuple(sorted([a[i], a[i - 1]])))
	return res
pairNum = 6

currentPlacement = [i for i in range(1 , pairNum + 1)]
needToTalk = list(combinations(currentPlacement, 2))
num = int(input("Input pair permutation: "))
print(permutatePairs(currentPlacement, num))
print(lTalkPairs(currentPlacement))
needToTalk = [x for x in needToTalk if (x not in lTalkPairs(currentPlacement))]
needToTalk = [x for x in needToTalk if x not in rTalkPairs(currentPlacement)]
currentPlacement = permutatePairs(currentPlacement, 0)
needToTalk = [x for x in needToTalk if x not in lTalkPairs(currentPlacement)]
print(needToTalk)