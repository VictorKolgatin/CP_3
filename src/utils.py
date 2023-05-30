import json
import os.path
from operator import itemgetter
from datetime import datetime


def load_file(path):
    """
    Загружает список банковских операций
    """

    if not os.path.exists(path):
        return None

    with open(path, 'r', encoding='utf-8') as json_file:
        file = json.load(json_file)
    return file


def executed_last_operations(file, last=None, state='EXECUTED'):
    """
    Функция обрабатывает список, берет последние 5 операций
    """
    executed_list = []

    for i in file:
        for kay, value in i.items():
            if value == state:
                executed_list.append(i)
                break

    sorted_list = sorted(executed_list, key=itemgetter('date'), reverse=True)
    last_operations = sorted_list[:last]

    return last_operations


def format_operation(data):
    """
    Преобразует данные в нужный формат
    """
    formatted_list = []
    for i in data:
        date = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        description = i['description']
        operations_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        if i.get('to') is None:
            to_info, to_bill = "Снятие наличных", ""
        else:
            recipient = i['to'].split()
            to_bill = recipient.pop(-1)
            to_bill = f"**{to_bill[-4:]}"
            to_info = " ".join(recipient)

        if i.get('from') is None:
            from_info, from_bill = "Пополнение вклада", ""
        else:
            sender = i['from'].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)

        formatted_list.append(f"""
        {date} - {description}
        {from_info} {from_bill} -> {to_info} {to_bill}
        {operations_amount}""")


    return formatted_list
