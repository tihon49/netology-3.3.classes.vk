from config import *
import requests
from pprint import pprint



access_token = ACESS_TOKEN_USER # пользовательский
app_token    = APP_TOKEN        # из приложения
app_id       = APP_ID           # id приложения


DOMAIN     = 'vindevi'
USER       = 148226630 # Ден
MY_USER_ID = 4305103   # мой ID
VERSION    = 5.103
METHOD     = 'users.getSubscriptions' # 'friends.getOnline'  #'users.get' #   'friends.get'
                                      # пример:  url = f'https://api.vk.com/method/{METHOD}'


def get_groups_names(user):
    url = f'https://api.vk.com/method/users.getSubscriptions'
    params = {'access_token': access_token,
              'user_id': user,
              'extended': 1,
              'count': 200,
              'v': VERSION
              }

    response = requests.get(url, params=params)
    data = response.json()
    groups = data['response']['items']

    for group in groups:
        try:
            print(group['name'])
        except:
            pass



if __name__ == '__main__':
	get_groups_names(USER)