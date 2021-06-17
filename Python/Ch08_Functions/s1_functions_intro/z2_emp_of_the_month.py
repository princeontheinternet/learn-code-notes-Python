# Employee of the month program on the basis of work hours.

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return employee_of_month, current_max


emp_hrs_tup = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

emp_name, hrs = employee_check(emp_hrs_tup)

print(emp_name)
