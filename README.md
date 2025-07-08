---

````markdown
# 💸 [Expense Tracker CLI](https://roadmap.sh/projects/expense-tracker)

A simple yet powerful command-line application to help you track your daily expenses. You can **add**, **view**, **update**, **delete**, **filter**, and **summarize** your expenses — all from your terminal.

## 📦 Features

- ✅ Add new expenses with description, amount, and category
- 🗑️ Delete expenses by ID
- 📝 Update existing expenses
- 📋 List all expenses
- 📊 Monthly and overall expense summary
- 📁 Export all expenses as CSV
- 🔎 Filter expenses by category
- 💰 Set a spending threshold and get warned when it's exceeded
- 📅 Check if you're within budget for a specific month

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/CanParlayan/expense-tracker-cli.git
cd expense-tracker-cli
````

### 2. Run the Application

Make sure you have Python 3 installed.

```bash
python expense-tracker.py --help
```

---

## 📚 Example Usage

### ➕ Add an Expense

```bash
python expense-tracker.py add --description "Lunch" --amount 12.5 --category Food
```

### 📃 List All Expenses

```bash
python expense-tracker.py list
```

Output:

```
  ID    Description, Amount, Category, Date
  A1B2C Lunch, 12.5, Food, 2025-07-08
```

### 🧾 View Summary

```bash
python expense-tracker.py summary
```

Output:

```
Total Amount: 45.0
```

### 🗓️ Monthly Summary

```bash
python expense-tracker.py summary --month July
```

Output:

```
Total Amount for July: 30.0
```

### 🧼 Delete an Expense

```bash
python expense-tracker.py delete --id A1B2C
```

### 🛠️ Update an Expense

```bash
python expense-tracker.py update --id A1B2C --description "Dinner" --amount 15 --category Food
```

### 📂 Export as CSV

```bash
python expense-tracker.py export
```

This will create a `expenses.csv` file in your current directory.

### 📁 Filter by Category

```bash
python expense-tracker.py filter-category --category Food
```

### 📉 Check Monthly Budget

```bash
python expense-tracker.py check-budget-monthly --month 7 --budget 200
```

Output:

```
Expenses are within the budget for month 7.
```

### 🚨 Set Threshold for Spending Warning

```bash
python expense-tracker.py set-threshold --threshold 100
```

---

## 🗂️ File Structure

```
├── expense-tracker.py         # Main CLI handler
├── ExpenseFunctions.py        # Core logic for managing expenses
├── Expense.py                 # Expense class
├── ExpenseStorage.py          # File I/O for storing and reading data
├── expenses.json              # Data file (auto-generated)
├── config.json                # Threshold config (auto-generated)
└── expenses.csv               # Exported CSV (generated on command)
```

---

## 💡 Tips

* You can run `--help` with any subcommand to see its arguments:

  ```bash
  python expense-tracker.py add --help
  ```

* Make regular exports (`export`) to back up your data.

---
