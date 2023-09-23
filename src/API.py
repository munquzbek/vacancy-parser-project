from abc import ABC, abstractmethod

import requests
import json

from src.vacancy import Vacancy


class API(ABC):
    """
    abstract class for APIs
    """

    def __init__(self):
        self.vacancy = Vacancy

    @abstractmethod
    def get_vacancies(self, search_query, quantity):
        pass


class HeadHunterAPI(API):
    """
    connecting with API server
    request query to get vacancies
    """
    api_url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_query, quantity):
        max_quantity = 100
        if int(quantity) >= 101:
            quantity = max_quantity

        params = {  # parameters of searching 'text': name of vacancy, 'per_page': quantity of vacancies in one page
            'text': search_query,
            'per_page': quantity
        }
        response = requests.get(url=HeadHunterAPI.api_url, params=params)  # request with parameters
        data = response.content.decode()                                   # decode from [Response 200] to str
        vacancies = json.loads(data)
        for vac in range(int(quantity)):
            if vacancies['items'][vac]['salary'] is None:
                salary = 'Min salary: unknown, figure out on interview or call'
            else:
                from_ = vacancies['items'][vac]['salary']['from']
                if vacancies['items'][vac]['salary']['to'] is None:
                    to_ = ''
                else:
                    to_ = f"-{vacancies['items'][vac]['salary']['to']}"
                currency = vacancies['items'][vac]['salary']['currency']
                salary = f'{from_}{to_} {currency}'
            name = vacancies['items'][vac]['name']
            url = vacancies['items'][vac]['alternate_url']
            area = vacancies['items'][vac]['area']['name']
            employer = vacancies['items'][vac]['employer']['name']
            requirement = vacancies['items'][vac]['snippet']['requirement']
            responsibilities = vacancies['items'][vac]['snippet']['responsibility']
            info = Vacancy(name, url, salary, area, employer, requirement, responsibilities)
            Vacancy.print_info(info)


class SuperJobAPI(API):
    api_url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, search_query, quantity):
        headers = {  # APi secret key
            'X-Api-App-Id': 'v3.h.4533236.0914b38d06ea31a5db7c2ef0784c59f472416865.'
                            'ee894d426ffb4deb94243f3f320d1bafe22df69b'
        }
        params = {   # parameters of searching 'keyword': name of vacancy, 'count': quantity of vacancies in one page
            'keyword': search_query,
            'count': quantity
        }
        response = requests.get(SuperJobAPI.api_url, headers=headers, params=params)
        data = response.content.decode()
        vacancies = json.loads(data)
        for var in range(int(quantity)):
            try:
                currency = vacancies['objects'][var]['currency']
                if vacancies['objects'][var]['payment_from'] == 0:
                    salary = 'Min salary: unknown, figure out on interview or call'
                elif vacancies['objects'][var]['payment_to'] == 0:
                    from_ = vacancies['objects'][var]['payment_from']
                    salary = f'{from_} {currency}'
                else:
                    from_ = vacancies['objects'][var]['payment_from']
                    to_ = vacancies['objects'][var]['payment_to']
                    salary = f'{from_}{to_} {currency}'
                name = vacancies['objects'][var]['profession']
                url = vacancies['objects'][var]['link']
                area = vacancies['objects'][var]['town']['title']
                employer = vacancies['objects'][var]['firm_name']
                requirement = vacancies['objects'][var]['candidat']
                responsibilities = vacancies['objects'][var]['vacancyRichText']
                info = Vacancy(name, url, salary, area, employer, requirement, responsibilities)
                Vacancy.print_info(info)
            except IndexError:
                break


# hh_api = HeadHunterAPI()
# hh_api.get_vacancies('python', 101)


# sj = SuperJobAPI()
# sj.get_vacancies('Java', 1000)

