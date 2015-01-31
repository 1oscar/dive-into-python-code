# __author__ = 'dkf'
#-*- coding:utf-8 -*-
#IDE：Pycharm3.4.1
import re


def rules(language):
    for line in file('D:\Project\python\dive into python\\rules.%s' % language):
        pattern, search, replace = line.split()
        yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)


def plural(noun, language='en'):
    for applyRule in rules(language):
        result = applyRule(noun)
        if result:
            print result


if __name__ == "__main__":
    plural('agency', language='en')


