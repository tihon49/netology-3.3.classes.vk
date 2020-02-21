from config import *
import requests
from pprint import pprint



access_token = APP_TOKEN        # токен приложения
app_id       = APP_ID           # id приложения


DOMAIN       = 'vindevi'
USER         = 148226630 # Ден
MY_USER_ID   = 4305103   # мой ID
VERSION      = 5.103
METHOD       = 'users.getSubscriptions' # варианты запросов: 'friends.getOnline' / 'users.get' / 'friends.get'
                                        # пример:  url = f'https://api.vk.com/method/{METHOD}'


class User:
    def __init__(self, id):
        self.id = id

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

        for friend in user_1_friends:
            if friend in user_2_friends:
                common_friends.append(friend)

        return common_friends

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



Den   = User(USER)
Tihon = User(MY_USER_ID)



pprint(Den.get_common_friends(Den.id, Tihon.id))