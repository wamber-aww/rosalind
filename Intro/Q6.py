#1: make a dictionary to count word frequency

def countWordFreqDict(string):    

    wordFreq = {}
    for i in string.split():
        if i not in wordFreq:
            wordFreq[i] = 1 #first time you see a word it has only appeared once
        elif i in wordFreq:
            wordFreq[i] += 1 #next time just add 1
            
    for key, val in wordFreq.items():
        #iterate through the dictionary and print
        print key, val

#---

#2: directly prints out the words and counts

def countWordFreq(string):

    uniqWords = set(string.split()) #remove duplicate words
    for word in uniqWords:
        print word, string.split().count(word)
