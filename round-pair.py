from itertools import combinations

def permutateAllPairs(a, i): 
	for j in range(0, len(a), 2):
		a[(j + i) % len(a)], a[(j + i + 1) % len(a)] = a[(j + i + 1) % len(a)], a[(j + i) % len(a)]
	return a

def permutateSkip(a, i):
    i %= 3
    if (i == 2):
        for i in range(0, len(a), 3):
            a[i % len(a)], a[(i + 1) % len(a)] = a[(i + 1) % len(a)], a[i % len(a)]
    else:
        for i in range(i, len(a), 3):
            a[(i - 1) % len(a)], a[(i - 2) % len(a)] = a[(i - 2) % len(a)], a[(i - 1) % len(a)]
    return a


def rTalkPairs(a):
	return [tuple(sorted(a[i:i+2])) for i in range(0, len(a), 2)]

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
print(needToTalk)
i = 1
while needToTalk:
    i = 1 - i
    currentPlacement = permutatePairs(currentPlacement, i)
    input()
    print(rTalkPairs(currentPlacement))
    print(currentPlacement)
    needToTalk = [x for x in needToTalk if x not in rTalkPairs(currentPlacement)]
print(needToTalk)
