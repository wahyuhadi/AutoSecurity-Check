from Controllers.Xss.xss import HtmlCheck
import  argparse
import datetime


def isXssHandler(isUrl, isTags):
    # Folder in Controllers -> Xss in xss.py
    isTimeNow = datetime.datetime.now()
    xssAnalisys = HtmlCheck(isUrl, isTags)
    xssAnalisys.RequestHtml()
    isEnd = datetime.datetime.now() - isTimeNow
    print ("[!] Process end with time", str(isEnd))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="is url test example : -u https://web.com/?data=aaa", required=True)
    parser.add_argument("-m", help="is tags will check  example : -m xss ", required=True)
    parser.add_argument("-t", help="is tags will check  example : -t value or div or a ")

    argv = (parser.parse_args())
    isUrl = argv.u
    isTestMethod = argv.m
    isTags = argv.t or 'all'
    if (isTestMethod == 'xss'):
        isXssHandler(isUrl,isTags)
    else :
        print ('[+] Opps please check testing avalible')
        
if __name__ == "__main__":
    main()