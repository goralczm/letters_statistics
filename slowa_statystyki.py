import string

alphabet = string.ascii_lowercase
vowel = list('aąeęiouóy')

def returnOccurances(letterBase):
    alphabetDict = { letter : 0 for letter in alphabet}
    for line in letterBase:
        cleanLine = line.strip()
        for char in cleanLine:
            if (char not in alphabetDict.keys()):
                alphabetDict[char] = 1
            else:
                alphabetDict[char] += 1
    return alphabetDict

def sortDictionaryByValues(dictionary):
    return {key: value for key, value in sorted(dictionary.items(), key=lambda item: item[1])}

def returnTotalLettersAmount(dictionary):
    return sum(dictionary.values())

def returnVowelAmount(dictionary):
    vowels = 0
    for letter in dictionary.keys():
        if (letter in vowel):
            vowels += dictionary[letter]
    return vowels

def mostCommonLetter(dictionary):
    sortedDict = sortDictionaryByValues(dictionary)
    lastKey = list(sortedDict.keys())[-1]
    return [lastKey, dictionary[lastKey]]

def returnLetterOccurance(dictionary, letter):
    return dictionary[letter]

with open("slowa.txt", "r", encoding='utf-8') as wordsFile:
    content = wordsFile.readlines()
    letterOccurrances = returnOccurances(content)
    allLetters = returnTotalLettersAmount(letterOccurrances)
    mostCommon = mostCommonLetter(letterOccurrances)
    percentageAmount = round((mostCommon[1]/allLetters)*100, 2)
    print(f'Most common letter is {mostCommon[0]} with {mostCommon[1]} occurances, percentage amount is {percentageAmount}')