from dictogram import *
from histograms import table_histogram
from sample import get_one_word_probability

# shoutout to Ramon for helping me build the Markov Chain
def markov_chain(word_list, num_of_words):
    terminate = False
    sentence = list()
    new_list = list()

    histogram = Dictogram(word_list)
    current_word = get_one_word_probability(histogram)
    sentence.append(current_word)

    for i in range(5, num_of_words):
        for index, word in enumerate(word_list):
            try:
                if word == current_word:
                    new_list.append(word_list[index + 1])
            except IndexError:
                terminate = True
                break

        if terminate == False:
            histogram = Dictogram(new_list)
            current_word = get_one_word_probability(histogram)
            sentence.append(current_word)
            new_list = []
        else:
            break

    return " ".join(sentence)


if __name__ == "__main__":
    # fish_list = "one fish two fish red fish blue fish blue green yellow".split()
    file = open("peterPan.txt", "r")
    word_list = file.read().split()
    # print(word_list)
    # print(table_histogram(word_list))
    # k = sample(table_histogram(word_list))
    # print(k)
    sentence = markov_chain(word_list, 15)
    print(sentence)


