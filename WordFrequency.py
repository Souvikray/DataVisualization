from matplotlib import pyplot as plt
import sys
import argparse


def main():
    # create a parser to parse the command line arguments
    parser = argparse.ArgumentParser()
    # add arguments to the parser
    parser.add_argument("word", help="the word to be searched in the file")
    parser.add_argument("filename", help="the path to the file")
    # save the arguments in a variable
    args = parser.parse_args()
    # ensure the program doesn't crash or terminate abruptly due to wrong filename provided
    try:
        open(args.filename)
    except FileNotFoundError:
        sys.stderr.write("The file with the name " + args.filename + " does not exist")
        # stop the execution of the program
        sys.exit(1)

    # call the word_frequency function to calculate the frequence for the given word
    word_frequency(args.word, args.filename)

def word_frequency(word, filename):
    '''
    we will take in a file, read each word, log how often they appear, 
    and save it all to a dictionary data type.
    '''
    # initialize an empty dictionary that will store each word and its frequency
    w_freq = {}
    for line in open(filename):
        split = line.split(" ")
        for entry in split:
            if w_freq.__contains__(entry):
                w_freq[entry] = int(w_freq.get(entry)) + 1
            else:
                w_freq[entry] = 1

    # if the given word is not found
    if not word in w_freq:
        sys.stderr.write("The word " + word + " does not exist in the file " + filename)
        # stop the execution of the program
        sys.exit(1)

    # sort the w_freq dictionary on the basis of decreasing order of word frequency
    sorted_w_freq = sorted(w_freq.items(), key=lambda x: x[1], reverse=True)
    # define a list that stores all the words' frequency
    occurence_list = []
    # define a list that stores all the words' rank
    rank_list = []
    # declare a variable that will store the given word's frequency
    given_word_freq = 0
    # declare a variable that will store the given word's rank
    given_word_rank = 0
    # starting rank
    entry_num = 1
    for entry in sorted_w_freq:
        if entry[0] == word:
            given_word_rank = entry_num
            given_word_freq = entry[1]

        rank_list.append(entry_num)
        entry_num += 1
        occurence_list.append(entry[1])

    # plot the graph
    # assign a title for the graph
    plt.title("Word Frequency Visualization")
    # assign a y label
    plt.ylabel("Frequency of words")
    # assign a x label
    plt.xlabel("Rank of words")
    # create a log base 10 graph
    plt.loglog(rank_list, occurence_list, basex=10)
    # plot the coordinate for the given word
    plt.scatter(given_word_rank, given_word_freq, color="red", marker="*", s=100, label=word)
    # show the plot
    plt.show()

if __name__ == "__main__":
    main()
