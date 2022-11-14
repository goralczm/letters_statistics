import collections
import string
import json
import os
import re

alphabet = string.ascii_lowercase
vowel = [*'aąeęiouóy']

# Sorts dictionary by values from lowest to highest
def sortDictByVal(dict):
    return {key: value for key, value in sorted(dict.items(), key=lambda item: item[1])}


# Returns how many letters are in given dictionary containing letter occurances
def totalLetters(occurances_dict):
    return sum(occurances_dict.values())


# Returns how many vowels are in given dictionary. containing letter occurances
def vowelAmount(occurances_dict):
    vowels = 0
    for letter in occurances_dict.keys():
        if (letter in vowel):
            vowels += occurances_dict[letter]
    return vowels


# Return list of two items, first is the most commong letter, second is how many of them are in given occurances dictionary
def mostCommonLetter(occurances_dict):
    sortedDict = sortDictByVal(occurances_dict)
    last_key = list(sortedDict.keys())[-1]
    return [last_key, occurances_dict[last_key]]


# Return formated percent amount of a in b
def percentAmount(a, b):
    return round((a/b)*100, 2)


def readStatistics(file_name):
    try:
        with open(f'text_statistics/{file_name}_statistics.json', "r", encoding='utf-8') as jsonFile:
            print('Reading json file')
            data = json.load(jsonFile)
            return data
    except FileNotFoundError:
        print('Trying to save statistics')
        return saveStatistics(file_name)

def saveStatistics(file_name):
    try:
        with open(f'text_sources/{file_name}.txt', 'r', encoding='utf-8') as words_file:
            with open(f'text_statistics/{file_name}_statistics.json', 'w', encoding='utf-8') as words_stats_file:

                print('Saving statistics...')

                statistics = {}
                file_content = words_file.readlines()

                occurances = collections.defaultdict(int)

                max_line_len = 0
                longest_words = []

                print('Counting letters...')
                
                for line in file_content:
                    clean_line = line.strip()
                    clean_line_no_special = re.sub('\W+', " ", clean_line)
                    clean_line_no_special = re.sub('[0 - 9]', " ", clean_line_no_special)
                    words = clean_line_no_special.split()
                    
                    for word in words:
                        for letter in word:
                            occurances[letter.lower()] += 1
                    
                        word_len = len(word)
                        if (max_line_len < word_len):
                            max_line_len = word_len
                            longest_words = [word]
                        elif (max_line_len == word_len):
                            longest_words.append(word)

                print('Calculating statistics...')

                total_letters = totalLetters(occurances)
        
                most_common_letter = mostCommonLetter(occurances)
                most_common_letter_percent = percentAmount(most_common_letter[1], total_letters)
        
                vowel_amount = vowelAmount(occurances)
                vowel_percent = percentAmount(vowel_amount, total_letters)
        
                consonant_amount = total_letters - vowel_amount
                consonant_percent = 100 - vowel_percent

                print('Combining statistics...')
                
                statistics['occurances'] = occurances
                statistics['most_common_letter'] = [most_common_letter, most_common_letter_percent]
                statistics['total_letters'] = total_letters
                statistics['vowels'] = [vowel_amount, vowel_percent]
                statistics['consonants'] = [consonant_amount, consonant_percent]
                statistics['longest_words'] = [len(longest_words), longest_words]

                print('Saving statistics...')

                json_data = json.dumps(statistics, indent=4)
                words_stats_file.write(json_data)
            print('Statistics has been saved successfully')
            return readStatistics(file_name)
    except FileNotFoundError:
        print('File does not exist')
        return None


def printFileStatistics(file_name, force_new_save = False):
    if (force_new_save):
        statistics = saveStatistics(file_name)
    else:
        statistics = readStatistics(file_name)

    total_letters = statistics['total_letters']
    most_common_letter = statistics['most_common_letter']
    vowel_amount = statistics['vowels'][0]
    vowel_percent = statistics['vowels'][1]
    consonant_amount = statistics['consonants'][0]
    consonant_percent = statistics['consonants'][1]
    longest_words = statistics['longest_words']

    print(f'\nTotal letters: {total_letters}')
    print(f'Most common letter is "{most_common_letter[0][0]}" with {most_common_letter[0][1]} occurances (~{most_common_letter[1]}%)')
    print(f'There are {vowel_amount} vowels (~{vowel_percent}%)')
    print(f'There are {consonant_amount} consonants (~{consonant_percent}%)')
    print(f'There are {longest_words[0]} longest words with {len(longest_words[1][0])} letters each')
    print(f'  First five longest words are "{", ".join(longest_words[1][0:5])}"')

files_to_test = ['slowa', 'words_alpha', 'pan-tadeusz', 'romeo_and_juliet', 'hamlet', 'rozprawka']
#files_to_test = ['pan-tadeusz']
for file in files_to_test:
    print(f'------------------------ {file}.txt ------------------------')
    printFileStatistics(file)
    print(f'------------------------ {file}.txt ------------------------\n')