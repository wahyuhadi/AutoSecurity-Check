import requests 
import urllib.parse as urlparse

isErrorbased = ['"', "'", '--']

class SimpleSqlCheck():

    def __init__(self, isUrl):
        self.isUrl = isUrl

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

        parsed = urlparse.urlparse(self.isUrl)
        querys = parsed.query.split("&")
        result = []
        for pairs in isErrorbased:
            for query in querys :
                new_query = "&".join([ "{}{}".format(query, pairs)])
                print (new_query)
                parsed = parsed._replace(query=new_query)
                result.append(urlparse.urlunparse(parsed))

        print (result)
    def CheckSqlInjection(self):
        lenght = self.isCheckNormalQuery()
        self.IsQueryErrors(lenght)