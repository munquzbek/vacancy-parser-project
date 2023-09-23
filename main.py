from src.API import HeadHunterAPI, SuperJobAPI

print('Welcome to my vacancy parser project')

keyword = input('Enter keyword of vacancy what you are looking for:\n')
quantity = input('Enter quantity of vacancy that will represented to you\n')


def check_is_digit(integer):
    while True:
        if integer.isdigit():
            integer = int(integer)
            return integer
        else:
            integer = input('There is unknown symbol, try again:\n')


quantity = check_is_digit(quantity)

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies(keyword, quantity)

sj_api = SuperJobAPI()
sj_vacancies = sj_api.get_vacancies(keyword, quantity)

