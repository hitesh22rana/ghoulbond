# Modules
import os
import platform
from colorama import Fore

def ip_and_mac_address():
    # Check
    if platform.uname()[0] != 'Windows':
        print(Fore.RED + "This work's only for Windows")
        exit()
    
    else:
        raw_address = os.popen('ipconfig /all').read()
        address_all = raw_address.split('\n')
        
        ip_address = []
        mac_address = []
        host_names = []
        
        for individual_name in address_all:
            if('Host Name . . . . . . . . . . . . :') in individual_name:
                host_names.append(individual_name.replace('Host Name . . . . . . . . . . . . :', '').strip())     

            if('IPv4 Address. . . . . . . . . . . :') in individual_name:
                ip_address.append(individual_name.replace('IPv4 Address. . . . . . . . . . . :', '').strip())
            
            if('Physical Address. . . . . . . . . :') in individual_name:
                mac_address.append(individual_name.replace('Physical Address. . . . . . . . . :', '').strip())

        # Host name
        if(len(host_names) == 0):
            print(Fore.RED + "\nHost Name is not found\n")
        
        else:
            print(Fore.RED + "\nHost Name : " , end = ' ')
            for individual_host in host_names:
                print(Fore.GREEN + individual_host , end = '  ')

        # IP Address's
        if(len(ip_address) == 0):
            print(Fore.RED + "No information of any IP address\n")

        else:
            print(Fore.RED + "\nAll gathered IP Address's : " , end = ' ')
            for individual_ip in ip_address:
                print(Fore.GREEN + individual_ip , end = '  ')
    
        # MAC/Physical Address's
        if(len(mac_address) == 0):
            print(Fore.RED + "No information of any MAC/Physical address\n")
        
        else:
            print(Fore.RED + "\nAll gathered Physical/MAC Address's : " , end = ' ')
            for individual_mac in mac_address:
                print(Fore.GREEN + individual_mac , end = '  ')

        print('\n')
        
if __name__ == '__main__':
    ip_and_mac_address()