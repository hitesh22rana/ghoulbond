# Modules
from logo import logo
from email_scraper import email_scraper
from password_grabber import passwords
from address import ip_and_mac_address
from system_info import sys_info
from colorama import Fore
from termcolor import colored
import logging, coloredlogs

logger = logging.getLogger(f"Logger")
coloredlogs.install(logger=logger)

# logo print
logo()

# Menu
print(Fore.RED+'''
[1] System Information
[2] Get IP and MAC address
[3] Get all Wifi password's 
[4] Scrape all Email's from target website
''')

# Menu-input
menu_input = int(input(Fore.GREEN+"Enter you'r choice : "))

# Menu-choice
if(menu_input == 1):
    sys_info()

elif(menu_input == 2):
    ip_and_mac_address()

elif(menu_input == 3):
    passwords()

elif(menu_input == 4):
    email_scraper()