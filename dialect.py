# __author__ = 'dkf'
#-*- coding:utf-8 -*-
#IDE：Pycharm3.4.1
import re
from BaseHtmlProcessor import BaseHtmlProcessor


class Dialectizer(BaseHtmlProcessor):
    subs = ()

    def reset(self):
        self.verbatim = 0
        BaseHtmlProcessor.reset(self)

    def start_pre(self, attrs):
        self.verbatim += 1
        self.unknown_starttag("pre", attrs)

    def end_pre(self):
        self.unknown_endtag("pre")
        self.verbatim -= 1

    def handle_data(self, text):
        self.pieces.append(self.verbatim and text or self.process(text))

    def process(self, text):
        for fromPatter, toPattern in self.subs:
            text = re.sub(fromPatter,toPattern,text)
        return text


class ChefDialectizer(Dialectizer):
    subs = ((r'a([nu])', r'u\1'),
            (r'A([nu])',r'U\1'),
            (r'a\B', r'e'),
            (r'A\B', r'E'),
            (r'en\b', r'ee'),
            (r'\Be\b', r'e-a'),
            (r'\Bew', r'oo'),
            (r'\be', r'i'),
            (r'\bE', r'l'),
            (r'\Bf', r'ff'),
            (r'\Bir', r'ur'),
            (r'(\w*?)i(\w*?)$', r'\1ee\2'),
            (r'bow', r'oo'),
            (r'\bo', r'oo'),
            (r'\bO', r'Oo'),
            (r'the', r'zee'),
            (r'The', r'Zee'),
            (r'th\b', r't'),
            (r'\Btion', r'shun'),
            (r'\Bu', r'oo'),
            (r'BU', r'Oo'),
            (r'v', r'f'),
            (r'V', r'F'),
            (r'w', r'w'),
            (r'W', r'W'),
            (r'([a-z])[,]', r'\1. Bork Bork Bork!'))


class FuddDialectizer(Dialectizer):
    """ convert HTMl to Elmer Fudd-speak
    """
    subs = ((r'[rl]', r'w'),
            (r'qu', r'qw'),
            (r'th', r'd'),
            (r'n[,]', r'n, uh-hah-hah-hah.'))


class OldeDialectizer(Dialectizer):
    """ convert HTml to mock Middle ENglish
    """
    subs = ((r'i([bcdfghjklmnpqrstvwxyz]e\b', r'y\1'),
            (r'ick\b', r'yk'),
            (r'oa', r'oo'),
            (r'ue', r'e'))


def translate(url, dialectName="chef"):
    """
    fecth URL and translate using dialect
    """
    import urllib
    sock = urllib.urlopen(url)
    htmlSource = sock.read()
    sock.close()
    parseName = "%sDialectizer" % dialectName.capitalize()
    parseClass = globals()[parseName]
    parse = parseClass()
    parse.feed(htmlSource)
    parse.close()
    return parse.output()


def test(url):
    """
     test all dialect against URL
    :return:
    """
    for dialect in ("chef", "fudd", "olde"):
        outfile = "%s.html" % dialect
        fsock = open(outfile, "wb")
        fsock.write(translate(url, dialect))
        fsock.close()
        import webbrowser
        webbrowser.open_new(outfile)

if __name__ == "__main__":
    test("http://diveintopython.org/odbchelper_list.html")


