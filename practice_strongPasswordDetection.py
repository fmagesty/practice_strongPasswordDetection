# Function that uses regular expressions to make sure the password string passed is strong
# Strong password must be: 8 characters long, contains both uppercase and lowercase characters and has at least one digit.
# Test the string against multiple regex patterns to validate its strenght
# strong  password to test: p455w0rdB3mF0rt3
# weak passwords to test: p455wordfrac0 , passwordfraco, 12345


import re

passwordRegex = re.compile(r'^.*(?=.{8,10})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9]+$')
password1 = passwordRegex.search('passwordfraco')

if password1 == None:
    print('Password not found. Password must contain at least 8 letters, lowercase and uppercase characters and at least one digit.')
if password1 != None:
    print(password1.group())
