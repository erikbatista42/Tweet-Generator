import sys
import random

def sample():
    #select a random word out of the text file that is typed on the terminal
    file_name = sys.argv[1]
    file = open(file_name, "r")
    word_list = file.read().split()

    index = random.choice(word_list)

    return index

def random_index(histogram):

    values = sum(histogram.values())
    rand_word = random.randint(0, values -1)
    counter = 0

    for key, value in histogram.items():
        counter += value

        if value > rand_word:
            return counter
        else:
            continue


if __name__ == "__main__":
    # test = sample()
    histogram = {"erik": 3, "bob": 1,"ben":1}
    random_index = random_index(histogram)
    print(random_index)
