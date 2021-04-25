#!/usr/bin/python
# -- coding utf-8 --

from kiira_search import *
import time

banner()
alvo = str(input('[*] Enter the website URL: ')).lower().strip()


def start():
    time.sleep(0.50)
    ask = 'emails'

    if ask == 'website': 
        extract_websites(alvo)
    elif ask == 'links': 
        get_links(alvo)
    elif ask == 'navigate':   
        navigate_links(alvo)
    elif ask == 'emails':
        extract_emails(alvo)
    elif ask == 'cookies':
        extract_cookies(alvo)
    elif ask == 'grabbing':
        website_grabber(alvo)
    else: 
        print('[-] Enter a valid answer.')

    print("All done")

if __name__ == '__main__':
    start()
