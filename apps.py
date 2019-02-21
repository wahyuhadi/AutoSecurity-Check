from Controllers.Xss.xss import *
import  argparse
import datetime


def isXssHandler(isUrl):
    # Folder in Controllers -> Xss in xss.py
    isTimeNow = datetime.datetime.now()
    xssAnalisys = LinkCrawler(isUrl)
    xssAnalisys.RequestHtml()
    isEnd = datetime.datetime.now() - isTimeNow
    print ("[!] Process end with time", str(isEnd))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="is url test example : -u https://web.com/?data=aaa", required=True)
    parser.add_argument("-t", help="is tags will check  example : -t xss ", required=True)
    argv = (parser.parse_args())
    isUrl = argv.u
    isTestMethod = argv.t
    if (isTestMethod == 'xss'):
        isXssHandler(isUrl)
    else :
        print ('[+] Opps please check testing avalible')
        
if __name__ == "__main__":
    main()