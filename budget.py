
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('budget')
c = conn.cursor()


def budget():
  

    c.execute('''CREATE TABLE IF NOT EXISTS budget (category text, amount real, date text)''')
    insert_statement = "INSERT INTO budget VALUES (?,?,?)"
    values = (str(input('insert expense')),input('insert amount in USD'),str(input('insert date')))
    c.execute(insert_statement,values)
    c.execute("SELECT date, sum(amount) FROM budget GROUP BY date")
    expenses = c.fetchall()
    dates, amounts = zip(*expenses)
    total_expenses = sum(expense[1] for expense in expenses)
    print(total_expenses)
    plt.plot(dates, amounts)
    plt.xlabel('Date')
    plt.ylabel('Expenses')
    plt.title('Expenses over Time')
    plt.xticks(rotation=270)
    plt.show()
    conn.commit()
