import collections
import string
import json
import os

alphabet = string.ascii_lowercase
vowel = [*'aąeęiouóy']

# Function takes list of lines and based on them counts occurances of each letter
def occurances(letterBase):
    alphabetDict = collections.defaultdict(int)
    for line in letterBase:
        cleanLine = line.strip()
        for letter in cleanLine:
            alphabetDict[letter] += 1
    return alphabetDict


# Sorts dictionary by values from lowest to highest
def sortDictByVal(dict):
    return {key: value for key, value in sorted(dict.items(), key=lambda item: item[1])}


# Returns how many letters are in given dictionary containing letter occurances
def totalLetters(occurancesDict):
    return sum(occurancesDict.values())


# Returns how many vowels are in given dictionary. containing letter occurances
def vowelAmount(occurancesDict):
    vowels = 0
    for letter in occurancesDict.keys():
        if (letter in vowel):
            vowels += occurancesDict[letter]
    return vowels


# Return list of two items, first is the most commong letter, second is how many of them are in given occurances dictionary
def mostCommonLetter(occurancesDict):
    sortedDict = sortDictByVal(occurancesDict)
    lastKey = list(sortedDict.keys())[-1]
    return [lastKey, occurancesDict[lastKey]]


# Returns occurances of given letter from occurances dictionary
def letterOccurance(occurancesDict, letter):
    return occurancesDict[letter]


def percentAmount(a, b):
    return round((a/b)*100, 2)


def readStatistics(file_name):
    try:
        with open(f'{file_name}_statistics.json', "r", encoding='utf-8') as jsonFile:
            print('Reading json file')
            data = json.load(jsonFile)
            return data
    except FileNotFoundError:
        print('Trying to save statistics')
        return saveStatistics(file_name)

def saveStatistics(file_name):
    try:
        with open(f'{file_name}.txt', 'r', encoding='utf-8') as wordsFile:
            with open(f'{file_name}_statistics.json', 'w', encoding='utf-8') as words_stats_file:

                print('Saving statistics...')

                statistics = {}
                file_content = wordsFile.readlines()

                occurances = collections.defaultdict(int)

                max_line_len = 0
                longest_words = []

                print('Counting letters...')

                for line in file_content:
                    clean_line = line.strip()

                    for letter in clean_line:
                        occurances[letter] += 1
                    
                    wordLen = len(clean_line)
                    if (max_line_len < wordLen):
                        max_line_len = wordLen
                        longest_words = [clean_line]
                    elif (max_line_len == wordLen):
                        longest_words.append(clean_line)

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

#files_to_test = ['slowa', 'words_alpha', 'pan-tadeusz']
files_to_test = ['pan-tadeusz']
for file in files_to_test:
    print(f'------------------------ {file}.txt ------------------------')
    printFileStatistics(file, True)
    print(f'------------------------ {file}.txt ------------------------\n')