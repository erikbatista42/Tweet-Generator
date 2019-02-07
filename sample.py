import sys
import random

def choose_random_word_from(word_list):
    rand_index = random.randint(0, len(word_list) -1)
    return word_list[rand_index]


def probability_of_words_in(word_list):
    lenOfWords = len(word_list)
    myWordDict = {}
    # hash table where key is the word, value is the number of times it appears
    for word in word_list:
        myWordDict[word] = word_list.count(word)
    # you get the probability by getting the number of times the word appears and dividing it by the length of the word_list
    for key, val in myWordDict.items():
        print("{} = {}".format(key,val/lenOfWords))


def num_of_times_to_run_probabilities_in(word_list, num_of_random_selections):
    random_words_list = []
    random_word_dict = {}
    while num_of_random_selections != 0:
        selected_random_word_list = random.sample(word_list, 1) # this returns a list
        random_word = ''.join(selected_random_word_list)
        random_words_list.append(random_word)
        num_of_random_selections -= 1
    for random_word in random_words_list:
        random_word_dict[random_word] = random_words_list.count(random_word)

    print(random_word_dict)


if __name__ == "__main__":
    fish_list = "one fish two fish red fish blue fish".split()

    try:
        '''if file is typed in terminal argument'''
        file_name = sys.argv[1]
        file = open(file_name, "r")
        word_list = file.read().split()
        probability_of_words_in(word_list)
        num_of_times_to_run_probabilities_in(word_list, 10000)
    except IndexError:
        '''if no input is taken, use the fish_list'''
        probability_of_words_in(fish_list)
        num_of_times_to_run_probabilities_in(fish_list, 10000)





