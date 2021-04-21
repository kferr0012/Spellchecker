import sys
import re
from Levenshtein import distance
# from nltk.metrics import edit_distance
from nltk.tokenize import RegexpTokenizer
import time


def main():
    time_start = time.time()
    
    #Load dictionary
    try:
        dictionary = open(sys.argv[1],'r').read()
    except:
        print("Error loading dictionary")
        exit()

    #Load corpus
    try:
        corpus = open(sys.argv[2],'r').read()
    except:
        print("Error loading corpus")
        exit()

    #Convert dictionary into an array of strings
    dictionary=dictionary.split()

    #Remove punctuation from each word in corpus and convert to array of strings 
    tokenizer = RegexpTokenizer(r'\w+')
    corpus=tokenizer.tokenize(corpus)

    #Remove all numbers from every word in the corpus
    pattern='[0-9]'
    corpus = [re.sub(pattern, '', i) for i in corpus]

    #lowercase every word in corpus
    for i in range(len(corpus)):
        corpus[i]=corpus[i].lower() 

    #populate ngram table
    ngramTable = {}
    for word in corpus:
        ngramTable[word] = ngramTable.get(word,0) + 1
    
    #lowercase every word in dictionary
    for i in range(len(dictionary)):
        dictionary[i]=dictionary[i].lower()

    #Get unique values in corpus
    corpusSet=set()
    for word in corpus:
        if word != "":
            corpusSet.add(word)

    #Create set for dictionary to allow set opertions
    dictionarySet=set()
    for word in dictionary:
        dictionarySet.add(word)

    #Use set operations to find all the mispellings
    mispellingsSet = corpusSet.difference(dictionarySet)

    #Find 3 suggestions for each mispellings
    for mispelledWord in mispellingsSet:
        bestSuggestedWords = ["", "", ""]
        bestSuggestedValues = [999,888,777]
        worstVal = max(bestSuggestedValues)

        for potentialWord in dictionarySet:
            levVal = distance(mispelledWord,potentialWord)
            # levVal = edit_distance(mispelledWord,potentialWord,substitution_cost=2)

            if levVal < worstVal:
                #Find index of worst val
                worstValIndex = bestSuggestedValues.index(worstVal)

                #Change word at that index
                bestSuggestedWords[worstValIndex] = potentialWord

                #Update value at that index and update worst val
                bestSuggestedValues[worstValIndex]=levVal
                worstVal=max(bestSuggestedValues)
            
            #Use ngram to decide a tie
            elif levVal == worstVal: 
                #Find index of worst val
                worstValIndex = bestSuggestedValues.index(worstVal)

                potentialWordNgram = ngramTable.get(potentialWord)
                currentPickedWordNgram = ngramTable.get(bestSuggestedWords[worstValIndex])

                if type(potentialWordNgram) is not type(None) and type(currentPickedWordNgram) is not type(None): 
                
                    if potentialWordNgram > ngramTable.get(bestSuggestedWords[worstValIndex]):

                        #Change word at that index
                        bestSuggestedWords[worstValIndex] = potentialWord

                        #Update value at that index and update worst val
                        bestSuggestedValues[worstValIndex]=levVal
                        worstVal=max(bestSuggestedValues)

        print(mispelledWord + ": " + bestSuggestedWords[0] + ", " + bestSuggestedWords[1] + ", " + bestSuggestedWords[2])

    time_end = time.time()
    time_lapsed = time_end-time_start
    print("Time : " + str(time_lapsed) + " seconds")


if __name__=='__main__':
    main()