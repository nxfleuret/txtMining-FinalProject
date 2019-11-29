import nltk
import os
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


# **** Tokenisasi ****
def tokenisasi(str_input):
    removeList = [line.rstrip('\n') for line in open("remove.txt")]
    result = ""

    # caseFoldingg
    # melakukan konversi kalimat menjadi huruf kecil
    str_input = str_input.lower()

    # menghapus karakter yang tidak perlukan.
    # setiap karakter yang terdapat di dalam removeList akan dihilangkan/diganti menjadi ''
    for letter in str_input.strip():
        if letter not in removeList:
            result += letter

    # melakukan tokenisasi
    str_input = result.split(' ')
    return (str_input)


# **** Filtering ****
# Mmelakukan tokenisasi dan penghilangan kata-kata yang tidak diperlukan yaitu yang terdapat pada stopwords list
def filter_string(string):
    stringToken = tokenisasi(string)
    
    stopList = [line.rstrip('\n') for line in open("stoplist.txt")]

    filteredString = [word for word in stringToken if word not in stopList]

    # menghapus array yang mengandung item string ['']
    # untuk menghindari terjadinya error "string index out of range" saat melakukan POS tagging nanti di method lemmatize_sentence
    filteredString = [word for word in filteredString if word]

    # keluaran dari filteredString berupa array
    # misal dari "string = 'hello, world'"
    # akan menjadi ['hello', 'world']
    return filteredString


# fungsi untuk melakukan konversi nltk tag menjadi wordnet tag
# dikarenakan nltk lemmatizer.lemmatize() cuma memiliki tag, yaitu
# {"J": wordnet.ADJ,
#  "N": wordnet.NOUN,
#  "V": wordnet.VERB,
#  "R": wordnet.ADV}
def nltk_to_wordnet_tag(tag_nltk):
    if tag_nltk.startswith('J'):
        return wordnet.ADJ
    elif tag_nltk.startswith('V'):
        return wordnet.VERB
    elif tag_nltk.startswith('N'):
        return wordnet.NOUN
    elif tag_nltk.startswith('R'):
        return wordnet.ADV
    else:          
        return None

# Untuk bagian stemming, di sini kami lebih menggunakan lemmitization, karena lemmitization
# lebih melakukan konversi ke root word dari inflection word bergantung pada konteksnya.
# Dan juga digunakan untuk menghindari kondisi over stemming. Yaitu seperti kata caring menjadi car.
# Namun penggunaan lemmatizing lebih lama dibanding stemming, karena perlu adanya analisa dulu dari lemmatizing.
def lemmatize_sentence(sentence):

    # Berikut penjelasan untuk variabel : nltk_tagged
    # Yaitu melakukan tokenisasi terhadap kalimat dengan method filter_string di atas
    # Dan melakukan penentuan POS tag untuk setiap words token (array)
    # nltk.pos_tag() digunakan untuk melakukan penandaan setiap komponen dalam kalimat
    # apakah termasuk pada komponen, yaitu :
    # [CC => coordinating conjunction] [CD => cardinal digit] 
    # [DT => determiner] [NN => noun, singular ‘desk’] [NNS => noun plural ‘desks’] etc...
    # kenapa diperlukan word tag, karena untuk hasil lebih optimal pada nltk.lemitize itu diperlukan nilai pos tag untuk membedakan apakah kata dalam suatu kalimat termasuk noun, verb, dll..
    # input=['Everything is all about money.']
    # nltk.pos_tag(input)
    # Output: [('Everything', 'NN'), ('is', 'VBZ'), 
    #      ('all', 'DT'),('about', 'IN'), 
    #      ('money', 'NN'), ('.', '.')] 

    nltk_tagged = nltk.pos_tag(filter_string(sentence)) 

    # tuple of (token, wordnet_tag)
    # wordnet_tagged berupa map
    wordnet_tagged = map(lambda it: (it[0], nltk_to_wordnet_tag(it[1])), nltk_tagged)
    lemmatized_sentence = []


    for word, tag in wordnet_tagged:
        if tag is None:
            lemmatized_sentence.append(word)
        else:
            # else menggunakan tag untuk me-lemmatisasi token
            # penggunaan tag pada nltk lemmatize terdapat di sini.
            # lebih optimal menggunakan lemmatize(word, tag) dibanding dengan lemmatize(word)
            # karena sudah diketahui suatu kata dalam kalimat termasuk komponen verb misalnya
            # maka akan lebih mudah pengubahannya, misal caring akan menjadi care.
            # kalau misal tanpa tag, maka data mining bisa menjadi data mine.
            # tapi dengan lemmatize("data mining", "n") akan tetap menjadi data mining.
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))

    return " ".join(lemmatized_sentence)

lemmatizer = WordNetLemmatizer()