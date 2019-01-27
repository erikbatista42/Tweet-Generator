import sys
import random

def getRandomWords():
    #read the file
    file = open("20k.txt", "r")

    #turn all words in file into a list
    wordList = file.read().split()

    #get 4 random words from the wordList
    numOfWordsWanted = int(sys.argv[1])
    randWords = random.sample(wordList, numOfWordsWanted)

    #return it into a "sentence"
    return " ".join(randWords)


if __name__ == "__main__":
    sentence = getRandomWords()
    print(sentence)
