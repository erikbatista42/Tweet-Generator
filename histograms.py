def hash_table_histogram(txt_file):
    word_list = txt_file.read().split()


    table = dict()

    for i in word_list:
        # puts the key as the word
        # and puts the value as the number of times the key appears
        table[i] = table.get(i, 0) + 1

    return table

def list_histogram(txt_file):
    cute_array = (erik, erik, erik, mel ,bob)


    eh = cute_array.split(" ")
    whole_list = list()

    for i in eh:
        whole_list.append(eh.count(i))
        count = 0

    # print(newList)
    print(whole_list)


def tuples_histogram(txt_file):
    pass

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
    table_histogram = hash_table_histogram(file)
    # print(table_histogram)
    # array_histogram = list_histogram(file)
    # print(array_histogram)

    tuple_histogram = tuples_histogram(file)

    # unique_words_in_histogram = unique_words(table_histogram)
    frequency = frequency(table_histogram, "bizjournalshire")
    print(frequency)
    file.close()

    # print("Unique words in histogram-> {} \nFrequency-> {}".format(unique_words_in_histogram, frequency))

