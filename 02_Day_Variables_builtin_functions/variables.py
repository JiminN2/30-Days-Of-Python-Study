
# Variables in Python

first_name = 'Elicia'
last_name = 'Park'
country = 'Finland'
city = 'Helsinki'
age = 25
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Elicia',
    'lastname': 'Park',
    'country': 'Finland',
    'city': 'Helsinki'
}
favourite_food = ('Pasta', 'Salad', 'Pizza')  # Tuple
unfavourite_food = {'Hamburger', 'Hamburger', 'Fries'}  # Set

# Printing the values stored in the variables
print(favourite_food)
print(unfavourite_food)
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
print('first name: ', first_name, 'last name: ', last_name, 'country: ', country)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

print(first_name, last_name, country, age, is_married)