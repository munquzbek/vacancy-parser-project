from src.API import HeadHunterAPI, SuperJobAPI
from src.json_saver import JSONSaver

import requests
import json


def get_city_name_for_hh(city_name, country_name):  # get id of city for using it to search
    response_area = requests.get('https://api.hh.ru/areas')
    data_area = response_area.content.decode()
    areas = json.loads(data_area)
    for area in areas:
        if area['name'] == country_name:
            for region in area['areas']:
                if region['name'] == city_name:
                    return region['id']


def check_is_digit(integer):
    while True:
        if integer.isdigit():
            integer = int(integer)
            return integer
        else:
            integer = input('There is unknown symbol, try again:\n')


def user_interaction():
    while True:
        print('Welcome to my vacancy parser project')

        keyword = input('Enter keyword of vacancy what you are looking for:\n')
        quantity = input('Enter quantity of vacancy that will represented to you:\n')
        country = input('Enter country: \n')
        city = input('Enter city: \n')

        id_city_for_hh = get_city_name_for_hh(city, country)
        quantity = check_is_digit(quantity)

        while True:
            platform = input('Search in "HeadHunter" or "SuperJob"? (write "HH" or "SJ"):\n')
            data = []  # var for collecting data vacancies
            if platform == 'HH':
                hh_api = HeadHunterAPI()
                while True:
                    try:
                        hh_vac = hh_api.get_vacancies(keyword, quantity, id_city_for_hh)
                        for q in range(quantity):
                            vacancies = hh_api.format_for_class(hh_vac, q)
                            data.append(vacancies)
                            print(vacancies)
                        break
                    except IndexError:
                        break
                break
            elif platform == 'SJ':
                sj_api = SuperJobAPI()
                while True:
                    try:
                        sj_vac = sj_api.get_vacancies(keyword, quantity, city)
                        for q in range(quantity):
                            vacancies = sj_api.format_for_class(sj_vac, q)
                            data.append(vacancies)
                            print(vacancies)
                        break
                    except IndexError:
                        break
                break
            else:
                print('Try again, You can do it)')
                continue

        if not data:
            print('No such Vacancies(')
            continue

        while True:
            agreement = input('Do you want to save these vacancies for further filter?(Yes or No):\n')
            if agreement == 'Yes':
                json_saver = JSONSaver()
                collected = json_saver.save_to_json(data)
                json_saver.save_to_file(collected)

                filter_by_salary_or_keyword = input('Information saved, do you want to filter by salary or keyword?\n'
                                                    'Write minimum salary(ex:10000) or keyword(ex:Postgres):\n')
                if filter_by_salary_or_keyword.isdigit():
                    data = json_saver.get_vacancies_by_salary(filter_by_salary_or_keyword)
                    if not data:
                        print('No vacancies by this keyword(')
                        break
                    else:
                        get_url_id = input('Choose and write ID of vacancy you like to get url '
                                           'and requirements for further application:\n')
                        get_url_id = check_is_digit(get_url_id)
                        json_saver.get_url_of_vac(get_url_id)
                        break
                else:
                    data = json_saver.get_vacancies_by_keyword(filter_by_salary_or_keyword)
                    if not data:
                        print('No vacancies by this keyword(')
                        break
                    else:
                        get_url_id = input('Choose and write ID of vacancy you like to get url '
                                           'and requirements for further application:\n')
                        get_url_id = check_is_digit(get_url_id)
                        json_saver.get_url_of_vac(get_url_id)
                        break
            elif agreement == 'No':
                break
            else:
                print('I did not understand, write "Yes" or "No"')
                continue
        start_or_stop = input("That's it, do you want to Start from beginning or Leave?('Start' or anything else to"
                              "Leave)\n")
        if start_or_stop == 'Start':
            continue
        else:
            print('Thank you, Bye>')
            break


if __name__ == "__main__":
    user_interaction()
