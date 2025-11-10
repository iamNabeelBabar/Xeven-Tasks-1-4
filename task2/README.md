# Employee Salary Adjustment System

A Python utility to automatically adjust employee salaries based on their performance ratings.

---

## Task Overview

An HR department wants to automatically adjust employee salaries based on performance ratings. This tool processes employee data, applies salary adjustments according to rating thresholds, and generates a report showing old and new salaries.

---

## Features

- Processes employee data containing name, salary, and performance rating
- Automatically calculates salary increases based on performance:
  - 10% increase if rating ≥ 4.5
  - 5% increase if rating ≥ 4.0
  - 0% increase otherwise
- Displays old and new salaries in a clean, formatted output
- Saves updated employee data to `updated_salaries.json`

---

## Requirements

- Python 3.6 or above
- Only uses built-in module: `json`

---

## Usage

1. Save the script as `salary_adjuster.py`.
2. Run the script:
   ```bash
   python salary_adjuster.py
   ```
3. View the console output for salary comparisons.
4. Check `updated_salaries.json` for the updated employee data.

---

## Example Output (Console)

```
Employee Salary Adjustment Report
=====================================

Employee: Ali
Old Salary: $60,000.00
New Salary: $66,000.00
Rating: 4.7 ⭐
Increase: 10%
-------------------------------------

Employee: Sara
Old Salary: $50,000.00
New Salary: $50,000.00
Rating: 3.2 ⭐
Increase: 0%
-------------------------------------

Employee: John
Old Salary: $70,000.00
New Salary: $77,000.00
Rating: 4.9 ⭐
Increase: 10%
-------------------------------------
```

---

## Example Output (`updated_salaries.json`)

```json
[
    {
        "name": "Ali",
        "salary": 66000.0,
        "rating": 4.7
    },
    {
        "name": "Sara",
        "salary": 50000.0,
        "rating": 3.2
    },
    {
        "name": "John",
        "salary": 77000.0,
        "rating": 4.9
    }
]
```

---

## Python Solution

```python
import json

def adjust_salaries(employees, output_file='updated_salaries.json'):
    print("Employee Salary Adjustment Report")
    print("=" * 37)
    print()

    for employee in employees:
        name = employee['name']
        old_salary = employee['salary']
        rating = employee['rating']

        # Determine salary increase based on rating
        if rating >= 4.5:
            increase_percent = 10
        elif rating >= 4.0:
            increase_percent = 5
        else:
            increase_percent = 0

        # Calculate new salary
        new_salary = old_salary * (1 + increase_percent / 100)

        # Update employee salary
        employee['salary'] = new_salary

        # Print formatted output
        print(f"Employee: {name}")
        print(f"Old Salary: ${old_salary:,.2f}")
        print(f"New Salary: ${new_salary:,.2f}")
        print(f"Rating: {rating} ⭐")
        print(f"Increase: {increase_percent}%")
        print("-" * 37)
        print()

    # Save updated data to JSON file
    with open(output_file, 'w') as f:
        json.dump(employees, f, indent=4)

    print(f"✅ Updated salaries saved to {output_file}")

    return employees


# Employee data
employees = [
    {"name": "Ali", "salary": 60000, "rating": 4.7},
    {"name": "Sara", "salary": 50000, "rating": 3.2},
    {"name": "John", "salary": 70000, "rating": 4.9}
]

# Run the salary adjustment
updated_employees = adjust_salaries(employees, output_file='updated_salaries.json')
```

---

## How the Code Works

- The script iterates through each employee in the list.
- For each employee, it checks their performance rating against defined thresholds.
- It calculates the salary increase percentage: 10% for rating ≥ 4.5, 5% for rating ≥ 4.0, and 0% otherwise.
- The new salary is computed by multiplying the old salary by (1 + increase percentage).
- The employee dictionary is updated with the new salary value.
- A formatted report is printed to the console showing old salary, new salary, rating, and increase percentage.
- All updated employee data is saved to `updated_salaries.json` in a structured format.

---

## Customization

- Modify the rating thresholds and increase percentages in the conditional logic.
- Add more employee data to the `employees` list.
- Change the output filename by modifying the `output_file` parameter.
- Extend the script to read employee data from an input JSON file.
- Add additional fields like department, hire date, or bonus calculations.

---

## License

MIT License

---

For questions or contributions, please open an issue or submit a pull request.
