[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/dVZYZI4T)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12178353&assignment_repo_type=AssignmentRepo)
# Test case Fora
### Файлы с данными:

###### competitors2.json - спортсмены с указанием нагрудного номера, имени и фамилии
###### results_RUN.txt - результаты первой попытки




Время приходит в формате «нагрудный_номер start ЧЧ:ММ:СС,дст» и «нагрудный_номер finish ЧЧ:ММ:СС,дст».





Что нужно вывести списком:

Результат

| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |
| --- | --- | --- | --- | --- |
| 1 | 132 | Иван | Иванов | 01:02,32 |
| 2 | 222 | Петр | Иванов | 01:03,00 |
| 3 | 331 | Клим | Петров | 01:04,10 |
| 4 | 2	| Андрей | Сидоров | 01:05,98 |

Так же необходимо сформировать и записать файл с названием final_results.json. (Ключи - занятые места, значениея - остальные данные)
```json
{
    "1": {
        "Нагрудный номер": "132",
        "Имя": "Иван",
        "Фамилия": "Иванов",
        "Результат": "01:02,32"
    },
    "2": {
        "Нагрудный номер": "222",
        "Имя": "Петр",
        "Фамилия": "Иванов",
        "Результат": "01:03,00"
    },
    "3": {
        "Нагрудный номер": "331",
        "Имя": "Клим",
        "Фамилия": "Петров",
        "Результат": "01:04,10"
    },
    "4": {
        "Нагрудный номер": "2",
        "Имя": "Андрей",
        "Фамилия": "Сидоров",
        "Результат": "01:05,98"
    }
}
```

Задание выполнять в этом же репозитории в ветке "dev". 
Ответ на задание присылать в пулреквест в ветку main. В реквесте указать ваши контактные данные данные.
Язык программирования Python, версия 3.9. Файл из которого происходит запуск программы должен называться main.py

Крайний срок выполнения задания суббота 23:59 по Новосибирскому времени. Если вы не успели и доступа на запись в репозиторий нет - не надо делать в своем репозитории и присылать PR, перезапросите ссылку на новый у HR.

Для решения задачи необходимо использовать только встроенные средства/модули языка программирования.
