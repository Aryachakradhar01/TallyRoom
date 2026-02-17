import db

def add_expense(amount, category, date, note):
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
        (amount, category, date, note)
    )

    conn.commit()
    conn.close()


def get_all_expenses():
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()
    return rows
