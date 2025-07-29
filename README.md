# myApp Console Application

A Python console application that manages employees using SQLite, supporting multiple operation modes via command-line arguments.

---

## Summary of Modes

1. **Create Employee Table:**
   - Creates the 'employees' table in the SQLite database with appropriate fields and types.

2. **Add One Employee:**
   - Adds a single employee to the database. Requires `--full_name`, `--birth_date`, and `--gender` as arguments.

3. **List Unique Employees:**
   - Lists all unique employees in the database, sorted by full name.

4. **Generate and Insert Random Employees:**
   - Generates 1,000,000 random employees and 100 additional male employees with last names starting with 'F', then inserts them in batch.

5. **Query for Male Employees with Last Name Starting with 'F':**
   - Runs a query to find all male employees whose last name starts with 'F' and measures the execution time.

6. **Add Indexes and Compare Query Performance:**
   - Adds indexes on `full_name` and `gender` columns, re-runs the query from mode 5, and compares the execution time before and after indexing.

7. **Add Indexes Only:**
   - Adds indexes on `full_name` and `gender` columns without running the query.

---

## Project Structure

- `app.py`: Main entry point, handles argument parsing and mode selection
- `employee.py`: Employee class with business logic and random generation
- `db_manager.py`: Handles SQLite database operations
- `requirements.txt`: Dependencies (all standard library, Faker optional)

---

## How to Run the App

Open a terminal in the project directory and use the following commands:

```sh
# 1. Create the employees table
python app.py --mode 1

# 2. Add a single employee
python app.py --mode 2 --full_name "Wesam shamsan" --birth_date 2001-02-18 --gender Male

# 3. List all unique employees
python app.py --mode 3

# 4. Generate and insert 1,000,100 random employees
python app.py --mode 4

# 5. Query for male employees with last name starting with 'F' and measure time
python app.py --mode 5

# 6. Add indexes, re-run mode 5, and compare speed
python app.py --mode 6

# 7. Add indexes only
python app.py --mode 7
```

---

## Performance Measurements (Example)

After generating and inserting the data (mode 4), you can measure query performance:

- **Mode 5 (before indexing):**
  - `Found 100 employees. Query took 2.35 seconds.`

- **Mode 6 (after indexing):**
  - `Indexes created. Re-running query...`
  - `Found 100 employees. Query with indexes took 0.04 seconds.`

*Note: Actual times may vary depending on your hardware and system load.*

---

## Explanation of Optimization in Mode 6

Mode 6 improves query performance by creating indexes on the `full_name` and `gender` columns in the employees table. Indexes allow the database to quickly locate rows matching the query conditions, especially when filtering by gender and searching for last names starting with a specific letter. This reduces the time complexity of the query, resulting in much faster execution compared to a full table scan.

---

## Notes
- All dependencies are from the Python standard library, except Faker (optional for better random names).
- The database file `myapp.db` will be created in the current directory. 