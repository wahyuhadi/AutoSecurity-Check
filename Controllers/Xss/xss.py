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


    def getQueryParamsUrls(self, isUrl):
        isQuery= dict(urlparse.parse_qsl(urlparse.urlsplit(isUrl).query))
        return isQuery


    def getParamsNameAndValues(self, isDict):
        paramsName = []
        paramsValues = []
        for name,dict_ in isDict.items():
            paramsName.append(name)
            paramsValues.append(dict_)

        return paramsName, paramsValues



    def RequestHtml(self):
        url = self.url
        tags = self.tags
        isUrl = self.ChangeQueryParamsValues(url, isCheck)
        print ("[+] Get HTML data from URL .. ")
        print ("[+] Checking from "+tags+" tags html")
        print ("[+] Indentification html Response .. ")
        for i in range(0, len(isUrl)):
            try: 
                isQueryParams = self.getQueryParamsUrls(isUrl[i])
                isParamsAndValues = self.getParamsNameAndValues(isQueryParams)
                isHtml = requests.get(isUrl[i], timeout=10)
                if (isHtml.status_code == 200):
                    isParsedHtml = self.Parser(isHtml.text, tags)
                    isAnalised = self.preCheckPayload(isParsedHtml, isParamsAndValues[1])
                    isQueryName = self.queryNameParsing(isQueryParams, isAnalised)
                    print ("[+] Posible Parameter in URL ", isQueryName , "\n")
                else:
                    print ("[!] Oops response is bad in url", str(isUrl[i]) , "\n")

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


    def queryNameParsing(self, isDict, isValue):
        nameParams = ""
        for value in isValue:
            for name, key in isDict.items() :
                if key == value:
                    nameParams += name+" "
        return nameParams or "Not Found"

    def preCheckPayload(self, isParsedHtml, isCheck):
        isResult = []
        for isValue in isCheck:
            if isValue in isParsedHtml:
                isResult.append(isValue)
                print ("[+] Xss indentified !! ", isValue)
        return isResult
        