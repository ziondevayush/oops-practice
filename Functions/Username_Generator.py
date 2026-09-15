def generate_username(first_name,last_name, year):
    first = first_name[0]
    short_year = year[-2:]

    username = f'{first}{last_name}{short_year}'.lower()
    return username
first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")
year = input("Born Year: ")
result = generate_username(first_name,last_name,year)
print(result)