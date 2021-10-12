import os
import re

file_path = input("Enter the path of your file: ")
assert os.path.exists(file_path), "I did not find the file at, "+str(file_path)

# Getting all words from text file.
sentenceList = []
with open(file_path,"r", encoding='cp437') as file:   
    for row in file:                                     
        sentence = re.split(r"\. |\?|\!",row) 
        sentenceList.extend(sentence)

slangList = ['fool', 'donkey', 'dumb', 'filthy']
slangsInEachSentence = []
for sentence in sentenceList:
    slang = 0 
    for word in sentence.split(" "):
        if word in slangList:     # we can search in set of all slangs or use inbuilt library(better_profanity) to identify slang word
            slang += 1
    slangsInEachSentence.append(slang)

print(slangsInEachSentence)



