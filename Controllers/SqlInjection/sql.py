import requests 
import urllib.parse as urlparse
import json,sys
from pprint import pprint

isErrorbased = ['"', "'", '--']
isJson = []

class SimpleSqlCheck():

    def __init__(self, isUrl, isLocation):
        self.isUrl = isUrl
        self.isLocation = isLocation

    def ParsingJson(self):
        if (self.isLocation == False):
            print ("[INFO] Please add specifict file json location")
            sys.exit(0)
        else :
            print ("[INFO] Parsing Json where method GET ..")
            with open(self.isLocation) as f:
                data = json.load(f)
                isItems = data['item']
                for items in isItems:
                    try:
                        item = items['item']
                    except (TypeError, KeyError):
                        pass

                    for i in item:
                        try:
                            isMethod = i['request']['method']
                            if (isMethod == 'GET'):
                                isJson.append(i)
                        except (TypeError, KeyError):
                            pass
        
        pprint (isJson)        # pprint (data['item'])

    def isCheckNormalQuery(self):
        try:
            isStatus = (requests.get(self.isUrl , timeout=10))
            if (isStatus.status_code == 200):
                print ("[INFO] status OK")
                return isStatus.headers['Content-Length']

        except (TimeoutError, ConnectionError):
            print ("[INFO] Time Out ")
            pass

    def IsQueryErrors(self, isContentLength):
        print ("[INFO] Checking Error Based ..")
        # isQueryParsed = urlparse.urlparse(self.isUrl).query
        # isQuery = isQueryParsed.split('&')
        # print(isQuery)

        parsed = urlparse.urlparse(self.isUrl).query
        print (urlparse.parse_qs(parsed))
        # querys = parsed.query.split("&")
        # result = []
        # for query in querys:
        #     for pairs in isErrorbased :
        #         print (query)
        #         new_query = "&".join([ "{}{}".format(query, pairs)])
        #         print (new_query)
        #         parsed = parsed._replace(query=new_query)
        #         result.append(urlparse.urlunparse(parsed))
        # print (result)

    def CheckSqlInjection(self):
        if (self.isLocation != False):
            self.ParsingJson()
        else:
            lenght = self.isCheckNormalQuery()
            self.IsQueryErrors(lenght)