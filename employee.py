from datetime import datetime
import random
try:
    from faker import Faker
    _faker = Faker()
except ImportError:
    _faker = None

class Employee:
    def __init__(self, full_name, birth_date, gender):
        self.full_name = full_name
        self.birth_date = birth_date  # Expected format: 'YYYY-MM-DD'
        self.gender = gender

    def save_to_db(self, conn):
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO employees (name, birth_date, gender) VALUES (?, ?, ?)',
            (self.full_name, self.birth_date, self.gender)
        )
        conn.commit()

    def calculate_age(self):
        birth = datetime.strptime(self.birth_date, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age

    @staticmethod
    def generate_random_employee():
        if _faker:
            gender = random.choice(['Male', 'Female'])
            if gender == 'Male':
                full_name = _faker.name_male()
            else:
                full_name = _faker.name_female()
            birth_date = _faker.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')
        else:
            gender = random.choice(['Male', 'Female'])
            first = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1)) + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
            last = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1)) + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
            full_name = f"{first} {last}"
            year = random.randint(1960, 2005)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            birth_date = f"{year:04d}-{month:02d}-{day:02d}"
        return Employee(full_name, birth_date, gender)

    @staticmethod
    def generate_multiple_employees(n):
        employees = []
        genders = ['Male', 'Female'] * (n // 2) + (['Male'] if n % 2 else [])
        random.shuffle(genders)
        for gender in genders:
            if _faker:
                if gender == 'Male':
                    full_name = _faker.name_male()
                else:
                    full_name = _faker.name_female()
                birth_date = _faker.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')
            else:
                first = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1)) + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
                last = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1)) + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
                full_name = f"{first} {last}"
                year = random.randint(1960, 2005)
                month = random.randint(1, 12)
                day = random.randint(1, 28)
                birth_date = f"{year:04d}-{month:02d}-{day:02d}"
            employees.append(Employee(full_name, birth_date, gender))
        return employees
