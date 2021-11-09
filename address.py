# Modules
import os
import platform
from colorama import Fore


def other_than_windows():
    raw_address_list = os.popen('ifconfig').read().strip().trim()
    address_list = raw_address_list.split('\n')

    ip_private_address = []
    mac_address = []

    for individual_name in address_list:
        if('inet ') in individual_name:
            ip_private_address.append(individual_name.replace('inet ' , '').strip())

        if('ether ') in individual_name:
            mac_address.append(individual_name.replace('ether ' , '').strip())

    # Hostname
    print(Fore.RED + "Host Name : " + Fore.GREEN + f"{os.popen('hostname').read().strip()}")
    
    # IP Address's Private
    if(len(ip_private_address) == 0):
        print(Fore.RED + "No information of any (Private/local) IP address's \n")

    else:
        print(Fore.RED + "All gathered IP Address's (Private/local) : " , end = ' ')
        for individual_ip in ip_private_address:
            print(Fore.GREEN + individual_ip , end = '  ')
    
    # MAC/Physical Address's
    if(len(mac_address) == 0):
        print(Fore.RED + "No information of any MAC/Physical address\n")
        
    else:
        print(Fore.RED + "\nAll gathered Physical/MAC Address's : " , end = ' ')
        for individual_mac in mac_address:
            print(Fore.GREEN + individual_mac , end = '  ')

    print('\n')
        

def ip_and_mac_address():
    # Check
    if platform.uname()[0] != 'Windows':
        other_than_windows()
    
    else:
        raw_address = os.popen('ipconfig /all').read()
        address_all = raw_address.split('\n')
        public_address = os.popen('nslookup myip.opendns.com resolver1.opendns.com').read()

        ip_private_address = []
        mac_address = []
        host_names = []
        
        for individual_name in address_all:
            if('Host Name . . . . . . . . . . . . :') in individual_name:
                host_names.append(individual_name.replace('Host Name . . . . . . . . . . . . :', '').strip())     

            if('IPv4 Address. . . . . . . . . . . :') in individual_name:
                ip_private_address.append(individual_name.replace('IPv4 Address. . . . . . . . . . . :', '').strip())
            
            if('Physical Address. . . . . . . . . :') in individual_name:
                mac_address.append(individual_name.replace('Physical Address. . . . . . . . . :', '').strip())

        # Host name
        if(len(host_names) == 0):
            print(Fore.RED + "\nHost Name is not found\n")
        
        else:
            print(Fore.RED + "\nHost Name : " , end = ' ')
            for individual_host in host_names:
                print(Fore.GREEN + individual_host , end = '  ')
        print()
        # Public IP Address's Public
        if(len(public_address) == 0):
            print(Fore.RED + "\nNo information of any (Public) IP address's \n")
        else:
            print(Fore.RED + "\nAll gathered Public IP Address's : ")
            print(Fore.GREEN + public_address , end = '')

        # Private IP Address's
        if(len(ip_private_address) == 0):
            print(Fore.RED + "No information of any IP address\n")

        else:
            print(Fore.RED + "All gathered IP Address's : " , end = ' ')
            for individual_ip in ip_private_address:
                print(Fore.GREEN + individual_ip , end = '  ')

        print()

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