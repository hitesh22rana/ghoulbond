# Modules
from logo import logo
from email_scraper import email_scraper
from password_grabber import passwords
from address import ip_and_mac_address
from system_info import sys_info
from portscanner import port_scan_main
from phone_details import get_details
from location import target_location
from keylogger import listener

from colorama import Fore
from termcolor import colored
import logging, coloredlogs

logger = logging.getLogger(f"Logger")
coloredlogs.install(logger = logger)


if __name__ == '__main__':
    
    # logo print
    logo()

    # Menu
    print(Fore.RED + '''
[1] System Information
[2] Get IP and MAC address
[3] Get all Wifi password's 
[4] Scrape all Email's from target website
[5] Port Scanner
[6] Phone Number details
[7] Target Geo-Location
[8] KeyLogger
[9] Quit
''')

    while(True):
        
        
        try:
            # Menu-input    
            menu_input = int(input(Fore.GREEN+"\nEnter you'r choice : "))
        
            if(type(menu_input) == int):
               
                # Menu-choice
                if(menu_input == 1):
                    sys_info()

                elif(menu_input == 2):
                    ip_and_mac_address()

                elif(menu_input == 3):
                    passwords()

                elif(menu_input == 4):
                    email_scraper()
                    
                elif(menu_input == 5):
                    port_scan_main()

                elif(menu_input == 6):
                    get_details()

                elif(menu_input == 7):
                    target_location()

                elif(menu_input == 8):
                    print(Fore.RED + "\nTyped key's data is getting saved in txt file!\n")
                    listener()

                elif(menu_input == 9):
                    print(Fore.YELLOW + "\nThanks For Using ghoulbond\n")
                    break
                    
                else:
                    print(Fore.RED + "\nInvalid Input!\n")
                
            else:
                print(Fore.RED + "\nInvalid Input!\n")
            
        except Exception as e:
            print(Fore.RED + "\nInvalid Input!\n")