import sys
import random

def rearrangeArguments():
    arguments = list()

    # gets all arguments and puts it in a list so we can use that list to rearrange the items in the list
    for arg in sys.argv:
        if arg != sys.argv[0]: # because item 0 is the file name. We don't want to add that to our arguments list
            arguments.append(arg)

    rearrangedArguments = list()

    while len(arguments) > 0:
        # passes all items in a random order to rearrangedArgument's list
        randomItem = random.randint(0, len(arguments) -1)
        rearrangedArguments.append(arguments[randomItem])
        arguments.pop(randomItem)

    return " ".join(rearrangedArguments)

if __name__ == "__main__":
    shuffleArgs = rearrangeArguments()
    print(shuffleArgs)
