"""Modules"""
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re
from colorama import Fore


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


"""main function"""
def email_scraper():

    user_url = str(input(Fore.RED+'[+] Enter Target URL To Scan : '))
    urls = deque([user_url])
    scraped_urls = set()
    emails = set()

    count = 0

    try:
        while len(urls):
            count += 1
            if count == 100:
                break

            url = urls.popleft()
            scraped_urls.add(url)

            parts = urllib.parse.urlsplit(url)
            base_url = '{0.scheme}://{0.netloc}'.format(parts)

            path = url[:url.rfind('/')+1] if '/' in parts.path else url

            print(Fore.CYAN+'[%d] Processing %s' % (count, url))

            try:
                response = session.get(url,headers=_headers,timeout=10)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, features="lxml")

            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                if not link in urls and not link in scraped_urls:
                    urls.append(link)

    except KeyboardInterrupt:
        print(Fore.RED+'\n[-] Closing!\n')
    
    if(len(emails) == 0):
        print(Fore.RED+"No Email's found\n")
    
    else:
        print(Fore.GREEN +"\nAll found Email's\n")
        for mail in emails:
            print(Fore.YELLOW + f"{mail}")
    
    print(Fore.RESET)

if __name__ == '__main__':
    email_scraper()