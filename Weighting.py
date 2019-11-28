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
def rawTerm (terms, index):
    rawWeight =[]

    for term in terms:
        docWeight = []
        for idx in index:
            docWeight.append(term.count(idx))
        rawWeight.append(docWeight)
    return rawWeight

# method untuk mendapatkan nilai log term frequency dari nilai raw term frequency yang didapat sebelumnya
def logTerm (terms, index):
    logWeight =[]
    for term in terms:
        docWeight = []
        for idx in index:
            if(term.count(idx) > 0):
                docWeight.append(1 + math.log10(term.count(idx)))
            else:
                docWeight.append(0)      
        logWeight.append(docWeight)
    return logWeight

# method untuk memperoleh nilai document frequency
def docsFrequency(terms, index):
    df = []
    for idx in index:
        dfWeight = 0
        for term in terms:
            if (idx in term):
                dfWeight += 1
        df.append(dfWeight)
    return df

#method untuk mempoeroleh nilai inverse dari nilai document frequency yang didapat sebelumnya
def inverseDocsFrequency(nDocs, df):
    invFreq = []
    for item in df:
        invFreq.append(math.log10(nDocs)/item)
    return invFreq

#method untuk menghitung nilai TF-IDF yang didapat dari hasil perkalian nilai log term frequency dan nilai inverse document frequency
def tfIdf(tfs, idf):
    tfIdf = []
    for tf in tfs:
        row =  []
        for i in range(0, len(idf)):
            row.append(tf[i] * idf[i])    
        tfIdf.append(row)
    return tfIdf


