# __author__ = 'dkf'
#-*- coding:utf-8 -*-
#IDE：Pycharm3.4.1


def openAnything(source):
    if hasattr(source, "read"):
        return source
    if source == '-':
        import sys
        return sys.stdin
    import urllib
    #try to open with urllib (if source is http,ftp,or file URL)
    try:
        return urllib.urlopen(source)
    except(IOError, OSError):
        pass
    #try to open with open function(if source is pathname)
    try:
        return open(source)
    except (IOError, OSError):
        pass
    #treat source as string
    import StringIO
    return StringIO.StringIO(str(source))


