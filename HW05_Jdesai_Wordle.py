import random
import logging
import csv
from collections import  OrderedDict
class wordle:

    def valid_words(self):
        with open('words.txt', 'r+') as f_pointer:
            content = f_pointer.read().split('\n')
            f_pointer.close()
            words = []
            for word in content:
                if len(word) != 5:
                    continue
                words.append(word)
            return words

    def words_list_to_file(list):
        with open('valid_words.txt', 'w') as f_pointer:
            f_pointer.writelines([str(i) + '\n' for i in list])
            f_pointer.close()

    def order(trials, user_input):  # function making file for storing in csv
        letter_list = OrderedDict()
        alphabet = [str(i) for i in 'abcdefghijklmnopqrstuvwxyz']  # comparing every to every letters
        for letter in alphabet:
            letter_list[letter] = [0, 0, 0, 0, 0]  #all index frequency
        while trials > 0:
            user_input = input('Enter a word: ')  #each nd every trials
            for index in range(len(user_input)):
                temp = letter_list[user_input[index]]
                index = index + 1
            trials -= 5
            for letter in letter_list:
                different_letters = ('%s -> %s' % (letter, letter_list[letter]))  # seperate letter and occurence

            with open('letterFrequency.csv', 'w') as csv_files:  # adding in csv files
                writer = csv.DictWriter(csv_files, fieldnames=letter_list.keys())  # writing into csv files the letters
                # and occurance
                writer.writeheader()
                writer.writerows(letter_list)  # outputs

    def get_input_from_user(trial):
        prompt_message = 'Enter a word: ' if trial > 5 else 'Reenter a word: '
        return input(prompt_message)

    def check_if_entered_word_is_valid(word):
        return word.isalpha() and len(word) == 5


def has_user_guessed_the_right_word(word, codeword):
    return word == codeword

def log_to_file(level, message):
    logging.basicConfig(filename='app.log', filemode='a+', format='%(levelname)s - %(message)s', level=logging.DEBUG)
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    else:
        logging.warning(message)

def get_spot_name(spot_val):
    if spot_val:
        if spot_val == 'NA':
            return '"'

        return ''

    return '`'


def position_check_for_letters(user_input, codeword):
    arr = list(user_input)
    code_arr = list(codeword)
    result = []
    for letter_index in range(len(codeword)):
        user_word_letter = arr[letter_index]
        if user_word_letter not in code_arr:
            result.append('NA')
            continue
        if user_word_letter != code_arr[letter_index]:
            result.append(False)
            continue
        result.append(True)

    return result


def validate_letter_position(positions, user_input):
    for i in range(len(positions)):
        decider = positions[i]
        user_char = user_input[i]
        print('%s%s' % (user_char, get_spot_name(decider)))

def get_word():
    with open('words.txt', 'r+') as file_pointer:
        content = file_pointer.read().split('\n')
        random_word = content[random.randint(0, len(content) - 1)]
        word = random_word if len(random_word) > 0 and len(random_word) == 5 else get_word()
        file_pointer.close()
        log_to_file('info', 'got files from words.txt!!!')
        return word


def check_if_word_in_dictionary(word):
    with open('words.txt', 'r+') as file_pointer:
        content = file_pointer.read().split('\n')
        is_word_present = word in content
        file_pointer.close()
        log_to_file('info', 'word is in the file')
        return is_word_present
