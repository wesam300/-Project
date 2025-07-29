import argparse
import sqlite3
import random
import string
import time
from employee import Employee
from db_manager import create_employee_table, insert_employees_batch, create_indexes

DB_FILE = 'myapp.db'

def random_name(prefix=None):
    first = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=6))
    if prefix:
        last = prefix + ''.join(random.choices(string.ascii_lowercase, k=6))
    else:
        last = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"{first} {last}"

def random_birth_date():
    year = random.randint(1960, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"

def mode_1(conn):
    create_employee_table(conn)
    print("Employee table created.")

def mode_2(conn, args):
    emp = Employee(args.full_name, args.birth_date, args.gender)
    emp.save_to_db(conn)
    print(f"Employee {emp.full_name} saved.")

def mode_3(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT full_name, birth_date, gender FROM employees ORDER BY full_name')
    rows = cursor.fetchall()
    for row in rows:
        print(f"Name: {row[0]}, Birth Date: {row[1]}, Gender: {row[2]}")
    print(f"Total unique employees: {len(rows)}")

def mode_4(conn):
    print("Generating 1,000,000 random employees and 100 'F' last name males...")
    employees = [Employee(random_name(), random_birth_date(), random.choice(['Male', 'Female'])) for _ in range(1_000_000)]
    employees += [Employee(random_name(prefix='F'), random_birth_date(), 'Male') for _ in range(100)]
    insert_employees_batch(conn, employees)
    print("Batch insert complete.")

def mode_5(conn):
    print("Querying for Male employees with last name starting with 'F'...")
    start = time.time()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT full_name, birth_date, gender FROM employees
        WHERE gender = 'Male' AND full_name LIKE '% F%'
        AND substr(full_name, instr(full_name, ' ')+2, 1) = 'F'
    """)
    rows = cursor.fetchall()
    elapsed = time.time() - start
    print(f"Found {len(rows)} employees. Query took {elapsed:.4f} seconds.")
    return elapsed

def mode_6(conn):
    print("Adding indexes on full_name and gender...")
    cursor = conn.cursor()
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_full_name ON employees(full_name)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_gender ON employees(gender)')
    conn.commit()
    print("Indexes created. Re-running query...")
    elapsed = mode_5(conn)
    print(f"Query with indexes took {elapsed:.4f} seconds.")

def mode_7(conn):
    create_indexes(conn)
    print("Indexes on full_name and gender have been created.")

def main():
    parser = argparse.ArgumentParser(description='myApp Advanced Console Application')
    parser.add_argument('--mode', type=int, choices=range(1, 8), required=True, help='Operation mode (1-7)')
    parser.add_argument('--full_name', type=str, help='Full name for mode 2')
    parser.add_argument('--birth_date', type=str, help='Birth date YYYY-MM-DD for mode 2')
    parser.add_argument('--gender', type=str, choices=['Male', 'Female'], help='Gender for mode 2')
    args = parser.parse_args()

    conn = sqlite3.connect(DB_FILE)

    if args.mode == 1:
        mode_1(conn)
    elif args.mode == 2:
        if not (args.full_name and args.birth_date and args.gender):
            print('Mode 2 requires --full_name, --birth_date, and --gender')
        else:
            mode_2(conn, args)
    elif args.mode == 3:
        mode_3(conn)
    elif args.mode == 4:
        mode_4(conn)
    elif args.mode == 5:
        mode_5(conn)
    elif args.mode == 6:
        mode_6(conn)
    elif args.mode == 7:
        mode_7(conn)
    else:
        print('Invalid mode')

    conn.close()

if __name__ == '__main__':
    main() 