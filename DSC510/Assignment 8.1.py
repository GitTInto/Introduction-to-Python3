# Purpose           : This program calculate the total words, and output the number of occurrences of each word in the file.
# Assignment Number : 8.1
# Author            : Tinto T. Kurian


import re           # importing regular expression
import operator     # importing operator

file_dict = {}      # declares a empty dictionary



# Below function process one line and splits the line on
# non-alphanumeric character and populates a list.
def Process_line(line):
    file_list = (re.split(r'\W+', line))      #\W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
    add_word(file_list)


# Below function iterates through each word in the list
# and populates the word and the count of the word into a dictionary.
def add_word(file_list):
    for word in file_list:
        word = word.lower()                             # Converts the words to lower case to eliminate mismatch due to case.
        if word != '':                                  # eliminates the empty string in the list
            file_dict[word] = file_dict.get(word, 0)+1  # using the get function, assign default value to 0 and count all words in the list


# Below function orders the count in reverse order to be used by the pretty print
def sort_dict(sort_dict):
    sorted_dict = sorted(sort_dict.items(), key=operator.itemgetter(1), reverse=True) # gets the count and reverse sorts it.
    return sorted_dict


# The below function prints the length of the dictionary and prints the count from high to low.
def Pretty_print(print_dict):
    print('\nLength of the dictionary: {}\n'.format(sum(print_dict.values())))  # Prints the Length
    print('{0:30}{1:10}'.format('Word', 'Count'))                               # Prints the header
    print('{}'.format('_'*35))
    sorted_dict = sort_dict(file_dict)                                          # Calls the sort_dict function
    for key, value in sorted_dict:
        print('{0:30}{1:<10}'.format(key,value))                                # Prints the word and the Count


# This is the main function which opens the file and calls the process_
# line function for each line in the file and then calls the pretty_print function.
def main():
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        Process_line(line)
    Pretty_print(file_dict)


if __name__ == '__main__':
    main()

