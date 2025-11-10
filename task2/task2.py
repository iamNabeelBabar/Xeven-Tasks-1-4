import json

def salary_increment(salary_dictionary):
    
    employees = salary_dictionary
    
    
    
    for employee in employees:
        
        
        if employee['rating'] >= 4.5:
            
            percent_salary = employee['salary'] + employee['salary'] / 10
            employee['new_salary'] = percent_salary
            
        elif employee['rating'] >= 4.0:
            
            percent_salary = employee['salary'] + employee['salary'] / 5
            employee['new_salary'] = percent_salary
        
        else:
            employee['new_salary'] = employee['salary']
    
    return employees
    
    
    
employees = [
    {"name": "Ali", "salary": 60000, "rating": 4.7},
    {"name": "Sara", "salary": 50000, "rating": 3.2},
    {"name": "John", "salary": 70000, "rating": 4.9}
    ]
            
            
new_salary = salary_increment(salary_dictionary=employees)

jsonfilename = 'updated_salaries.json'

with open(jsonfilename, 'w') as fp:
    json.dump(new_salary, fp,indent=4)
    print(f'Successfully data saved at {jsonfilename}')
    
print(new_salary)