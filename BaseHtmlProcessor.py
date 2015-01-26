# __author__ = 'dkf'
#-*- coding:utf-8 -*-
#IDE：Pycharm3.4.1
from sgmllib import SGMLParser
import htmlentitydefs


class BaseHtmlProcessor(SGMLParser):
    def reset(self):
        #extend(called by SGMLParser.__init__)
        self.pieces = []
        SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs):
        #called for each start tag
        #attrs is a list of (attr,value)tuples
        #e.g for <pre class="screen">,tag="pre", attrs=[("class","screen")]
        strattrs = " ".join(['%s="%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())

    def unknown_endtag(self, tag):
        self.pieces.append("</%(tag)s>" % locals())

    def handle_charref(self, ref):
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityref(self, ref):
        self.pieces.append("&%(ref)s" % locals())
        if htmlentitydefs.entitydefs.has_key(key):
            self.pieces.append(";")

    def handle_data(self, text):
        self.pieces.append(text)

    def handle_comment(self, text):
        self.pieces.append("<!--%(text)s-->" % locals())

    def handle_pi(self, text):
        self.pieces.append("<?%(text)s>" % locals())

    def handle_decl(self, text):
        self.pieces.append("<!%(text)s>" % locals())

    def output(self):
        """
        :return:processed HTML as a single string
        """
        return " ".join(self.pieces)

if __name__ == "__main__":
    for k, v in globals().items():
        print k, "=", v


















