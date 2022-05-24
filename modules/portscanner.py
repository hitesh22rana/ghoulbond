"""Modules"""
import socket
import datetime
import sys
from colorama import Fore
from IPy import IP

"""Global Dictionary for result's"""
open_port_details_dict = {}

"""Each Port Scan"""
def scan_port(ipaddress , port , user_given , sock_timeout):
    try:
        sock = socket.socket()
        sock.settimeout(sock_timeout)
        sock.connect((ipaddress, port))

        print(Fore.GREEN + f'[+] Port {port} is Open')
        open_port_details_dict[user_given].append(port)

    except:
        print(Fore.RED + f'[-] Port {port} is Closed')

"""Check Each IP Address"""
def check_ip(ip):
    try:
        return IP(ip)
    except ValueError:
        return socket.gethostbyname(ip)

"""Scan Function"""
def scan(ipaddress , port_number , sock_timeout):
    converted_ip = check_ip(ipaddress)
    print(Fore.RED + f'\n[-_0 Scanning Target] {ipaddress}\n')
    open_port_details_dict[ipaddress] = []
    for port in range(1,port_number+1):
        scan_port(converted_ip , port , ipaddress , sock_timeout)

"""All Port which are to be Scanned"""
def port_inputs():
    try:
        portnum = int(input(Fore.BLUE + '\nEnter the portnumber upto which you want to scan {e.g : 500} (For better results/accuracy input atleast 100) : '))
        return portnum

    except ValueError:
        print(Fore.RED + 'Wrong input for portnumber!!')
        print(Fore.RED + 'Enter portnumber again!!')
        port_inputs()

"""Timeout Functions"""
def timeouts():
    try:
        sock_timeout = float(input(Fore.BLUE + '\nEnter the socket timeout in seconds for better depth search and accuracy (Atleast input 0.5 and for better results/accuracy), More socket time leads to depth search but increase in program result time : '))
        return sock_timeout

    except ValueError:
        print(Fore.RED + 'Wrong input for socket timeout!!')
        print(Fore.RED + 'Enter socket timeout again!!')
        timeouts()

"""Input Function"""
def user_inputs():
    print(Fore.GREEN + 'Enter Domain name {e.g. xyz.com} of the Target/s or IP Address')
    targets = input(Fore.GREEN + '[+] Enter Target/s To Scan (Split multiple targets with , ): ')

    port_number = port_inputs()
    sock_timeout = timeouts()

    print(Fore.BLUE + '\nHold up!! this may take some time depending on the target!')

    try:
        if ',' in targets:
            for ipaddress in targets.split(','):
                try:
                    scan(ipaddress.strip(' ') , port_number , sock_timeout)
                except:
                    print()
                    ipaddress = ipaddress.strip(' ')
                    print(Fore.RED + f'{ipaddress} : is Wrong Domain name or IP address!!')

        else:
            scan(targets.strip(' ').strip(',') , port_number , sock_timeout)

    except:
        print(Fore.RED + '\nYou Entered Wrong Details (Wrong IP Address or Domain name)')
        print(Fore.RED + 'Scan Completed!!')
        sys.exit()

"""Fetch Results"""
def fetch_results():
    print(Fore.BLUE + '\nDo you want the results of just open ports?')

    try:
        choice = int(input(Fore.GREEN + '\n=> Enter 1 for YES and 2 for NO : '))
        if(choice == 1):
            print()
            print(Fore.BLUE + '\nDo you want the results in file format or in command line?')
            results_input = input(Fore.GREEN + '\n=> Enter 1 for File format, 2 for command line or any other key to exit the program : ')

            try:

                if(int(results_input) == 1):
                    current_time = datetime.datetime.now()
                    file_name = str(current_time.day) + ',' + str(current_time.month) + ',' + str(current_time.year) + '.txt'
                    print(Fore.GREEN + f'Details have been saved in {file_name} file')

                    with open(f'{file_name}',"a") as f:
                        f.write('\n')
                        f.write('Time in :- ' + 'hours:minutes:seconds => ' + str(current_time.hour) + ':' + str(current_time.minute) + ':' + str(current_time.hour))
                        f.write('\n')

                        for key, values in open_port_details_dict.items():
                            f.write('Open Port\'s [+] for ' + str(key) + '-> ')

                            if(len(values) == 0):
                                f.write('No Port is Open!')

                            else:
                                f.write('[')
                                length_values = len(values)
                                counter = 0
                                for each in values:
                                    if(counter == length_values-1):
                                        f.write(str(each))
                                    else:
                                        f.write(str(each) + ",")
                                        counter = counter + 1
                            f.write(']')
                            f.write('\n')
                        f.write('------------------------------------------------------------')

                elif(int(results_input) == 2):
                    print()
                    for key , values in open_port_details_dict.items():
                        print(Fore.GREEN + f'Open Port\'s [+] for {key} : {values}')
                    print()

                else:
                    print(Fore.GREEN + 'Scan Successfull!!\n')
                    sys.exit()

            except:
                print(Fore.GREEN + 'Scan Successfull!!\n')
                sys.exit()

        elif(choice == 2):
            return

        else:
            print(Fore.RED + "You Entered some wrong value (Other than 1 or 2) ")
            print(Fore.RED + 'Enter again')
            fetch_results()

    except ValueError:
        print(Fore.RED + "You Entered some wrong value (Other than 1 or 2) ")
        print(Fore.RED + 'Enter again')
        fetch_results()

"""Main Function"""
def port_scan_main():
    print()
    user_inputs()
    print(Fore.GREEN + '\nScan Successfull!!\n')
    if(len(open_port_details_dict) == 0):
        print(Fore.GREEN + "No Open Ports are found!")
        pass
    else:
        fetch_results()
    print(Fore.RESET,end='')

if __name__ == "__main__":
    port_scan_main()