# word dictionary
from PyDictionary import PyDictionary
import sys

dictionary = PyDictionary()

print("This is a basic python dictionary")
print("")

word = input("Enter your word: ")
if word == '':
    sys.exit

print(dictionary.meaning(word))