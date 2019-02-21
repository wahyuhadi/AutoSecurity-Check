import requests
import sys
from urllib import parse
import urllib.parse as urlparse

isCheck= ['"', '>', '<', '(',')','!',';','%','@',"'"]

class LinkCrawler():

    def __init__(self, url):
        self.url = url

    def ChangeQueryParamsValues(self, isUrl, isCheckChar):
        parsed = urlparse.urlparse(isUrl)
        querys = parsed.query.split("&")

        if (parsed.query == ''):
            print ("opps parameter not found")
            sys.exit(1)
        else:
            result = []
            for pairs in isCheckChar:
                if (pairs == "'") or (pairs == '"'):
                    pairs = pairs+'checkxss' 
                new_query = "&".join([ "{}{}".format(query, pairs) for query in querys])
                parsed = parsed._replace(query=new_query)
                result.append(urlparse.urlunparse(parsed))
            return result


    def RequestHtml(self):
        url = self.url
        isUrl = self.ChangeQueryParamsValues(url, isCheck)
        for i in isUrl:
            try: 
                print (i)
                isHtml = requests.get(i, timeout=10)
                if (isHtml.status_code == 200):
                    print ("[+] Get HTML data from URL ..")
                else:
                    print ("[!] Oops response is bad in url", str(i))
                    sys.exit(0)
            except (TimeoutError) as e:
                print ("[+] Oops Request timeout")
                sys.exit(0)
            

    # def Parser()