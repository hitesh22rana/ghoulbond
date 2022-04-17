"""Internal Modules"""
from modules.logo import logo
from modules.email_scraper import email_scraper
from modules.password_grabber import passwords
from modules.address import ip_and_mac_address
from modules.system_info import sys_info
from modules.portscanner import port_scan_main
from modules.phone_details import get_details
from modules.location import target_location
from modules.username_check import username_check
from modules.speed_test import speedTestResult

"""External Modules"""
from colorama import Fore
from termcolor import colored
import logging, coloredlogs

logger = logging.getLogger(f"Logger")
coloredlogs.install(logger = logger)


if __name__ == '__main__':
    
    """logo print"""
    logo()

    while(True):

        """Menu"""
        print(Fore.LIGHTBLACK_EX + '''
[1] System Information
[2] Get IP and MAC address
[3] Get all Wifi password's 
[4] Scrape all Email's from target website
[5] Port Scanner
[6] Phone Number details
[7] Target Geo-Location
[8] Internet Speed Test
[9] Username check
[10] Quit
''')
                
        try:
            """Menu-input"""    
            menu_input = int(input(Fore.GREEN+"Enter you'r choice : "))
        
            if(type(menu_input) == int):

                """Menu-choice"""
                match(menu_input):
                    case 1:
                        sys_info()
                    case 2:
                        ip_and_mac_address()
                    case 3:
                        passwords()
                    case 4:
                        email_scraper()
                    case 5:
                        port_scan_main()
                    case 6:
                        get_details()
                    case 7:
                        target_location()
                    case 8:
                        speedTestResult()
                    case 9:
                        username_check()
                    case 10:
                        print(Fore.YELLOW + "\nThanks For Using ghoulbond\n")
                        break
                    case _:
                        print(Fore.RED + "\nInvalid Input!\n")
            else:
                print(Fore.RED + "\nInvalid Input!\n")

        except KeyboardInterrupt:
            print(Fore.RED+'\n\n[-] Closing!')
            print(Fore.YELLOW + "Thanks For Using ghoulbond\n")
            break

        except Exception as e:
            print(Fore.RED + "\nInvalid Input!")