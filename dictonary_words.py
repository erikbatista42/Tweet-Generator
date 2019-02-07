import sys
import random

def get_num_of_rand_words_from(given_list, num_of_words_wanted):
    '''take console argument num and get num of random words'''
    randWords = random.sample(given_list, num_of_words_wanted)

    #return a "sentence"
    return " ".join(randWords) + "."


if __name__ == "__main__":

    fish_list = "one fish two fish red fish blue fish".split()

    try:
        '''num of words wanted typed in terminal argument'''
        with open("20k.txt", "r") as file:
            wordList = file.read().split()

        wanted_words_num = int(sys.argv[1])

        output_sentence = get_num_of_rand_words_from(wordList, wanted_words_num)
        print(output_sentence)

    except IndexError:
        '''if no num input in terminal argument, use the fish list'''
        fish_sentence = get_num_of_rand_words_from(fish_list, 2)
        print(fish_sentence)
