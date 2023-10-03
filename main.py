import json
from datetime import datetime


def open_file(inf_file, result_file):
    """
    Принимает файл с личной инфой и файл с временем
    выводит словари с персональной информацией и 2 списка (номер, время) с сортировкой по возрастанию времени
    """

    with open('competitors2.json', 'r', encoding='utf-8-sig') as file_personal_info:
        personal_info = json.load(file_personal_info)

    with open('results_RUN.txt', 'r', encoding='utf-8-sig') as file_result:
        result_dict = dict()
        for line in file_result:
            data_line = line.split()
            number = data_line[0]
            temp_time = datetime.strptime(data_line[2].split()[0], '%H:%M:%S,%f')
            if number in result_dict:
                start_sec = result_dict[number]['start']
                result_dict[number] = temp_time - start_sec
            else:
                result_dict[number] = {data_line[1]: temp_time}
        result = dict(sorted(result_dict.items(), key=lambda x: x[1]))
        list_win_nums = list(result.keys())
        list_win_time = list(result.values())

    return personal_info, list_win_nums, list_win_time


def result_dict_compile_and_print(personal_info, list_win_nums, list_win_time, fin_num=4):
    """
    Функция принимает обработанную инфу с open_file
    и формирует словарь (а так же печатает результат)
    fin_num - сколько нужно вывести позиций (по тз: 4)
    """
    final_results_dict = dict()
    for i in range(fin_num):
        final_results_dict[i+1] = {'Нагрудный номер': list_win_nums[i], 'Имя': personal_info[list_win_nums[i]]["Surname"],
                                   'Фамилия': personal_info[list_win_nums[i]]["Name"], 'Результат': list_win_time[i]}
        print('Занятое место: {pos} {tab} Нагрудный номер: {num} {tab} '
              'Имя: {sn} {tab} Фамилия: {name} {tab} Результат:{res}'
              .format(pos=i+1, tab='\t' * 2, num=list_win_nums[i], sn=personal_info[list_win_nums[i]]["Surname"],
                      name=personal_info[list_win_nums[i]]["Name"], res=list_win_time[i]))
    return final_results_dict


def save_json(final_results_dict):
    """ Cохранение в json файл """
    with open('final_results.json', 'w', encoding='utf-8') as file_final_result:
        json.dump(final_results_dict, file_final_result, ensure_ascii=False, default=str, indent=4)


if __name__ == "__main__":
    pers_info, win_nums, win_time = open_file('competitors2.json', 'results_RUN.txt')
    fres_dict = result_dict_compile_and_print(pers_info, win_nums, win_time, 10)
    save_json(fres_dict)
