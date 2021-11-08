# modules
from logo import logo
from email_scraper import email_scraper
from password_grabber import passwords
from colorama import Fore
from termcolor import colored
import logging, coloredlogs

logger = logging.getLogger(f"Logger")
coloredlogs.install(logger=logger)

# logo print
logo()

# Menu
print(Fore.RED+'''
[1] Scrape all Email's from target website
[2] Get all Wifi password's 
''')

# Menu-input
menu_input = int(input(Fore.GREEN+"Enter you'r choice : "))

# Menu-choice
if(menu_input == 1):
    email_scraper()

elif(menu_input == 2):
    passwords()