import json
import os


def get_current_date():
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d')


def save_expense(expense):
    import json
    with open('expenses.json', 'a') as file:
        file.write(json.dumps(expense.to_dict()) + '\n')


def load_expenses():
    if not os.path.exists('expenses.json'):
        return []

    with open('expenses.json', 'r') as file:
        lines = file.readlines()

    expenses = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                expenses.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Skipping invalid line: {line} -- {e}")
    return expenses


def load_config():
    try:
        with open('config.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_config(config):
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)


def generate_id():
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
