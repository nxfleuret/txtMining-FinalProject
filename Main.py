import os
import PreProcessing as pre
import Weighting as weight
import Clasification as clasf

directory = os.fsencode("input")

terms = []

# menuliskan hasil preprocessing ke dalam .txt
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     str_input = open("input/"+filename, errors = 'ignore').read()
     filteredWords = pre.lemmatize_sentence(str_input).split(' ')
     terms.append(filteredWords)
     text_file = open("output/hasil-"+filename, "w+")
     for line in filteredWords:
         text_file.write(line + "\n")
     text_file.close()

index = weight.getIndex(terms)
rawTerm = weight.getRawTerm(terms, index)
logTerm = weight.getLogTerm(terms, index)
df = weight.getDocFrequency(terms, index)
idf = weight.getInverseDocFrequency(len(terms), df)
tf_idf = weight.getTFIDF(logTerm, idf)
totalTerm = clasf.TermSum(terms, index)
totalTermdocs = clasf.TotalTerm(terms, index)
totalIndex = clasf.countIndex(rawTerm)

#menuliskan hasil perhitungan raw Term kedalam .txt
filebaru = open("output/hasil rawTerm.txt", "w+")
for i in rawTerm:
    for x in i:
        filebaru.write(str(x) + " ")
    filebaru.write("\n")
filebaru.close()

#menuliskan hasil perhitungan TF-IDF kedalam .txt
filebaru = open("output/hasil TFIDF.txt", "w+")
for i in tf_idf:
    for x in i:
        filebaru.write(str(x) + " ")
    filebaru.write("\n")
filebaru.close()

#menuliskan hasil peengolahan term yang unik
filenew = open("output/Index.txt", "w+")
for i in index:
    filenew.write(str(i) + "\n")
filenew.close()

#menuliskan hasil penjumlahan total dari rawTerm tiap dokumen
filenew = open("output/hasil totalTerm.txt", "w+")
for i in totalTerm:
    filenew.write(str(i) + "\n")
filenew.close()

# #menuliskan hasil penjumlahan total dari rawTerm tiap dokumen pada masing-masing kategori
# filenew = open("output/totalTerm per Doc.txt", "w+")
# for i in totalTermdocs:
#     filenew.write(str(i) + "\n")
# filenew.close()

filenew = open("output/test.txt", "w+")
for i in totalIndex:
    filenew.write(str(i) + "\n")
filenew.close()

print(clasf.categoryTerm[0])
print(clasf.categoryTerm[1])
print(clasf.categoryTerm[2])