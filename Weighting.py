import math

# method untuk mendapatkan hasil terms yang unik
def getIndex(terms):
    index = []
    for term in terms:
        for word in term:
            if word not in index:
                index.append(word)
    return index

# method untuk mendapatkan nilai raw term frequency
def getRawTerm (terms, index):
    rawTerm =[]

    for term in terms:
        docWeight = []
        for idx in index:
            docWeight.append(term.count(idx))
        rawTerm.append(docWeight)
    return rawTerm

# method untuk mendapatkan nilai log term frequency dari nilai raw term frequency yang didapat sebelumnya
def getLogTerm (terms, index):
    logTerm =[]
    for term in terms:
        docWeight = []
        for idx in index:
            if(term.count(idx) > 0):
                docWeight.append(1 + math.log10(term.count(idx)))
            else:
                docWeight.append(0)      
        logTerm.append(docWeight)
    return logTerm

# method untuk memperoleh nilai document frequency
def getDocFrequency(terms, index):
    docFreq = []
    for idx in index:
        dfWeight = 0
        for term in terms:
            if (idx in term):
                dfWeight += 1
        docFreq.append(dfWeight)
    return docFreq

#method untuk mempoeroleh nilai inverse dari nilai document frequency yang didapat sebelumnya
def getInverseDocFrequency(nDocs, df):
    invDocFreq = []
    for item in df:
        invDocFreq.append(math.log10(nDocs)/item)
    return invDocFreq

#method untuk menghitung nilai TF-IDF yang didapat dari hasil perkalian nilai log term frequency dan nilai inverse document frequency
def getTFIDF(logtf, idf):
    tfIdf = []
    for tf in logtf:
        row =  []
        for i in range(0, len(idf)):
            row.append(tf[i] * idf[i])    
        tfIdf.append(row)
    return tfIdf