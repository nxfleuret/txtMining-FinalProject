import math
import Weighting as weight

categoryTerm = []

def totalTerm (terms, index):
    totalTerm =[]

    for term in terms:
        total = 0
        for idx in index:
            total = total + term.count(idx)
        totalTerm.append(total)
    return totalTerm

def countTotal (terms, index):
    totTerm = totalTerm(terms, index)
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

def totIndex (index):
    count = 0
    for idx in index:
        count += 1
    return count