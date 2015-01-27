# __author__ = 'dkf'
#-*- coding:utf-8 -*-
#IDE：Pycharm3.4.1


import urllib2, urlparse, gzip
from StringIO import StringIO


USER_AGENT = 'OpenAnything/1.0 +http://diveintopython.org/http_web_services/'


class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(
            self, req, fp, code, msg, headers)
        result.status = code
        return result

    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_302(
            self, req, fp, code, msg, headers)
        result.status = code
        return result


class DefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
    def http_error_default(self, req, fp, code, msg, headers):
        result = urllib2.HTTPError(req.get_full_url(), code, msg, headers, fp)
        result.status = code
        return result


def openAnything(source, etag=None, lastmodified=None, agent=USER_AGENT):
    """URL, filename, or string-->stream"""
    if hasattr(source, 'read'):
        return source

    if source == '-':
        return sys.stdin

    if urlparse.urlparse(source)[0] == 'http':
        #open URL with urllib2
        request = urllib2.Request(source)
        request.add_header('User-Agent', agent)
        if etag:
            request.add_header('If-None-Match', etag)
        if lastmodified:
            request.add_header('If-Modified-Since', lastmodified)
        request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener(SmartRedirectHandler(), DefaultErrorHandler())
        return opener.open(request)

    #try to open with native open function (if source is a filename)
    try:
        return open(source)
    except(IOError, OSError):
        pass

    #treat source as string
    return StringIO(str(source))


def fetch(source, etag=None, last_modefied=None, agent=USER_AGENT):
    """fetch data and metadata from a URL,file,stream, or string"""
    result = {}
    f = openAnything(source, etag, last_modefied, agent)
    result['data'] = f.read()
    if hasattr(f, 'headers'):
        result['etag'] = f.headers.get('ETag')
        result['lastmodified'] = f.headers.get('Last-Modified')
        if f.headers.get('content-encoding', '') == 'gzip':
            result['data'] = gzip.GzipFile(fileobj=StringIO(result['data'])).read()
    if hasattr(f, 'url'):
        result['url'] = f.url
        result['status'] = 200
        if hasattr(f, 'status'):
            result['status'] =f.status
        f.close()
        return result

    