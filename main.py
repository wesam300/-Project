import argparse
from db_manager import DBManager
from employee import Employee


def main():
    parser = argparse.ArgumentParser(description='myApp Console Application')
    parser.add_argument('--mode', type=int, choices=range(1, 7), required=True, help='Operation mode (1-6)')
    args = parser.parse_args()

    db = DBManager('myapp.db')
    emp = Employee()

    if args.mode == 1:
        print('Mode 1: Add employee')
        emp.add_employee(db)
    elif args.mode == 2:
        print('Mode 2: List employees')
        emp.list_employees(db)
    elif args.mode == 3:
        print('Mode 3: Update employee')
        emp.update_employee(db)
    elif args.mode == 4:
        print('Mode 4: Delete employee')
        emp.delete_employee(db)
    elif args.mode == 5:
        print('Mode 5: Search employee')
        emp.search_employee(db)
    elif args.mode == 6:
        print('Mode 6: Custom operation')
        emp.custom_operation(db)
    else:
        print('Invalid mode')

if __name__ == '__main__':
    main() 