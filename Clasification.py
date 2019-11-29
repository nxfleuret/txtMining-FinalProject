import math
import Weighting as weight

categoryTerm = []

def TermSum (terms, index):
    totalTerm =[]

    for term in terms:
        total = 0
        for idx in index:
            total = total + term.count(idx)
        totalTerm.append(total)
    return totalTerm

def TotalTerm (terms, index):
    totTerm = TermSum(terms, index)
    catA = 0
    catB = 0
    catC = 0
    for idx, val in enumerate(totTerm):
        if(idx < 10):
            catA = catA + val
        if(idx > 9 and idx < 20):
            catB = catB + val
        if(idx > 19 and idx < 30):
            catC = catC + val
    categoryTerm.append(catA)
    categoryTerm.append(catB)
    categoryTerm.append(catC)
    return 0

#masih salah
def countIndex (param):
    totalIndex = []
    temp = []

    for a in param:
        total = 0
        for i, b in enumerate (a):
            for x in range(1338):
                if(i==x):
                    total += b
                    temp.append(total)
    totalIndex.append(temp)
    return totalIndex

def totIndex (index):
    count = 0
    for idx in index:
        count += 1
    return count