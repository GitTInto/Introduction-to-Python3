# Purpose           : This program reads the file "gettysburg.txt"  and calculate the total words,
#                     writes the number of occurrences of each word
#                     and the total number of words into a user chosen file.
# Assignment Number : 9.1
# Author            : Tinto T. Kurian




import re           # importing regular expression
import operator     # importing operator
import os

file_dict = {}      # declares a empty dictionary

file_type = '.txt'  # declares the type (extension) of the output file.




# The below function gets the name of the output file as an input from the user,
# Appends the file name with extension .txt
# for the below conditions raises exception and prompts user to enter a new output file name
#   1. If the output file name entered is same as the input file "gettysburg.txt" to avoid overwriting the input file.
#   2. If an empty string was passed as the input file name
#   3. If the output file already exists, gives the user an open to chose another file name or can overwrite the existing output file.
def get_output_filename():
    while True:
        try:
            output_file = str(input('\nEnter the name of the output file (without the file extension,'
                                    ' the output file will always be {}) :\n'.format(file_type)))
            output_file = output_file + file_type
            if output_file == 'gettysburg.txt':                 # If the output file name is "gettysburg.txt" raises and exception
                raise Exception('The output file name cannot be same as the input file name "gettysburg",'
                                ' Please chose another name for the output file.')
            if output_file == '.txt':                               # If the output filename is empty string raises and exception
                raise Exception('Please enter a non empty string as filename')
            if os.path.isfile(output_file) is True:             # Checks if the file exist and gives the user option to overwrite or chose a different file name.
                re_write = input('\nThe file {0} exist, Do you wnat to re-write ?,'
                                 ' please enter "n" to chose another file name else enter any other key to overwrite {0}\n'.format(output_file)).lower()
                if re_write =='n':
                    raise Exception('You chose not to re-write the existing file, Please chose another file name')
        except Exception as e:                      # Caches any other exception and print the exception.
            print(e)
        else:
            return output_file


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


# Below function orders the count in reverse order to be used by the process file.
def sort_dict(sort_dict):
    sorted_dict = sorted(sort_dict.items(), key=operator.itemgetter(1), reverse=True) # gets the count and reverse sorts it.
    return sorted_dict



# The below function opens the output file in append mode ( as the main program has already written a line into  the file)
# writes the header, calls the sort_dict function
# and writes the words and its count into the output_file.
def process_file(output_file):
    try:
        with open(output_file, 'a') as write_file:
            write_file.write('\n{0:30}{1:10}'.format('Word', 'Count'))            # Prints the header
            write_file.write('\n{}'.format('_' * 35))
            sorted_dict = sort_dict(file_dict)                                  # Calls the sort_dict function
            for key, value in sorted_dict:
                write_file.write('\n{0:30}{1:<10}'.format(key, value))          # Prints the word and the Count
    except Exception as e:
            print('\nThe program have been terminated with the below error \n{}'.format(e))
    else:
        print('\nThe output have been written to the file {} successfully.'.format(output_file))



# This is the main function which opens the "gettysburg.txt" file and calls the process_
# line function for each line in the file and then calls get_output_filename to get the output file name from the user
# Opens the Output file and writes the total number of words to the file and then calls process_file function.
def main():
    try:
        with open('gettysburg.txt', 'r') as gba_file:
            for line in gba_file:
                Process_line(line)
    except Exception as e:
        print('\nThe program have been terminated with the below error \n{}'.format(e))
    else:
        output_file = get_output_filename()
        try:
            with open(output_file, 'w') as write_file:
                write_file.write('\nThe total number of words in the file is : {}\n'.format(sum(file_dict.values())))   # Writes the total number of words.
        except Exception as e:
            print('\nthe program have been terminated with the below error \n{}'.format(e))
        else:
            process_file(output_file)
    finally:
        print('\n**** This is the end of the program ****')


if __name__ == '__main__':
    main()



