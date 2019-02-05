import sys
import random

def sample():
    #select a random word out of the text file that is typed on the terminal
    file_name = sys.argv[1]
    file = open(file_name, "r")
    word_list = file.read().split()

    rand_index = random.randint(0, len(word_list) -1)

    return word_list[rand_index]

def probabilistic_word_sampler(myWords, numRandomSelections):
    myWordList = myWords.split(' ')
    lenOfWords = len(myWordList)
    myWordDict = {}
    # hash table where key is the word, value is the number of times it appears
    for word in myWordList:
        myWordDict[word] = myWordList.count(word)
    # this is where we get the probabilities
    # you get the probability by getting the number of times the word appears and dividing
    # it by the length of the original string
    for key, val in myWordDict.items():
        print("{} = {}".format(key,val/lenOfWords))


    listOfRandomWords = []
    randomWordDict = {}
    while numRandomSelections != 0:
        randomWordList = random.sample(myWordList, 1) # this returns a list
        randomWord = ''.join(randomWordList)
        listOfRandomWords.append(randomWord)
        numRandomSelections -= 1
    for randomWord in listOfRandomWords:
        randomWordDict[randomWord] = listOfRandomWords.count(randomWord)

    print(randomWordDict)

if __name__ == "__main__":
    myWords = "one fish two fish red fish blue fish"
    probabilistic_word_sampler(myWords, 10000)
