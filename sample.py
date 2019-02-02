import sys
import random

'''Run this file in the command line'''


def sample():
    #select a random word out of the text file that is typed on the terminal
    file_name = sys.argv[1]
    file = open(file_name, "r")
    word_list = file.read().split()

    index = random.choice(word_list)

    return index

if __name__ == "__main__":
    test = sample()
    print(test)
