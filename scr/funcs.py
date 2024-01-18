import os
import json
from datetime import datetime


def open_file():
    """функция открытия файла
    operation.json"""
    ROOT_DIR = os.path.dirname(__file__)
    OPERATION = os.path.join(ROOT_DIR, "operations.json")
    with open(OPERATION, encoding="UTF8") as file:
        file = json.load(file)
    return file


# print(type(open_file(operations.json)))
def sort_date(data):
    new_data = []
    for item in data:
        if item == {}:
            continue
        elif item['state'] == 'EXECUTED':
            new_data.append(item)

    sorted_date = sorted(new_data, key=lambda x: x['date'], reverse=True)
    five_transactions = sorted_date[:5]

    return five_transactions


def format_date(data):
    for item in data:
        item['date'] = datetime.fromisoformat(item['date']).strftime('%d.%m.%Y')
    return data


def hide_accounts_data(data):
    # new_data = []
    for item in data:
        item['to'] = f"{item['to'][:4]} **{item['to'][-4:]}"

        if item.get('from') is None:
            item['from'] = ''
        else:
            if item['from'][0] == 'С':
                item['from'] = f"{item['from'][:4]} **{item['from'][-4:]}"
            else:
                item['from'] = '{} {}** **** {}'.format(item['from'][:-12], item['from'][-10:-8], item['from'][-4:])
            # new_data.append(item['from'])
    return data


def bill_output(final_data):
    result = []
    for item in final_data:
        if item.get('from') is None:
            continue
        date = item['date']
        from_ = item['from']
        description = item['description']
        to = item['to']
        amount = item['operationAmount']['amount']
        currency = item['operationAmount']['currency']['name']
        result.append(f"{date} {description}\n{from_} -> {to}\n{amount} {currency}\n")

    return result
