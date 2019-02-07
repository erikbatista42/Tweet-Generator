import random
import sys

def table_histogram(given_list):
    table = dict()

    for i in given_list:
        # puts the KEY as the word
        # and puts the VALUE as the number of times the key appears
        table[i] = table.get(i, 0) + 1

    return table


def list_histogram(word_list):
    masterList = []
    for wordIndex in range(len(word_list)):
        modelList = [word_list[wordIndex], word_list.count(word_list[wordIndex])]
        if modelList in masterList:
            wordIndex += 1
        else:
            masterList.append([word_list[wordIndex], word_list.count(word_list[wordIndex])])
    return masterList


def tuples_histogram(word_list):
    masterList = []
    for wordIndex in range(len(word_list)):
        modelTuple = (word_list[wordIndex], word_list.count(word_list[wordIndex]))
        if modelTuple in masterList:
            wordIndex += 1
        else:
            masterList.append((word_list[wordIndex], word_list.count(word_list[wordIndex])))
    return masterList


def unique_words(histogram):
    uniques = list()

    for key, value in histogram.items():
        # if the value is 1, it means the word is unique
        if value == 1:
            uniques.append(key)
        return len(uniques)


def frequency(histogram, word):
    # returns the num of times the given word appears in a histogram
    return histogram[word]


if __name__ == "__main__":

    fish_list = "one fish two fish red fish blue fish".split()

    # file = open("20k.txt", "r")
    # word_list = file.read().split()

    table_gram = table_histogram(fish_list)
    print(table_gram)

    list_gram = list_histogram(fish_list)
    print(list_gram)

    tuple_gram = tuples_histogram(fish_list)
    print(tuple_gram)

    frequency_of_word_in_table = frequency(table_gram, "fish")
    print(frequency_of_word_in_table)

    # file.close()

