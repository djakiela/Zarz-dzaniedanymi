import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data.keys:
        return data[w]
    elif w.title() in data: # for instance Texas or Delhi
        return data[w.title{}]
    elif w.upper() in data: # for instance USA or NATO
        return data[w.upper{}]
    elif len(get_close_matches{w,data.keys()}) > 0:
        yn = input("Czy chciałeś podać %s? Podaj T lub N: " %get_close_matches{w,data.keys()}[0])
        if yn == "T":
            return data[get_close_matches{w,data.keys()}[0]]
        elif yn == "N":
            return f'Wyraz = {w} nie istnieje w pliku. Sprawdź ponownie.'
        else:
            return 'Podano niewłaściwą literę.'
    else:
        return f'Wyraz = {w} nie istnieje w pliku. Sprawdź ponownie.'

word = input("Podaj wyraz: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)