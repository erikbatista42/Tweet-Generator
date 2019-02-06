def table_histogram(txt_file):
    word_list = txt_file.read().split()


    table = dict()

    for i in word_list:
        # puts the key as the word
        # and puts the value as the number of times the key appears
        table[i] = table.get(i, 0) + 1

    return table

def list_histogram(txt_file):
    my_word_list = ["erik", "erik", "erik", "mel" ,"bob"]
    new_list = []

    # c = cute_array.split(" ")
    # whole_list = list()
    for w in my_word_list:
        word_found = False
        if len(new_list) == 0:
            new_list.append([w,1])
        else:
            for this_word in my_word_list:
                if w in this_word[0]:
                    word_found = True
                    this_word[1] += 1
                if not word_found:
                    new_list.append([w,1])

    # print(newList)
    print(new_list)


def tuples_histogram(txt_file):
    new_list = []
    my_word_list = ["erik", "erik", "erik", "mel"]

    # for w in my_word_list:
    #     count = 0
    #     for t in my_word_list:
    #         if w == t:
    #             count += 1
    #     wtuple = (w, count)
    #     if w not in new_list:
    #         new_list.append(wtuple)
    # print(new_list)

    for i in my_word_list:
        count = 1
        for j in my_word_list:
            if i == j:
                my_word_list.remove(j)
                count += 1
        add = (i, count)
        new_list.append(add)
    print(new_list)

def unique_words(histogram):
    uniques = list()

    for key, value in histogram.items():
        # if the value is 1, it means the word is unique
        if value == 1:
            uniques.append(key)
        return len(uniques)

def frequency(histogram, word):
    # returns the num of times the word appears in a histogram
    return histogram[word]

if __name__ == "__main__":
    file = open("20k.txt", "r")

    myWords = "one fish two fish red fish blue fish"
    my_table_histogram = table_histogram(file)

    tuple_histogram = tuples_histogram(file)

    frequency = frequency(my_table_histogram, "bizjournalshire")
    print(frequency)
    file.close()

    # print("Unique words in histogram-> {} \nFrequency-> {}".format(unique_words_in_histogram, frequency))

