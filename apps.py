from Controllers.Xss.xss import *
import  argparse


def isXssHandler(isUrl):
    tes = LinkCrawler(isUrl)
    tes.RequestHtml()

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