import requests 

class SimpleSqlCheck():

    def __init__(self, isUrl):
        self.isUrl = isUrl

    def isCheckNormalQuery(self):
        try:
            isStatus = (requests.get(self.isUrl , timeout=10))
            if (isStatus.status_code == 200):
                print ("[INFO] status OK")
                print (isStatus.url)
                print (isStatus.headers['Content-Length'])

        except (TimeoutError, ConnectionError):
            print ("[INFO] Time Out ")
            pass
    # def IsQueryErrors(self):

    def CheckSqlInjection(self):
        self.isCheckNormalQuery()
        # self.IsQueryErrors()