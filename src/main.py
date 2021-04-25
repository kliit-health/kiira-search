#!/usr/bin/python
# -- coding utf-8 --

from kiira_search import *
import time

banner()
target = str(input('[*] Enter the website URL: ')).lower().strip()


def start():
    time.sleep(0.50)
    ask = 'emails'

    if ask == 'website': 
        extract_websites(target)
    elif ask == 'links': 
        get_links(target)
    elif ask == 'navigate':   
        navigate_links(target)
    elif ask == 'emails':
        extract_emails(target)
    elif ask == 'cookies':
        extract_cookies(target)
    elif ask == 'grabbing':
        website_grabber(target)
    else: 
        print('[-] Enter a valid answer.')

    print("All done")

if __name__ == '__main__':
    start()
