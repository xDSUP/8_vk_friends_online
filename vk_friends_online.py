import vk
import getpass


APP_ID = 5822638


def get_user_login():
    login = input("Введите ваш логин : ")
    return login


def get_user_password():
    password = getpass.getpass(prompt="Введите ваш пароль : ")
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        scope='friends',
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    list_friends = api.friends.getOnline()
    user_ids = ", ".join(map(str, list_friends))
    return api.users.get(user_ids=user_ids)


def output_friends_to_console(friends_online):
    print ("Friends online :")
    for friend in friends_online:
        print ("name: %s %s" % (friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
