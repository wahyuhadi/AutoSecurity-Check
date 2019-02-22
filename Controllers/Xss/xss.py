import requests
import sys
from urllib import parse
import urllib.parse as urlparse
from bs4 import BeautifulSoup

isCheck= ['"', '>', '<', '(',')','!',';','%','@',"'"]

class LinkCrawler():

    def __init__(self, url, tags):
        self.url = url
        self.tags = tags

   
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
        tags = self.tags
        isUrl = self.ChangeQueryParamsValues(url, isCheck)
        print ("[+] Checking from "+tags+" tags html")
        for i in isUrl:
            try: 
                isHtml = requests.get(i, timeout=10)
                if (isHtml.status_code == 200):
                    print ("[+] Get HTML data from URL ..")
                    self.Parser(isHtml.text, tags)
                else:
                    print ("[!] Oops response is bad in url", str(i))
                    sys.exit(0)
            except (TimeoutError) as e:
                print ("[+] Oops Request timeout")
                sys.exit(0)
            

    def Parser(self, isHtmlResponse, isTagsHtml):
        isHtml = ''
        if (isTagsHtml == 'all') : 
            isHtml = isHtmlResponse
        else :
            isParsedHtml = BeautifulSoup(isHtmlResponse,'html.parser')
            html = isParsedHtml.find_all(isTagsHtml)
            for x in html:
                tags = str(x).replace(" ", "")
                isHtml += tags

        return isHtml