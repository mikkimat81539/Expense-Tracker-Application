"""Project: "Expense Tracker Application"
Goal:
Build a command-line expense tracker where users can log their daily expenses, categorize them,
and get a summary of their spending. The app will allow users to:

Add expenses with categories (e.g., Food, Entertainment, Bills).
View a summary of total expenses per category.
See a daily total, and filter by date.
Optionally, store the data in a JSON or CSV file for persistence.

Steps to build:
Create the Expense structure: Each expense can have:
    Amount
    Category (e.g., Food, Transportation, Entertainment)
    Date (for filtering by day, week, or month)

Define functions:
    Add Expense: Prompt the user to input the expense amount, category, and date.
    View Expenses: Display the expenses in a readable format, with options to filter by category or date.
    Generate Report: Summarize the total spending by category and date range.
    Save and Load Data: Use JSON or CSV to persist data so it can be loaded when the program starts."""

# When you call .get("1.0", "end-1c"), you’re saying: "Give me all the text starting from the very beginning up to,
# but not including, the extra newline at the end."

#Before we can update the label, we need to retrieve its current text.
# The .cget("text") method gets the current text value of the label.
# cget stands for "config get" — it's a way to get the current value of a configuration setting (in this case, the text of the label).

import tkinter as tk

def window():
    screen = tk.Tk()
    screen.title("Expense Tracker")
    screen.geometry("700x600")
    screen.configure(background="#012438",
                     cursor="arrow")
    return screen


def title(screen):
    heading = tk.Label(screen, text="Expense Tracker")
    heading.configure(font=("Sans Serif", 30),
                   fg="White",
                   background="#012438")

    return heading

def insert(screen):
    items = tk.Label(screen, text="Items")
    items.configure(font=("Sans Serif", 20),
                    fg="White",
                    background="#012438")


    input1 = tk.Text(screen, height=1, width=15)
    input1.configure(font=("Sans Serif", 15),
                     fg="black",
                     background="white",
                     highlightcolor="#012438",
                     highlightbackground="#012438",
                     cursor="xterm")

    quantity = tk.Label(screen, text="Quantity")
    quantity.configure(font=("Sans Serif", 20),
                    fg="White",
                    background="#012438")

    input2 = tk.Text(screen, height=1, width=15)
    input2.configure(font=("Sans Serif", 15),
                     fg="black",
                     background="white",
                     highlightcolor="#012438",
                     highlightbackground="#012438",
                     cursor="xterm")

    cost = tk.Label(screen, text="Cost per Unit")
    cost.configure(font=("Sans Serif", 20),
                    fg="White",
                    background="#012438")

    input3 = tk.Text(screen, height=1, width=15)
    input3.configure(font=("Sans Serif", 15),
                     fg="black",
                     background="white",
                     highlightcolor="#012438",
                     highlightbackground="#012438",
                     cursor="xterm")

    return items, input1, quantity, input2, cost, input3

def btns(screen):
    frame1 = tk.Frame(screen, bg="#012438")

    adding = tk.Button(frame1,
                       text="Add Items",
                       font=("Sans Serif", 15),
                       width=7,
                       height=2,
                       cursor="hand2",
                       highlightbackground="#012438")

    clear = tk.Button(frame1,
                       text="Clear",
                       font=("Sans Serif", 15),
                       width=7,
                       height=2,
                       cursor="hand2",
                      highlightbackground="#012438",)

    return frame1, adding, clear


def lists(screen):
    expense = tk.Label(screen, text="Expenses")
    expense.configure(background="#012438",
                      fg="white",
                      font=("Sans Serif", 20))

    item = tk.Label(screen, text="Item\t\tQuantity\t\tUnit Cost\t\tTotal")

    item.configure(font=("Sans Serif", 15),
                   fg="white",
                   background="#012438")

    return expense, item

def add_expense(input1, input2, input3, expenses, item_label):

    items = input1.get("1.0", "end-1c").strip()  # Get item name

    quantity = input2.get("1.0", "end-1c").strip()  # Get quantity

    cost = input3.get("1.0", "end-1c").strip()  # Get cost

    # Errors
    if not items or not quantity or not cost:
        print("Please fill all fields")
        return

    try:
        quantity = int(quantity)  # Convert quantity to integer
        cost = float(cost)  # Convert cost to float

    except ValueError:
        print("Invalid number format")
        return

    total = quantity * cost
    expenses.append((items, quantity, cost, total))

    # Update the displayed list of expenses
    update_expenses(item_label, expenses)

def clear_inputs(input1, input2, input3):
    # Clear input fields after adding
    input1.delete("1.0", "end")
    input2.delete("1.0", "end")
    input3.delete("1.0", "end")


def update_expenses(item_label, expenses):
    # Update the item_label to show the list of expenses
    item_label.config(text="Item\t\tQuantity\t\tUnit Cost\t\tTotal")  # Reset header

    for expense in expenses:
        item_label.config(text=item_label.cget("text") + f"\n{expense[0]}\t\t{expense[1]}\t\t{expense[2]}\t\t{expense[3]:.2f}")


def running():
    screen = window()

    heading = title(screen)
    heading.pack(pady=10)

    items, input1, quantity, input2, cost, input3 = insert(screen)

    items.pack(pady=5)
    input1.pack(pady=5)

    quantity.pack(pady=(15, 5))
    input2.pack(pady=5)

    cost.pack(pady=(15, 5))
    input3.pack(pady=5)

    frame1, adding, clear = btns(screen)

    frame1.pack()

    adding.pack(padx=10, pady=10, side=tk.LEFT)

    clear.pack(side=tk.RIGHT)

    expense, item = lists(screen)
    expense.pack(pady=5)

    item.pack(pady=5)

    # Initialize expenses as an empty list
    expenses = []

    adding.config(command=lambda: add_expense(input1, input2, input3, expenses, item))
    clear.config(command=lambda: clear_inputs(input1, input2, input3))

    screen.mainloop()

running()
