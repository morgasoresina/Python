# Import the 'string' module with the alias 'st'
import string as st
# Import the 'numpy' module with the alias 'np'
import numpy as np
# Import the 'time' module
import time

# Get all the digits as a string
numbers = st.digits
# Get all the punctuation symbols as a string
symbols = st.punctuation
# Get all the letters (uppercase and lowercase) as a string
letters = st.ascii_letters
# Concatenate all the strings into a single string
build = letters+symbols+numbers

# Randomly choose 10 characters from the 'build' string and create a list with them
password = np.random.choice(list(build),10)

# Wait for the user to press any key
input('Press any key to get a safe password ')
# 2 seconds wait for the "building" (just for fun)
time.sleep(2)
# Convert the 'password' list into a string and print it on the screen
print(''.join(password))