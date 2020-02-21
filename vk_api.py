from config import *
import requests
from pprint import pprint



access_token = APP_TOKEN        # токен приложения
app_id       = APP_ID           # id приложения
VERSION      = 5.103



class User:
    def __init__(self, id):
        self.id = id


    def __str__(self):
        return f'https://vk.com/id{self.id}'

    # отправка request'a / получение response'а
    def get_response(self, url, params):
        response = requests.get(url, params=params)
        data = response.json()
        return data


    # получаем список групп пользователя. type => list
    def get_groups_names(self):
        url = f'https://api.vk.com/method/groups.get' #'users.getSubscriptions'
        params = {'access_token': access_token,
                  'user_id': self.id,
                  'extended': 1,
                  'count': 1000,
                  'v': VERSION
                  }

        data = self.get_response(url, params)
        groups = data['response']['items']
        return [group['name'] for group in groups]


    # получаем список с друзьями. type => list
    def get_friends(self, user_id): 
        url = f'https://api.vk.com/method/friends.get'
        params = {'access_token': access_token,
                  'v': VERSION,
                  'user_id': user_id,
                  'order': 'hints',
                  'fields': 'nickname,domain,city,photo_200_orig,online',
                  'name_case': 'nom'
                  }

        data = self.get_response(url, params)
        friends_id = [friend['id'] for friend in data['response']['items']]
        return friends_id


    # полчучаем список общих друзей у двух пользователей. type => list
    def get_common_friends(self, user_1, user_2):
        user_1_friends = self.get_friends(user_1)
        user_2_friends = self.get_friends(user_2)
        common_friends = []
        common_friends_classes = []

        for friend in user_1_friends:
            if friend in user_2_friends:
                common_friends.append(friend)

        for i in common_friends:
            user_name = str(i)
            user_name = User(i)
            common_friends_classes.append(user_name)

        return common_friends_classes


    # получаем список друзей онлайн. type => dict
    def get_friends_online(self):
        url = 'https://api.vk.com/method/friends.getOnline?v=5.52&access_token='
        params = {
                 'access_token': access_token,
                 'v': VERSION,
                 'user_id': self.id
                 }

        data = self.get_response(url, params=params)
        return data['response']



def dz_number_2():
    try:
        user_input = input('введите команду в виде: "id_user_1 & id_user_2": ').split('&')
        user1 = User(int(user_input[0]))
        user2 = User(int(user_input[1]))

        pprint(user1.get_common_friends(user1.id, user2.id))

        print(f'\nссылка на пользователя №1: {user1}')
        print(f'ссылка на пользователя №2: {user2}')

    except Exception as e:
        print(f'error: {e}')



if __name__ == '__main__':
    dz_number_2()