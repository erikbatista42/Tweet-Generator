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
    master_list = []
    for word_index in range(len(word_list)):
        model_list = [word_list[word_index], word_list.count(word_list[word_index])]
        if model_list in master_list:
            word_index += 1
        else:
            master_list.append([word_list[word_index], word_list.count(word_list[word_index])])
    return master_list


def tuples_histogram(word_list):
    master_list = []
    for word_index in range(len(word_list)):
        model_tuple = (word_list[word_index], word_list.count(word_list[word_index]))
        if model_tuple in master_list:
            word_index += 1
        else:
            master_list.append((word_list[word_index], word_list.count(word_list[word_index])))
    return master_list


def num_of_unique_word_in(histogram):
    uniques = list()

    for key, value in histogram.items():
        # if the value is 1, it means the word is unique
        if value == 1:
            uniques.append(key)
        return "num of unique words: {}".format(len(uniques))


def frequency(histogram, given_word):
    # returns the num of times the given word appears in a histogram
    return histogram[given_word]


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

    uniques_in_gram = num_of_unique_word_in(table_gram)
    print(uniques_in_gram)

    frequency_of_word_in_table = frequency(table_gram, "fish")
    print(frequency_of_word_in_table)

    # file.close()

