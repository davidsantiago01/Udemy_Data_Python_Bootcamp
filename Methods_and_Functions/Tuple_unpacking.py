
stock_prices = [('AAPL', 200), ('GOOG', 400), ('MSFT', 100)]
for item in stock_prices:
    print (item)
('AAPL', 200)
('GOOG', 400)
('MSFT', 100)
#-----
for ticker, price in stock_prices:
    print (price+(0.1*price)) 
220.0
440.0
110.0
#-----

work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)

employee_check(work_hours)
('Cassie', 800)
#--------

