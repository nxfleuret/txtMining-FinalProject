import math
import numpy as np
import Weighting as weight

categoryTerm = []

#method untuk mencari jumlah term dari masing-masing dokumen
def TermSum (terms, index):
    totalTerm =[]

    for term in terms:
        total = 0
        for idx in index:
            total = total + term.count(idx)
        totalTerm.append(total)
    return totalTerm

#method untuk mencari jumlah term keseluruhan masing-masing kategori
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

#method untuk menghitung nilai penjumlahan masing-masing index menurut kategorinya
def countIndex (rawTerm):
    Index  = []

    global totIndex
    totIndex = len(rawTerm[0])

    for i in range(1, 4):
        tempIndex = []
        for j in range(totIndex):
            temp = i*10
            tempIndex.append(np.sum(np.array(rawTerm)[temp-10:temp,j]))
        Index.append(tempIndex)
    return Index

#method untuk mencari nilai Conditional Probability dari masing-masing index
def conditionalProb (totalIndex, x, y):
    TotalTerm(x, y)
    conProbIndex = []

    for category, countIndexInAnyCategory in enumerate(totalIndex):
        tempConProb = []
        for index, value in enumerate(countIndexInAnyCategory):
            tempConProb.append((value + 1)/(categoryTerm[category]+totIndex))
        conProbIndex.append(tempConProb)
    return conProbIndex

#method untuk mencari index yang sama dari data sebelumnya dengan index pada data uji
def getSameIndex (a1, a2):
    sameIndex = []

    for a in a1:
        for count, b in enumerate(a2):
            if (a==b):
                sameIndex.append(count)
    return sameIndex

#method untuk menghitung klasifikasi dari data uji, data tersebut akan diolah untuk mendapatkan klasifikasinya dengan metode naive bayes
def classification(sameIndex, conProbability):
    klasifikasi = []

    for count, a in enumerate(conProbability):
        for idx in sameIndex:
            temp = 1
            for counter, b in enumerate(a):
                if(idx == counter):
                    temp = temp * b
        klasifikasi.append(temp/3)
    
    if (klasifikasi[0] > klasifikasi[1] and klasifikasi[0] > klasifikasi[2]):
        klasifikasi.append("agriculture")
    elif (klasifikasi[1] > klasifikasi[0] and klasifikasi[1] > klasifikasi[2]):
        klasifikasi.append("education")
    elif (klasifikasi[2] > klasifikasi[0] and klasifikasi[2] > klasifikasi[1]):
        klasifikasi.append("engineering")

    print(klasifikasi[3])

    return klasifikasi