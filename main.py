# coding=utf-8
from bs4 import BeautifulSoup
import urllib
import requests
import string
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#获取网页状态码
def get_status(url):  
    r = requests.get(url, allow_redirects = False)  
    return r.status_code 

#初始化soup
def initSoup(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    return soup

#写数据
def wireFile(url,filename):
    soup = initSoup(url)
    title = soup.h1.string
    open(filename,'ab+').write(title)
    open(filename,'ab+').write("\r\n")
    data = soup.article.strings
    s1 = BeautifulSoup('上篇')
    s2 = BeautifulSoup('目录')
    s3 = BeautifulSoup('下篇')
    for i in data:
        if (i.string == s1.string or i.string == s2.string or i.string == s3.string):
            pass
        else:
            open(filename,'ab+').write(i)
            open(filename,'ab+').write("\r\n")
            


#获取单个页面所有href   
def getAllHref(url):
    soup = initSoup(url)
    liArr = soup.find_all('li')
    urlArr = []
    for i in liArr:
        href = i.a['href']
        urlArr.append(href)
    return urlArr
#获取书名
def getFileName(url):
    soup = initSoup(url)
    title = soup.h1.string
    filename = title+".txt"
    return filename

#下载一本书
def downloadOneBook(url):
    orginUrl = url
    fileName = getFileName(url)
    print fileName
    AllHref = getAllHref(url)
    for url in AllHref:
        wireFile(url,fileName)
    i = 2
    while(1):
        if(get_status(url)==200):
            url = orginUrl+"list-"+str(i)+".html"
            print url
            AllHref = getAllHref(url)
            for url in AllHref:
                #pass
                wireFile(url,fileName)
            i = int(i)
            i = i+1
        else:
            break


if __name__ == '__main__':
    url = "http://duguoxue.cn/ershisishi/baihuashiji/"

    downloadOneBook(url)
      
