import json
from difflib import get_close_matches

file = open('data.json')
data = json.load(file)

def trans(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    elif word.title() in data:
            return data[word.title()]
    else:
        return "word is not available"

word_input = input('Enter Word:')

output = trans(word_input)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
