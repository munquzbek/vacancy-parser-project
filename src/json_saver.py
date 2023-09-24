from abc import ABC, abstractmethod
import json


class Saver(ABC):
    """abstract class for API"""
    @abstractmethod
    def __init__(self):
        pass


class JSONSaver(ABC):
    """child class of abstract class Saver"""
    @staticmethod
    def save_to_json(datas):                   # function for creating a list of dictionaries in json format
        count = 1                              # for further use
        dict_datas = []
        for data in datas:
            dict_json = {
                'id': count,
                'name': data.name,
                'salary': data.salary,
                'min_salary': data.min_salary,
                'currency': data.currency,
                'url': data.url,
                'area': data.area,
                'employer': data.employer,
                'requirement': data.requirements,
                'responsibility': data.responsibilities
            }
            count += 1
            dict_datas.append(dict_json)  # add dict to created list 'dict_datas'
        return dict_datas

    @staticmethod
    def save_to_file(data):                                      # function for saving the list of dicts in new file
        with open('src/json_data.json', 'a') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def get_vacancies_by_salary(min_salary):                     # get vacancies by min salary
        with open('src/json_data.json', 'r') as file:            # open&read file
            data = json.load(file)                               # from json file to var
            collect_vac_by_salary = []                           # where we will append found vacancies
            for d in data:
                if d['min_salary'] >= min_salary:                # comparison with min salary
                    collect_vac_by_salary.append(f"ID:{d['id']}Salary: {d['salary']}, Profession:{d['name']}")
                    continue
                elif not d['min_salary']:
                    continue
            return collect_vac_by_salary

    @staticmethod
    def delete_vacancy_by_id(id_name):                           # deleting vacancy by id
        with open('src/json_data.json', 'r') as file:
            data = json.load(file)
            for d in data:
                if d['id'] == id_name:
                    del d
                    continue
                print(d['id'])

