"""Modules"""
from colorama import Fore
import time

def loading (iteration, total, prefix = '', suffix = '', length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(Fore.GREEN+f'\r{prefix} |{bar}| {suffix}', end = printEnd)
    if iteration == total: 
        print()

def printloader():
    print(Fore.GREEN+'''
 <=====================================Loading=====================================>
''')
    items = list(range(0, 50))
    l = len(items)

    loading(0, l, prefix = '', suffix = '', length = 81)
    for i, _ in enumerate(items):
        time.sleep(0.025)
        loading(i + 1, l, prefix = '', suffix = '', length = 81)

def logo():
    try:
        printloader()

        print(Fore.GREEN+'''
           /$$                           /$$ /$$                                 /$$
          | $$                          | $$| $$                                | $$
  /$$$$$$ | $$$$$$$   /$$$$$$  /$$   /$$| $$| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$
 /$$__  $$| $$__  $$ /$$__  $$| $$  | $$| $$| $$__  $$ /$$__  $$| $$__  $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$
| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/| $$| $$$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$
 \____  $$|__/  |__/ \______/  \______/ |__/|_______/  \______/ |__/  |__/ \_______/
 /$$  \ $$                                                                          
|  $$$$$$/                                                                          
 \______/                                                                                
 ''')

    except KeyboardInterrupt:
        print(Fore.RED+'\nError!! in starting'+Fore.GREEN+' ghoulbond '+Fore.RED+'[-] Closing!\n')
    print(Fore.RESET,end='')

if __name__ == '__main__':
    logo()