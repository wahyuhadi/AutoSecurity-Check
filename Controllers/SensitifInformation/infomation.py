'''
author : rahmat wahyu hadi 
date : 2019-02-22
'''

import requests
import sys
import nmap
import socket
import json 
import pprint

CYELL = '\033[93m'
CENDYELL = '\033[0m'
CGRE = '\033[92m'
CYAN = '\033[36m'

class InformationDisclorse ():
    def __init__ (self, isUrl):
        self.isUrl = isUrl
    
    def GetWebServer (self, isUrl):
        print ("[INFO] Checking information form server ...\n")
        try:
            isResponse = requests.get(isUrl, timeout=10)
            if (isResponse.status_code == 200) : 
                headerJson = isResponse.headers
                try:
                    WebServer = headerJson['Server'] 
                except (ValueError, KeyError, TypeError):
                    WebServer = 'null'

                try:
                    XPowerBy = headerJson['X-Powered-By'] 
                except (ValueError, KeyError, TypeError) : 
                    XPowerBy = 'null'


                if (WebServer != 'null' ):
                    print (CGRE,"[+] Web Server Found ", WebServer, CENDYELL)
                    print (CYELL,"[Advice] Hardening your servers ",CENDYELL)
                if (XPowerBy != 'null'):
                    print (CGRE,"[+] Backend Technology Found ", XPowerBy, CENDYELL)
                    print (CYELL,"[Advice] Hardening your servers ",CENDYELL)
                if (WebServer == 'null' and XPowerBy == 'null'):
                    print ("[+] Server status is Ok\n")

            else : 
                print (CYELL, "[!] Oops response is bad in url ", str(isUrl), "\n",CENDYELL)
        
        except (TimeoutError) as e:
            print ("[+] Oops Request timeout")
            sys.exit(0)

    def ScanningServer(self, isUrl):
        print ("\n[INFO] Scanning Port Server ",isUrl," ..")
        isScaning = nmap.PortScanner() 
        host = socket.gethostbyname(isUrl)
        print ("[-->] Scanning IP : ", host)
        isResultScan = isScaning.scan(host)
        pprint.pprint(isResultScan['scan'][host]['tcp'])

    def FindCritcalLink(self, isUrl):
        isCritical = []
        with open('Controllers/SensitifInformation/link.txt') as filehandle:  
            for line in filehandle:
                uri = line[:-1]
                isCritical.append(uri)

        print ("\n[INFO] Checking Critical URL .. \n")

        for critical in isCritical:
            url = isUrl+critical
            isStatus = (requests.get(url).status_code)
            if (isStatus == 200):
                print (CGRE,"[WARNING] Critical link found ",url,CENDYELL)

    def GetInformation(self):
        self.GetWebServer(self.isUrl)
        self.FindCritcalLink(self.isUrl)