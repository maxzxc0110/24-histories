# coding=utf-8
from bs4 import BeautifulSoup
import urllib
import requests
import string
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#写数据
def wireFile(url,filename):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    data = soup.article.strings
    for i in data:
        open(filename,'ab+').write(i)
        open(filename,'ab+').write("\r\n")
        

if __name__ == '__main__':
    url = "http://duguoxue.cn/ershisishi/4223.html"
    filename = "三国.txt"
    wireFile(url,filename)
