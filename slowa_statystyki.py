import collections
import string
import json

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

def importJsonData(fileName):
    with open(fileName, "r", encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)
        return data

with open("slowa.txt", "r", encoding='utf-8') as wordsFile:
    content = wordsFile.readlines()
    
    statisticsFile = importJsonData('statistics.json')
    occurances = statisticsFile['occurances'][0]

    #occurances = collections.defaultdict(int)
    
    maxLenght = 0
    longestWords = []
    mostRecursiveLine = ['', 0, '']
    
    for line in content:
        cleanLine = line.strip()
                
        # Letter occurances
        #for letter in cleanLine:
        #    occurances[letter] += 1
        
        # Longest word
        wordLen = len(cleanLine)
        if (maxLenght < wordLen):
            maxLenght = wordLen
            longestWords = [cleanLine]
        elif (maxLenght == wordLen):
            longestWords.append(cleanLine)
        
        # Most recursive letters word
        lettersCounter = collections.Counter(list(cleanLine))
        maxLetter = max(lettersCounter, key=lettersCounter.get)
        currentRecursive = [cleanLine, lettersCounter[maxLetter]]
        if (mostRecursiveLine[1] < currentRecursive[1]):
            mostRecursiveLine[0] = cleanLine
            mostRecursiveLine[1] = currentRecursive[1]
            mostRecursiveLine[2] = maxLetter
    
    totalLetters = totalLetters(occurances)
    
    mostCommonLetter = mostCommonLetter(occurances)
    mostCommonLetterPercent = percentAmount(mostCommonLetter[1], totalLetters)
    
    vowelAmount = vowelAmount(occurances)
    vowelPercent = percentAmount(vowelAmount, totalLetters)
    
    consonantAmount = totalLetters - vowelAmount
    consonantPercent = 100 - vowelPercent
    
    print(occurances)


    #print(f'Total letters: {totalLetters}')
    #print(f'Most common letter is "{mostCommonLetter[0]}" with {mostCommonLetter[1]} occurances (~{mostCommonLetterPercent}%)')
    #print(f'There are {vowelAmount} vowels (~{vowelPercent}%)')
    #print(f'There are {consonantAmount} consonants (~{consonantPercent}%)')
    #print(f'This are the {len(longestWords)} longest words with {maxLenght} letters each')
    #print(f'  First five longest words are "{"\", \"".join(longestWords[0:5])}"')
    #print(f'Word with most recursive letter is "{mostRecursiveLine[0]}" with {mostRecursiveLine[1]} occurances of letter "{mostRecursiveLine[2]}"')