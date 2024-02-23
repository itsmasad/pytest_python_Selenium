# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using pip package manager (incuding Django) as well as custom modules

# Core Modules

# Importing date time module
import datetime
today = datetime.date.today()
print(today)

# Another way of importing directly date from the datetime
from datetime import date
today1 = date.today()
print(today1)

# Importing time
import time
timestamp = time.time()
print(timestamp)

# Pip Modules
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))


# Import Custom Module
import Validator
from Validator import validate_email

email = "test@test.com"
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')