# Spellchecker #

Spellchecker built with python that takes in dictionary and corpus via command line arguments.

Recommends 3 correctly spelled words for every mispelled word.

Uses Levenshtein Distance and N-grams to recommend a correctly spelled word.



## Dictionaries ##

commonWordDictionary.txt contains the top 100,000 most common English words.

largeDictionary.txt contains the top 500,000 most common English words.

unixDictionary.txt contains the built in Unix dictionary.

## Coropa ##

mobyDickCorpus.txt contains the book Moby Dick.

givenTestCase.txt contains the test case provided from assignment 1.


## Usage ##

Python script ngramSpellChecker.py takes in a dictionary and corpus via command line.

Example: python3 ngramSpellChecker.py commonWordsDictionary.txt  mobyDickCorpus.txt 
