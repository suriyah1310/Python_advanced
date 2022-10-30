try:
    customer_age = int(input('Enter Age: '))
    no_of_years = 1990/customer_age
    print(customer_age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid input, provide number value only')