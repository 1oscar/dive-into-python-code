# __author__ = 'dkf'
#-*- coding:utf-8 -*-


def printString(params):
    """
    This is python doc!
    The is a functions
    """
    return ";".join(["%s=%s" % (k, v) for (k, v) in params.items()])

if __name__ == "__main__":
    params = {"databases" : "a" ,\
          "maths":"b", \
        "arts" : "c", \
        "computer" : "w"
    }
    print printString(params)
    print printString.__doc__

