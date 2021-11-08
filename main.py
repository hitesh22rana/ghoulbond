# modules
from logo import logo
from email_scraper import email_scraper
from password_grabber import passwords

# logo print
logo()

# Menu
print('''\033[1;31;40m
[1] Scrape all Email's from target website
[2] Get all Wifi password's 
''')

# Menu-input
menu_input = int(input("\033[1;32;40mEnter you'r choice : "))

# Menu-choice
if(menu_input == 1):
    email_scraper()

elif(menu_input == 2):
    passwords()