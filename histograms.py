def histogram(txt_file):
    #return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
    wordList = txt_file.read().split()
    table = dict()

    for i in wordList:
        table[i] = table.get(i, 0) + 1 # .get allows you to specify a default value if the key does not exist.
    return table

def unique_words(histogram):
    #returns the total count of unique words in the histogram
    uniques = list()
    for key, value in histogram.items():
        if value == 1:
            uniques.append(key)
    return len(uniques)

def frequency(histogram, word):
    #returns the number of times that word appears in a text.
    #For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.

    # goes into histogram table and gets value
    return histogram[word]

if __name__ == "__main__":
    file = open("20k.txt", "r")

    histogram = histogram(file)
    uniqueWordsInHistogram = unique_words(histogram)
    frequency = frequency(histogram, "erik")

    print("Histogram-> {} \nUnique words in histogram-> {} \nFrequency-> {}".format(histogram, uniqueWordsInHistogram, frequency))

    file.close()

