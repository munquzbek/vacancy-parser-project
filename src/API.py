from abc import ABC, abstractmethod
from src.vacancy import Vacancy, HeadHunterVacancy, SuperJobVacancy

import requests
import json


class API(ABC):
    """
    abstract class for APIs
    """

    @abstractmethod                                         # abstract method for child classes
    def get_vacancies(self, search_query, quantity):
        pass


class HeadHunterAPI(API):
    """
    connecting with API server
    request query to get vacancies
    """
    api_url = 'https://api.hh.ru/vacancies'                  # url of api where we make a GET REQUEST

    def get_vacancies(self, search_query, quantity):         # get data with keyword and quantity of vacancies we want
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
        return vacancies

    @staticmethod
    def format_for_class(vacancies, count):     # format the data from get_vacancies dunc to Vacancy object
        if vacancies['items'][count]['salary'] is None:
            currency = 0
            min_salary = 0
            salary = 'Min salary: unknown, figure out on interview or call'
        else:
            if vacancies['items'][count]['salary']['from'] is None:
                max_salary = f"{vacancies['items'][count]['salary']['to']}"
                currency = vacancies['items'][count]['salary']['currency']
                min_salary = max_salary
                salary = f'{max_salary} {currency}'
            else:
                min_salary = vacancies['items'][count]['salary']['from']
                currency = vacancies['items'][count]['salary']['currency']
                if vacancies['items'][count]['salary']['to'] is None:
                    max_salary = ''
                    salary = f'{min_salary}{max_salary} {currency}'
                else:
                    max_salary = f"{vacancies['items'][count]['salary']['to']}"
                    salary = f'{min_salary}-{max_salary} {currency}'
        name = vacancies['items'][count]['name']
        url = vacancies['items'][count]['alternate_url']
        area = vacancies['items'][count]['area']['name']
        employer = vacancies['items'][count]['employer']['name']
        requirements = vacancies['items'][count]['snippet']['requirement']
        responsibilities = vacancies['items'][count]['snippet']['responsibility']
        return HeadHunterVacancy(name, url, salary, int(min_salary), currency, area, employer, requirements,
                                 responsibilities)


class SuperJobAPI(API):
    api_url = 'https://api.superjob.ru/2.0/vacancies/'       # url of api where we make a GET REQUEST

    def get_vacancies(self, search_query, quantity):
        max_quantity = 100
        if int(quantity) >= 101:
            quantity = max_quantity

        headers = {  # APi secret key
            'X-Api-App-Id': 'v3.h.4533236.0914b38d06ea31a5db7c2ef0784c59f472416865.'
                            'ee894d426ffb4deb94243f3f320d1bafe22df69b'
        }
        params = {   # parameters of searching 'keyword': name of vacancy, 'count': quantity of vacancies in one page
            'keyword': search_query,
            'count': quantity
        }
        response = requests.get(SuperJobAPI.api_url, headers=headers, params=params)  # Get request
        data = response.content.decode()
        vacancies = json.loads(data)
        return vacancies

    @staticmethod
    def format_for_class(vacancies, quantity):
        currency = vacancies['objects'][quantity]['currency']
        if vacancies['objects'][quantity]['payment_from'] == 0:
            min_salary = 0
            salary = 'Min salary: unknown, figure out on interview or call'
        elif vacancies['objects'][quantity]['payment_to'] == 0:
            min_salary = vacancies['objects'][quantity]['payment_from']
            salary = f'{min_salary} {currency}'
        else:
            min_salary = vacancies['objects'][quantity]['payment_from']
            max_salary = vacancies['objects'][quantity]['payment_to']
            salary = f'{min_salary}-{max_salary} {currency}'
        name = vacancies['objects'][quantity]['profession']
        url = vacancies['objects'][quantity]['link']
        area = vacancies['objects'][quantity]['town']['title']
        employer = vacancies['objects'][quantity]['firm_name']
        requirements = vacancies['objects'][quantity]['candidat']
        responsibilities = vacancies['objects'][quantity]['vacancyRichText']
        return SuperJobVacancy(name, url, salary, int(min_salary), currency, area, employer, requirements,
                               responsibilities)



