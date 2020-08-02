import json

def get_username:
    """Получает имя пользователя, если оно есть"""
    filename = 'user.json'
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user


def greet_user:
    """Привтетсвие пользователя"""

    username = get_username()
    if username:
        print("Добро пожаловать " + user + "!")
    else:
        username = input("Вдедите ваше имя: ")
        filename = 'user.json'
        with open(filename, 'w', encoding="utf-8") as fl:
            json.dump(username, fl, ensure_ascii=False)
            print("Мы запомним ваше имя, как " + username + " !")

greet_user()