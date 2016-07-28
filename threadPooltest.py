import threadpool
import urllib2
import random
import time
import os

def worker(url):
    proxy = {'http':url[0]}
    molbaseurl = url[1]
    i = url[2]
    finalurl = molbaseurl[0:-1] + '-contact'
    print finalurl
    basename = '/Users/changjun/molbase/'
    filename = basename + str(i) + '.html'
    print filename
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    req = urllib2.Request(finalurl, headers=i_headers)
    try:
	html = urllib2.urlopen(req, timeout=4)
	doc = html.read()
#	doc = ''
    except Exception:
        pass
    else:
        if len(doc) > (20*1024):
            with open(filename, 'a+') as f:
                f.write(doc)
#with open('/Users/changjun/Desktop/goodip.txt', 'a+') as f:
#                string = url[0] + '\n'
#               f.write(string)
        else:
            print doc
def boss(proxyurl):
    finalurl = []
    i = 0
    j = 0
    with open('/Users/changjun/Desktop/diff.txt') as f:
	for line in f.readlines():
	    url = line.strip('\n')
	    i += 1
	    filename = '/Users/changjun/molbase/' + str(i) + '.html'
	    if os.path.exists(filename):
		continue
	    else:
		value = [proxyurl[j], url, i]
		j += 1
	    finalurl.append(value)
	    if len(finalurl) == len(proxyurl):
		break
    return finalurl

if __name__ == '__main__':
    proxyurl = []
    with open('/Users/changjun/Desktop/ip.txt') as f:
        for proxystr in f.readlines():
            value = proxystr.strip('\n').strip('\r')
            proxyurl.append(value)
    pool = threadpool.ThreadPool(110)
    i = 0
    while 1:
        i += 1
        finalurl = boss(proxyurl)       
        requests = threadpool.makeRequests(worker, finalurl)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        print 'Sleep!', str(i)
        time.sleep(300)
