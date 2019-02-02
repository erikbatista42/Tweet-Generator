import sys
import random

def sample():
    #select a random word out of the text file that is typed on the terminal
    file_name = sys.argv[1]
    file = open(file_name, "r")
    word_list = file.read().split()

    index = random.choice(word_list)

    return index

def random_index():
    '''
    Make the .choice method but words will be chosen based on frequency.
    So if the word 'fish' appears 3x and 'erik' appears 1x,
    the program will choose the most *frequent* word. "fish" like 75% of the time
    '''

    # I'm thinking of..
    # makig a hash table
    # measure the occurances - histogram

    # do if and else statements to choose

    myList = ["erik","erik","erik","mel"]
    table = {}

    for i in myList:
        table[i] = table.get(i, 0) + 1


    return table


if __name__ == "__main__":
    # test = sample()
    random_index = random_index()
    print(random_index)
