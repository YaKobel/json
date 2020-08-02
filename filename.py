import json

username = input("Введите ваше имя: ")

filename = 'user.json'
with open(filename, 'w', encoding="utf-8") as fl:
    json.dump(username, fl, ensure_ascii=False)
    print("Мы запомним ваше имя как " + username + "!")

