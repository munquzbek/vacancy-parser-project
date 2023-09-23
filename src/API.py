from abc import ABC, abstractmethod

import requests
import json


class API(ABC):

    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HeadHunterAPI(API):
    api_url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_query):
        params = {
            'text': search_query,
            'per_page': 5
        }
        response = requests.get(url=HeadHunterAPI.api_url, params=params)
        data = response.content.decode()
        vacancies = json.loads(data)
        for vac in range(params['per_page']):
            print(vacancies['items'][vac]['name'])


class SuperJobAPI(API):
    api_url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, search_query):
        headers = {
            'X-Api-App-Id': 'v3.h.4533236.0914b38d06ea31a5db7c2ef0784c59f472416865.'
                            'ee894d426ffb4deb94243f3f320d1bafe22df69b'
        }
        params = {
            'keyword': search_query,
            'count': 5
        }
        response = requests.get(SuperJobAPI.api_url, headers=headers, params=params)
        data = response.content.decode()
        vacancies = json.loads(data)
        for vac in range(params['count']):
            print(vacancies['objects'][vac]['profession'])


hh_api = HeadHunterAPI()
hh_api.get_vacancies('Программист')

sj = SuperJobAPI()
sj.get_vacancies('Программист')

