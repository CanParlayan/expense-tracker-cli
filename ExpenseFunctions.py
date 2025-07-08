import csv
import json
from datetime import datetime

from Expense import Expense
import ExpenseStorage


def calculate_total_expenses():
    total = 0
    with open('expenses.json', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    expense = json.loads(line)
                    total += expense.get('amount', 0)
                except json.JSONDecodeError:
                    continue  # threshold satırı vs varsa atla
    return total


class ExpenseFunctions:
    @staticmethod
    def add_expense(description, amount, category):
        """Add a new expense."""
        date = datetime.now().strftime('%Y-%m-%d')  # Get the current date in YYYY-MM-DD format
        expense_id = ExpenseStorage.generate_id()  # Generate a unique ID for the expense
        expense = Expense(expense_id, description, amount, category, date)  # Pass the date to the Expense constructor
        ExpenseStorage.save_expense(expense, )
        print(f"Expense added successfully: {expense_id}")
        threshold = ExpenseFunctions.get_threshold()
        if threshold is not None:
            ExpenseFunctions.check_and_warn(threshold)
        else:
            pass
        return expense

    @staticmethod
    def view_expenses():
        expenses = ExpenseStorage.load_expenses()
        # Ensure each expense is parsed as a dictionary
        if isinstance(expenses, list) and all(isinstance(expense, str) for expense in expenses):
            expenses = [json.loads(expense) for expense in expenses]
        return [Expense(**expense) for expense in expenses]

    @staticmethod
    def delete_expense(expense_id):
        expense = ExpenseStorage.load_expenses()
        updated_expenses = [exp for exp in expense if exp['id'] != expense_id]
        with open('expenses.json', 'w') as file:
            for exp in updated_expenses:
                file.write(json.dumps(exp) + '\n')
        print(f"Expense with ID {expense_id} deleted successfully.")

    @staticmethod
    def summary():
        expenses = ExpenseStorage.load_expenses()
        total_amount = sum(expense['amount'] for expense in expenses)
        categories = {}
        for expense in expenses:
            category = expense['category']
            if category not in categories:
                categories[category] = 0
            categories[category] += expense['amount']
        return {
            'total_amount': total_amount,
            'categories': categories
        }

    @staticmethod
    def summary_by_month(month):
        expenses = ExpenseStorage.load_expenses()
        # Convert month to a zero-padded string
        month_str = str(month).zfill(2)
        # Filter expenses by the YYYY-MM format
        monthly_expenses = [expense for expense in expenses if expense['date'].startswith(f"2025-{month_str}")]
        total_amount = sum(expense['amount'] for expense in monthly_expenses)
        return {'total_amount': total_amount, 'month': month_str}

    @staticmethod
    def update(expense_id, new_description, new_amount, new_category):
        expenses = ExpenseStorage.load_expenses()
        updated_expenses = []
        for expense in expenses:
            if expense['id'] == expense_id:
                expense['description'] = new_description
                expense['amount'] = new_amount
                expense['category'] = new_category
            updated_expenses.append(expense)
        with open('expenses.json', 'w') as file:
            for exp in updated_expenses:
                file.write(json.dumps(exp) + '\n')

    @staticmethod
    def filter_expenses_by_category(category):
        expenses = ExpenseStorage.load_expenses()
        filtered_expenses = [expense for expense in expenses if expense['category'] == category]
        return [Expense(**expense) for expense in filtered_expenses]

    @staticmethod
    def check_budget_by_month(month, budget):
        expenses = ExpenseStorage.load_expenses()
        monthly_expenses = [expense for expense in expenses if expense['date'].startswith(month)]
        total_amount = sum(expense['amount'] for expense in monthly_expenses)
        return total_amount <= budget

    @staticmethod
    def set_threshold(threshold):
        config = ExpenseStorage.load_config()
        config['threshold'] = threshold
        ExpenseStorage.save_config(config)
        print(f"Threshold set to {threshold}")

    @staticmethod
    def get_threshold():
        config = ExpenseStorage.load_config()
        return config.get('threshold', None)

    @staticmethod
    def check_and_warn(threshold):
        if threshold is None or threshold == 0:
            return  # Exit if threshold is None or 0
        total_amount = calculate_total_expenses()  # Calculate total expenses
        if total_amount > threshold:
            print(f"Warning: Your total expenses ({total_amount}) exceed the threshold ({threshold})!")

    @staticmethod
    def export_expenses_as_csv():
        expenses = ExpenseStorage.load_expenses()
        with open('expenses.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'description', 'amount', 'category', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense)
        print("Expenses exported to expenses.csv")
