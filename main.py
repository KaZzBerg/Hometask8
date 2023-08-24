import re

home_phone = [input('Enter your home number: ')]

home_phone_regex = re.compile(r'^[+]*[38]*0+[0-9]{4}[0-9]{5}$')

for phone in home_phone:
    if home_phone_regex.match(phone) and 9 >= len(home_phone) <= 13:
        print(f'Your home number: {home_phone}')
    else:
        print('Incorrect number!')

user_phone = [input('Enter your phone number: ')]

phone_regex = re.compile(r'^[+]*[38]*0+[0-9]{2}[0-9]{7}$')

for phone1 in user_phone:
    if phone_regex.match(phone1) and 9 >= len(user_phone) <= 13:
        print(f'Your phone number: {user_phone}')
    else:
        print('Incorrect number!')

user_email = input('Enter your email: ')

if re.match(r'\w+@\w+.(\w+)', user_email) and len(user_email) <= 40:
    print(f'Your email: {user_email}')
else:
    print('Incorrect email!')

user_name = str(input('Enter your full name: ').title())
length = re.findall(r'\w+', user_name)
if re.match(r'\w+\D', user_name) and len(length) == 3 and 2 <= len(user_name) <= 20:
    print(f'Your full name: {user_name}')
else:
    print('Incorrect full name')
