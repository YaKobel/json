import json

username = input("Введите ваше имя: ")

filename = 'user.json'
with open(filename, 'w') as fl:
    json.dump(username, fl)
    print("Мы запомним ваше имя как" + username + "!")

