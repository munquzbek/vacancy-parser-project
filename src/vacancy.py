from abc import ABC


class Vacancy(ABC):
    """
    Class for creating objects of vacancy
    """

    def __init__(self, name, url, salary, min_salary, currency, area, employer, requirements, responsibilities):
        self.name = name
        self.url = url
        self.salary = salary
        self.min_salary = min_salary
        self.currency = currency
        self.area = area
        self.employer = employer
        self.requirements = requirements
        self.responsibilities = responsibilities


class HeadHunterVacancy(Vacancy):
    def __init__(self, name, url, salary, min_salary, currency, area, employer, requirements, responsibilities):
        super().__init__(name, url, salary, min_salary, currency, area, employer, requirements, responsibilities)

    def __str__(self):
        return f'HH|Vacancy:{self.name}, Salary: {self.salary}, City: {self.area}, Company name: ' \
               f'{self.employer}'


class SuperJobVacancy(Vacancy):
    def __init__(self, name, url, salary, min_salary, currency, area, employer, requirements, responsibilities):
        super().__init__(name, url, salary, min_salary, currency, area, employer, requirements, responsibilities)

    def __str__(self):
        return f'SJ|Vacancy:{self.name}, Salary: {self.salary} {self.currency}, City: {self.area}, Company name: ' \
               f'{self.employer}'

