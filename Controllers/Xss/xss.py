import requests
import sys

class LinkCrawler():

    def __init__(self, url):
        self.url = url

    def RequestHtml(self):
        try: 
            isHtml = requests.get(self.url, timeout=10)
        except (TimeoutError) as e:
            print ("[+] Oops Request timeout")
            sys.exit(0)
        if (isHtml.status_code == 200):
            print (isHtml.text)
        else:
            print ("[+] Oops response is bad")
            sys.exit(0)
    
