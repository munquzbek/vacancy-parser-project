

class Vacancy:
    """
    Class for creating objects of vacancy
    """
    def __init__(self, name, url, salary, area, employer, requirement, responsibilities): # initialization
        self.name = name
        self.url = url
        self.salary = salary
        self.area = area
        self.employer = employer
        self.requirement = requirement
        self.responsibilities = responsibilities

    def print_info(self):  # function for representing available vacancies
        print(f'Profession: {self.name}, Salary: {self.salary}, City: {self.area}, Company name: {self.employer}')
