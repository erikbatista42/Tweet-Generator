def histogram(txtFile):
    #return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
    wordList = txtFile.read().split()
    wl = ["mel","mel","erik","bob","bob","ana"]
    table = dict()

    for i in wl:
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

    print("Histogram: ")
    print(histogram)

    print("Unique words in histogram: ")
    print(uniqueWordsInHistogram)

    print("Frequency: ")
    print(frequency)

    file.close()

