import math
import numpy as np
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

def countIndex (rawTerm):
    Index  = []
    for i in range(1, 4):
        tempIndex = []
        for j in range(len(rawTerm[0])):
            temp = i*10
            tempIndex.append(np.sum(np.array(rawTerm)[temp-10:temp,j]))
        Index.append(tempIndex)
    return Index

def totIndex (index):
    count = 0
    for idx in index:
        count += 1
    return count

def conditionalProb (index, x, y):
    TotalTerm(x, y)
    conProbIndex = []

    for a, idx in enumerate(index):
        tempConProb = []
        for count, b in enumerate(idx):
            tempConProb.append((b + 1)/(categoryTerm[a]+1339))
        conProbIndex.append(tempConProb)
    return conProbIndex

def getSameIndex (a1, a2):
    sameIndex = []

    for a in a1:
        for count, b in enumerate(a2):
            if (a==b):
                sameIndex.append(count)
    return sameIndex

def classification(sameIndex, conProbability):
    clasA = 0
    clasB = 0
    clasC = 0
    klasifikasi = []
    for a in sameIndex:
        for b in range(len(conProbability[0])):
            if(a == b):
                clasA = clasA * np.array(conProbability)[0:a]
                clasB = clasB * np.array(conProbability)[1:a]
                clasC = clasC * np.array(conProbability)[2:a]
    klasifikasi.append(clasA/3)
    klasifikasi.append(clasB/3)
    klasifikasi.append(clasC/3)
    print(len(klasifikasi))