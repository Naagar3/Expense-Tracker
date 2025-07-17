import pandas as pd
import numpy as np
import os

# File to store expenses
data_file = "expenses.csv"

# Initialize the data file if it doesn't exist
def initialize_file():
    if not os.path.exists(data_file):
        df = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])
        df.to_csv(data_file, index=False)

# Add a new expense
def add_expense(date, category, description, amount):
    new_expense = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Description": [description],
        "Amount": [amount]
    })
    df = pd.read_csv(data_file)
    df = pd.concat([df, new_expense], ignore_index=True)
    df.to_csv(data_file, index=False)
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    df = pd.read_csv(data_file)
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print(df)

# Analyze expenses
def analyze_expenses():
    df = pd.read_csv(data_file)
    if df.empty:
        print("No expenses recorded yet.")
        return

    print("\nTotal Expenses:")
    print(df["Amount"].sum())

    print("\nExpenses by Category:")
    print(df.groupby("Category")["Amount"].sum())

    print("\nMonthly Expenses:")
    df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M")
    print(df.groupby("Month")["Amount"].sum())

# Main menu
def main_menu():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Travel, Utilities): ")
            description = input("Enter description: ")
            try:
                amount = float(input("Enter amount: "))
                add_expense(date, category, description, amount)
            except ValueError:
                print("Invalid amount. Please try again.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    initialize_file()
    main_menu()
