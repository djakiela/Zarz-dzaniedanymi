# import json

# data=json.load(
#     open("simple_data.json")
# )
# user_input = input('Podaj wyraz: ')

# print(f'Data from Simple JSON:\n{data}')

# print(f'the value(s) for keyword: {user_input} is / are {data[user_input]}')

# print(data.keys())

import json

data=json.load(
    open("simple_data.json")
)

def translate(w):
    return data[w]

# def nasza_funkcja(ui):
#     if ui in data.keys():
#         return data[ui]
#     else:
#         return f'Podanego slowa {ui} nie ma w slowniku'

word = input('Podaj wyraz: ')

print(f'Dla podanego klicza: {word} wynik to:\n{translate(word)}')

# print(f'RESULT:\n{nasza_funkcja(user_input)}')
