# Modules
import platform
from colorama import Fore

def sys_info(): 
    my_system = platform.uname()

    print()
    # Host name
    if(my_system.node == ""):
        print(Fore.RED + "Host Name is not found")
    else:
        print(Fore.RED + "Host name : " + Fore.GREEN + f"{my_system.node}")

    # System
    if(my_system.system == ""):
        print(Fore.RED + "System : " + Fore.GREEN + "Others")
    else:
        print(Fore.RED + "System : " + Fore.GREEN + f"{my_system.system}")

    # Release 
    if(my_system.release == ""):
        print(Fore.RED + "No System Released is found!")
    else:
        print(Fore.RED + "Release : " + Fore.GREEN + f"{my_system.release}")

    # Platform
    if(platform.platform() == ""):
        print(Fore.RED + "Platform could not be found!")
    else:
        print(Fore.RED + "Platform : " + Fore.GREEN + f"{platform.platform()}")

    # Architecture
    if(platform.architecture() == ""):
        print(Fore.RED + "Machine's Architecture could not be found!")
    else:
        print(Fore.RED + "Machine's Architecture : " + Fore.GREEN + f"{platform.architecture().__getitem__(0)} , {platform.architecture().__getitem__(1)}" )

    # Processor
    if(my_system.processor == ""):
        print(Fore.RED + "Unable to find Processor's Infromation!")
    else:
        print(Fore.RED + "Processor's Information : " + Fore.GREEN + f"{my_system.processor}")

    print()
    
if __name__ == '__main__':
    sys_info()