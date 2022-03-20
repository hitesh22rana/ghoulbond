"""Modules"""
from colorama import Fore
import requests
import tldextract

"""Websites list's"""
Website_list = [
    # Coding Related Websites

    'https://leetcode.com/',
    'https://github.com/',
    'https://codeforces.com/profile/',
    'https://www.codechef.com/users/',
    'https://replit.com/@',
    'https://www.hackerearth.com/',

    # Social Websites

    'https://www.instagram.com/',
    'https://twitter.com/',
    'https://pinterest.com/',
    'https://www.snapchat.com/add/',
    'https://www.reddit.com/user/',
    'https://www.flickr.com/people/',
    'https://www.quora.com/profile/'
]

"""Headers For Performance"""
_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'Access-Control-Allow-Credentials': 'true',
    'Content-Encoding': 'gzip'
}

"""Global Session For Performance"""
session = requests.session()

"""Domain Name Extractor from Website's URL"""
def domain_name(url):
    parsed = tldextract.extract(url)
    return parsed.domain+'.'+parsed.suffix

"""Checks Username from each website"""
def username_check():
    username = input(Fore.LIGHTMAGENTA_EX + '\n[+] Enter Target Username To Scan : ')
    found_list = []
    print()
    for individual_website in Website_list:
        try:
            website_name = domain_name(individual_website)
            print(Fore.LIGHTMAGENTA_EX + f'[+] Searching on {website_name}')
            response = session.get(individual_website+str(username) , timeout=10 , headers=_headers)

            if(response.status_code == 200):
                if(username in response.text):
                    print(Fore.LIGHTGREEN_EX + f'[-_0] {username} Found on {website_name}.')
                    found_list.append(f'{individual_website}{username}')   
                    print()
                else:
                    print(Fore.LIGHTYELLOW_EX + f'[!] {username} Not Found on {website_name} Might be a false positive!')
                    print()
            else:
                print(Fore.LIGHTRED_EX + f'[-] {username} not Found on {website_name}.')
                print()

        except:
            print(Fore.RED + f'Error Occured while! checking {username} on different websites!')
            print(Fore.RED + '[-] Aborting!\n')
            break
    
    if(len(found_list) != 0):
        print(Fore.YELLOW + f'\nUsername found on Websites\n')
        for website_found in found_list:
            print(Fore.GREEN + website_found)
        print()
    else:
        print(Fore.RED + f'\nUsername not found on any Websites\n')

"""Main Function"""
if __name__ == '__main__':
    username_check()