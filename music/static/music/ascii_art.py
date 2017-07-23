import sys
import codecs
import locale


sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
x1 = u"\u00D7"
x2 = x1 * 2
x3 = x1 * 3
x4 = x2 * 2
x5 = x1 * 5
x6 = x3 * 2
x7 = x1 * 7
s1 = ' '
s2 = '  '
s3 = '   '
# print "this " + line
a = s1 + x5 + ' \n' + x2 + s3 + x2 + '\n' + x7 + \
    '\n' + x2 + s3 + x2 + '\n' + x2 + s3 + x2 + '\n'
b = x6 + '\n' + x2 + s3 + x2 + '\n' + x6 + '\n' + x2 + s3 + x2 + '\n' + x6
print a, b
