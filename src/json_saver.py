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
    def save_to_json(datas):  # function for creating a list of dictionaries in json format
        count = 1  # for further use
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
                'requirements': data.requirements,
                'responsibility': data.responsibilities
            }
            count += 1
            dict_datas.append(dict_json)  # add dict to created list 'dict_datas'
        return dict_datas

    @staticmethod
    def save_to_file(data):  # function for saving the list of dicts in new file
        with open('src/json_data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def get_vacancies_by_salary(min_salary):  # get vacancies by min salary
        with open('src/json_data.json', 'r') as file:  # open&read file
            data = json.load(file)  # from json file to var
            collect_vac_by_salary = []  # where we will append found vacancies
            for d in data:
                if d['min_salary'] >= int(min_salary):  # comparison with min salary
                    collect_vac_by_salary.append(f"ID:{d['id']} Salary: {d['salary']}, Profession:{d['name']}")
                    continue
                elif not d['min_salary']:
                    continue
            for collect_vac in collect_vac_by_salary:
                print(collect_vac)
            return collect_vac_by_salary

    @staticmethod
    def get_vacancies_by_keyword(keyword):
        with open('src/json_data.json', 'r') as file:  # open&read
            data = json.load(file)
            collect_vac_by_keyword = []
            for d in data:
                del_dot = d['requirements'].replace('.', '')
                del_coma = del_dot.replace(',', '')
                del_slash = del_coma.replace('/', ' ')
                del_rscope = del_slash.replace(')', '')
                del_lscope = del_rscope.replace('(', '')
                del_text = del_lscope.replace('highlighttext', '')
                del_rarrow = del_text.replace('>', '')
                del_larrow = del_rarrow.replace('<', '')
                split_data = del_larrow.split(' ')
                for split in split_data:
                    if split.lower() == keyword.lower():
                        collect_vac_by_keyword.append(f"ID:{d['id']} Salary: {d['salary']}, Profession:{d['name']}\n"
                                                      f"{d['requirements']}")
                    elif split != keyword:
                        continue
            collect_vac_by_keyword = list(set(collect_vac_by_keyword))
            for collect_vac in sorted(collect_vac_by_keyword):
                print(collect_vac)
            return collect_vac_by_keyword

    @staticmethod
    def get_url_of_vac(id_name):
        with open('src/json_data.json', 'r') as file:
            data = json.load(file)
            for d in data:
                if d['id'] == id_name:
                    print(f"{d['name']}, {d['url']} \n{d['requirements']} \n{d['responsibility']}")
                elif d['id'] != id_name:
                    continue
                else:
                    print('No such ID')
