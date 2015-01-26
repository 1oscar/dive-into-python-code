# __author__ = 'dkf'
#-*- coding:utf-8 -*-
#IDE：Pycharm3.4.1
from sgmllib import SGMLParser


class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):
        href = [v for k, v in attrs if k=='href']
        if href:
            self.urls.extend(href)

if __name__ == "__main__":
    import urllib
    usock = urllib.urlopen("http://diveintopython.org/")
    parser = URLLister()
    parser.feed(usock.read())
    parser.close()
    usock.close()
    for url in parser.urls:
        print url, "Dkf"