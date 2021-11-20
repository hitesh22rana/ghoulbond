# Modules
from colorama import Fore
import requests
import tldextract
import time

# Websites list's
Website_list = [
    # Coding Related Websites
    'https://leetcode.com/',
    'https://github.com/',
    'https://codeforces.com/profile/',
    'https://www.codechef.com/users/',
    'https://replit.com/@'
    'https://www.hackerearth.com/'

    # Social Websites 
    'https://www.instagram.com/',
    'https://twitter.com/',
    'https://pinterest.com/',
    'https://www.snapchat.com/add/',
    'https://www.reddit.com/user/',
    'https://www.flickr.com/people/',
    'https://www.quora.com/profile/'
]

def domain_name(url):
    parsed = tldextract.extract(url)
    return parsed.domain+'.'+parsed.suffix

def username_check():
    global Website_list
    
    username = input(Fore.RED + '\n[+] Enter Target Username To Scan : ')

    found_list = []
    print()
    for individual_website in Website_list:
        try:
            website_name = domain_name(individual_website)
            print(Fore.RED + f'[+] Searching on {website_name}')
            response = requests.get(individual_website+str(username) , timeout=10)

            time.sleep(2)

            if(response.status_code == 200):
                found_list.append(f'{individual_website}{username}')
            
            else:
                pass

        except:
            print(Fore.RED + f'Error Occured while! checking {username} on different websites!')
            print(Fore.RED + '[-] Aborting!')
            break
    
    if(len(found_list) != 0):
        print(Fore.YELLOW + f'\nUsername found on Websites\n')
        for website_found in found_list:
            print(Fore.GREEN + website_found)
        print()
    else:
        print(Fore.RED + f'\nUsername not found on any Websites\n')

if __name__ == '__main__':
    username_check()