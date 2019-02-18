# Python-email-script
Pulls up seperate Chrome browser to google search for inputed list of searches, and scrapes URLs from google,
compiles a list and then scrapes emails from individual websites that offer emails as href links, inside 'a' tags

To run code, must have: 
-Chrome Driver, change location in code for your local machine
-Python3
-Selenium
-bs4
-requests
-Internet connection

To run code through terminal:
-Use '1' for searches that require locations, even if its local
-Use '2' for a generic search (Coming Soon)
-Should have 4 command args

python search.py inputFile.txt outEmails.txt '1 or 2'
