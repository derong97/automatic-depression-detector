from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
   
ps = PorterStemmer() 
   
sentence = "Programers program with programing languages"
words = word_tokenize(sentence) 
   
for w in words: 
    print(w, " : ", ps.stem(w)) 