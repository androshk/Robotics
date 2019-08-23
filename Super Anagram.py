words = input("Enter words: ")
words = words.split()
wordOne = words[0]
wordTwo = words[1]
wordOne_1 = wordOne[0]
wordTwo_1 = wordTwo[0]
wordOneEnd = wordOne[-1]
wordTwoEnd = wordTwo[-1]

firstWord = str(wordOne)
secondWord = str(wordTwo)
lettersOne = sorted(firstWord)
lettersTwo = sorted(secondWord)

if lettersOne == lettersTwo:
    if wordOne_1 == wordTwo_1:
        if wordOneEnd == wordTwoEnd:
            print("Super Anagram!")
        else:
            print("Huh?")
else:
  print("Huh?")
