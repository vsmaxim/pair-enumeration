from itertools import combinations, permutations
from math import log

def talk(first, second):
    return [(first[i], second[i]) for i in range(len(first))]

def permutate(a):
    a.append(a.pop(0))
    return a

def halfTalk(a):
    left = generateHalfs(a)[0]
    right = generateHalfs(a)[1]
    res = []
    for i in range(len(left)):
            right = permutate(right)
            res.append(talk(left, right))
    return res

def generateHalfs(a):
    middle = len(a) // 2
    return a[:middle], a[middle:]

def talkPlan(a):
    deg = int(log(len(a), 2))
    fullres = []
    for i in range(deg):
        if (i == 0):
            res = generateHalfs(a)
        else:
            res = [generateHalfs(i) for i in res]
            nres = []
            for i in res:
                nres += i
            res = nres
        for i in range(0, len(res), 2):
            fullres += halfTalk(res[i] + res[i + 1])
    resultingPlan = []
    i = 0
    while (i != len(fullres)): 
        tempPlan = []
        if (len(fullres[i]) == len(a) // 2):
            resultingPlan.append(fullres[i])
            i += 1
        else:
            while (len(tempPlan) != len(a) // 2):
                tempPlan += fullres[i]
                i += 1
            resultingPlan.append(tempPlan)
    return resultingPlan

def matrixPrint(plan, num):
    a = [[0 for i in range(num)] for i in range(num)]
    for i in range(len(plan)):
        for j in plan[i]:
            a[j[0] - 1][j[1] - 1], a[j[1] - 1][j[0] - 1] = i + 1, i + 1
    for i in a:
        print(' '.join([str(f) for f in i]))

_elementsNum = int(input('Введите количество человек: ')) 
_defaultElements = tuple(int(i) for i in range(1, _elementsNum + 1))

if (_elementsNum == 2 ** (int(log(_elementsNum, 2)))):
    plan = talkPlan([i + 1 for i in range(_elementsNum)])
else:
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
    for plan in combinations(checkedGroups, _elementsNum - 1):
        b = []
        for i in plan:
            b += list(i)
        if len(b) == len(set(b)):
            result.append(plan)
            break
print("План бесед:")
matrixPrint(plan, _elementsNum)
