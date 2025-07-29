import sqlite3
import time

class DBManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self._create_employee_table()

    def _create_employee_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT,
                salary REAL
            )
        ''')
        self.conn.commit()

    def add_employee(self, name, position, salary):
        pass

    def list_employees(self):
        pass

    def update_employee(self, emp_id, name, position, salary):
        pass

    def delete_employee(self, emp_id):
        pass

    def search_employee(self, name):
        pass

    def custom_operation(self):
        pass

    def __del__(self):
        self.conn.close()


def create_employee_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            gender TEXT NOT NULL
        )
    ''')
    conn.commit()


def insert_employees_batch(conn, employee_list):
    cursor = conn.cursor()
    data = [(emp.full_name, emp.birth_date, emp.gender) for emp in employee_list]
    cursor.executemany(
        'INSERT INTO employees (full_name, birth_date, gender) VALUES (?, ?, ?)',
        data
    )
    conn.commit()


def query_male_employees_with_f(conn):
    start = time.time()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, full_name, birth_date, gender FROM employees
        WHERE gender = 'Male' AND full_name LIKE 'F%'
    """)
    rows = cursor.fetchall()
    elapsed = time.time() - start
    return rows, elapsed 


def create_indexes(conn):
    cursor = conn.cursor()
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_full_name ON employees(full_name)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_gender ON employees(gender)')
    conn.commit() 