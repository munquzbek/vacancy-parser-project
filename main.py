from src.API import HeadHunterAPI,  SuperJobAPI
from src.json_saver import JSONSaver


# json_saver = JSONSaver()
# json_saver.delete_vacancy_by_id(4)



# json_saver = JSONSaver()
# print(json_saver.get_vacancies_by_salary(50001))

# sj_api = SuperJobAPI()
# sj_vac = sj_api.get_vacancies(keyword, quantity)
# data = []
# for q in range(quantity):
#     vacancies = sj_api.format_for_class(sj_vac, q)
#     data.append(vacancies)
# print(data)
# json_saver = JSONSaver()
# collected = json_saver.save_to_json(data)
# print(collected)
# json_saver.save_to_file(collected)

# hh_api = HeadHunterAPI()
# hh_vac = hh_api.get_vacancies(keyword, quantity)
# data = []
# for q in range(quantity):
#     vacancies = hh_api.format_for_class(hh_vac, q)
#     data.append(vacancies)
#
# print(data)
# json_saver = JSONSaver()
# collected = json_saver.save_to_json(data)
# print(collected)
# json_saver.save_to_file(collected)

# while True:
#     print('Welcome to my vacancy parser project')
#
#     keyword = input('Enter keyword of vacancy what you are looking for:\n')
#     quantity = input('Enter quantity of vacancy that will represented to you\n')
#
#
#     def check_is_digit(integer):
#         while True:
#             if integer.isdigit():
#                 integer = int(integer)
#                 return integer
#             else:
#                 integer = input('There is unknown symbol, try again:\n')
#
#
#     quantity = check_is_digit(quantity)
#
#     hh_api = HeadHunterAPI()
#     hh_vacancies = hh_api.get_vacancies(keyword, quantity)
#
#     sj_api = SuperJobAPI()
#     sj_vacancies = sj_api.get_vacancies(keyword, quantity)
#
