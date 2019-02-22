import requests
import sys
from urllib import parse
import urllib.parse as urlparse
from bs4 import BeautifulSoup

isCheck= ['"', '>', '<', '(',')','!',';','%','@',"'"]
isXssPayload = ['<script>alert("xss found");</script>',    '"><script>alert("xss found");</script>', "<script>alert('xss found');</script>", "'><script>alert('xss found');</script>"]

CYELL = '\033[93m'
CENDYELL = '\033[0m'
CGRE = '\033[92m'
CYAN = '\033[36m'

class HtmlCheck():

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
        isXssUrl = self.ChangeQueryParamsValues(url, isXssPayload)
        totalRequest = 0
        requestError = 0

        print ("[+] Get HTML data from URL .. ")
        print ("[+] Checking from "+tags+" tags html")
        print ("[+] Indentification html Response .. ")
        for i in range(0, len(isUrl)):
            totalRequest = totalRequest + 1
            try: 
                isQueryParams = self.getQueryParamsUrls(isUrl[i])
                isParamsAndValues = self.getParamsNameAndValues(isQueryParams)
                isHtml = requests.get(isUrl[i], timeout=10)
                if (isHtml.status_code == 200):
                    isParsedHtml = self.Parser(isHtml.text, tags)
                    isAnalised = self.preCheckPayload(isParsedHtml, isParamsAndValues[1])
                    isQueryName = self.queryNameParsing(isQueryParams, isAnalised)
                    if (isQueryName != 'Not Found'):
                        print (CYAN,"[-->] Posible Parameter in URL ", isQueryName , "\n",CENDYELL)
                else:
                    print (CYELL, "[!] Oops response is bad in url ", str(isXssUrl[i]), "\n",CENDYELL)
                    requestError = requestError + 1

            except (TimeoutError) as e:
                print ("[+] Oops Request timeout")
                sys.exit(0)


        print ("[+] Checking Xss Payload ... ")
        for xss in range (0, len(isXssUrl)):
            totalRequest = totalRequest + 1
            try: 
                isQueryParams = self.getQueryParamsUrls(isXssUrl[xss])
                isParamsAndValues = self.getParamsNameAndValues(isQueryParams)
                isHtml = requests.get(isXssUrl[xss], timeout=10)
                if (isHtml.status_code == 200):
                    isParsedHtml = self.Parser(isHtml.text, tags)
                    isAnalised = self.preCheckPayload(isParsedHtml, isParamsAndValues[1])
                    isQueryName = self.queryNameParsing(isQueryParams, isAnalised)
                    if (isQueryName != 'Not Found'):
                        print (CGRE,"[-->] Posible Xss Parameter in URL Found ", isXssUrl[xss] , "\n",CENDYELL)
                else:
                    print (CYELL, "[!] Oops response is bad in url", str(isXssUrl[xss]) , "\n",CENDYELL)
                    requestError = requestError + 1

            except (TimeoutError) as e:
                print ("[+] Oops Request timeout")
                sys.exit(0)


        print ("[+] Total request ", totalRequest)
        print ("[-] Request Success ", totalRequest - requestError)
        print ("[-] Error Request ", requestError)
            

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
                    split = nameParams.split(" ")
                    if name in split   :
                        var = ''
                    else :
                        nameParams += name+" "
        return nameParams or "Not Found"

    def preCheckPayload(self, isParsedHtml, isCheck):
        isResult = []
        for isValue in isCheck:
            if isValue in isParsedHtml:
                isResult.append(isValue)
                print ("[+] Unescape html indentified  ", isValue, "true")
        return isResult