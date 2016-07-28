# -*- coding: utf-8 -*- 

from HTMLParser import HTMLParser
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    divfloat = 0
    divpadding = 0
    litag = 0
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
		if attr[1] == 'float:left;':
		    self.divfloat = 1
		if attr[1] == 'padding-left:150px;width:670px;':
		    self.divpadding = 1
    def handle_endtag(self, tag):
	if tag == 'div':
	    if self.divfloat == 1:
		self.divfloat = 0
		with open('/Users/changjun/Desktop/data2.txt', 'a+') as f:
		    f.write(',')
	    if self.divpadding == 1:
		with open('/Users/changjun/Desktop/data2.txt', 'a+') as f:
		    f.write('|')
		self.divpadding = 0
	if tag == 'body':
	   with open('/Users/changjun/Desktop/data2.txt', 'a+') as f:
	       f.write('\n')
    def handle_data(self, data):
	string = data.strip('：').strip('	').strip('\r').strip('\n')
	if self.divfloat == 1:
	    with open('/Users/changjun/Desktop/data2.txt', 'a+') as f:
		f.write(string)
	if self.divpadding == 1:
	    with open('/Users/changjun/Desktop/data2.txt', 'a+') as f:
		f.write(string)
BOM_CODE={
    'BOM_UTF8':'utf_8',
    'BOM_LE':'utf_16_le',
    'BOM_BE':'utf_16_be',
    }
DEFAULT_CODES=['utf8']

def decode_file(d):
    for k in BOM_CODE:
        if k==d[:len(k)]:
            code=BOM_CODE[k]
            d=d[len(k):]
            text=d.decode(code)
            return text.splitlines()
    for encoding in DEFAULT_CODES:
        try:
            text=d.decode(encoding)
            return text.splitlines()
        except:
            continue
    raise Exception('解码失败')
def read_file(file_name):
    with open(file_name,'rb')as fn:
        return decode_file(fn.read())
i = 0
while i < 15768:
    i += 1
    print str(i)
    string = '/Users/changjun/molbase/' + str(i) + '.html'
    myparser = MyHTMLParser()
    for line in read_file(string):
        myparser.feed(line)
