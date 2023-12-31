# openai


## To not get SSL Certificate Error
One possible solution is to instruct Python to use your Windows Certificate Store instead of the built-in store in the certifi package. You can do that by installing python-certifi-win32:

pip install python-certifi-win32
Python in then using the same certificates as your browsers do.