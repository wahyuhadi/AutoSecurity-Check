import requests 
import urllib.parse as urlparse
import json,sys
from pprint import pprint

isErrorbased = ['"', "'", '--']
isJson = []


CYELL = '\033[1;93m'
CENDYELL = '\033[0m'
CGRE = '\033[1;92m'
CYAN = '\033[1;36m'
RED =  '\033[1;31m'


class SimpleSqlCheck():

    def __init__(self, isUrl, isLocation):
        self.isUrl = isUrl
        self.isLocation = isLocation

    def ParsingJson(self):
        if (self.isLocation == False):
            print (RED,"[WARNING] Please add specifict file json location example -j /home/user/api.json",CENDYELL)
            sys.exit(0)
        else :
            print ("[INFO] Parsing Json where method GET ..")
            try:
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
            except (FileNotFoundError) :
                print (RED,"[WARNING] Please add specifict file json location example -j /home/user/api.json ", CENDYELL)
                sys.exit(0)
        
    def isCheckNormalQuery(self):
        try:
            isHeaders = { 'userToken' : 'null'}
            isStatus = (requests.get(self.isUrl, params=isHeaders , timeout=10))
            if (isStatus.status_code == 200):
                print ("[INFO] status OK")
                return isStatus.headers['Content-Length']

        except Exception as e:
                print (RED,"[WARNING] Oops Request timeout ",e, CENDYELL)
                sys.exit(0)


    def isParsingUrl(self): 
        print (CYAN,"[INFO] is Parsing url ..", CENDYELL)
        # pprint (isJson)
        print (CYAN,"[INFO] Is url detected ..", CENDYELL)
        for isurl in isJson:
            print (isurl['request']['url']['raw'])

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
            self.isParsingUrl()

        else:
            lenght = self.isCheckNormalQuery()
            self.IsQueryErrors(lenght)