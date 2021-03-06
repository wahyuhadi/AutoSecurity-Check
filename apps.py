'''
author : rahmat wahyu hadi 
date : 2019-02-22
'''

from Controllers.Xss.xss import HtmlCheck
from Controllers.SensitifInformation.infomation import InformationDisclorse
from Controllers.SqlInjection.sql import SimpleSqlCheck
import  argparse
import datetime
import json

def isListAvail():
    CYAN = '\033[36m'
    END = '\033[0m'
    with open('method.json') as f:
        data = json.load(f)
    for i in range(0, len(data)):
        print ("[+] method / -m = ", data[i]['method'])
        print (CYAN,"[-->] version     = ", data[i]['version'], "\n",END)

def isXssHandler(isUrl, isTags):
    # Folder in Controllers -> Xss in xss.py
    isTimeNow = datetime.datetime.now()
    xssAnalisys = HtmlCheck(isUrl, isTags)
    xssAnalisys.RequestHtml()
    isEnd = datetime.datetime.now() - isTimeNow
    print ("[!] Process end with time", str(isEnd))

def isInformationGatheringHandler(isUrl):
    informationGather = InformationDisclorse(isUrl)
    informationGather.GetInformation()

def isSQlInjectionHandler(isUrl, isJson):
    sqli = SimpleSqlCheck(isUrl, isJson)
    sqli.CheckSqlInjection()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="is url test example : -u https://web.com/?data=aaa")
    parser.add_argument("-m", help="method for testing, see with -l, example: -m xss ", required=True)
    parser.add_argument("-t", help="is tags will check  example : -t value or div or a ")
    parser.add_argument("-j", help="json export for test API location : -j /home/user/api.json")

    argv = (parser.parse_args())
    isUrl = argv.u
    isTestMethod = argv.m
    isTags = argv.t or 'all'
    isJson = argv.j or False

    if (isTestMethod == 'xss'):
        isXssHandler(isUrl,isTags)
    elif (isTestMethod == 'info'):
        isInformationGatheringHandler(isUrl)
    elif (isTestMethod == 'sqli'):
        isSQlInjectionHandler(isUrl,isJson)
    else :
        print ('[+] Opps please check testing avalible')
        isListAvail()
        
if __name__ == "__main__":
    main()