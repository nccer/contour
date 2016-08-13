import threadpool
import urllib2
import random
import time
import os

def worker(url):
    proxy = {'http':url[0]}
    molurl = url[1]
    i = url[2]
    basename = '/home/pc/Documents/mol/'
    filename = basename +molurl.split("/")[-1]
#    proxy_support = urllib2.ProxyHandler(proxy)
#    opener = urllib2.build_opener(proxy_support)
#    urllib2.install_opener(opener)
    i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    req = urllib2.Request(molurl, headers=i_headers)
    try:
	html = urllib2.urlopen(req, timeout=4)
	doc = html.read()
    except Exception:
        pass
    else:
        with open(filename, 'a+') as f:
            f.write(doc)
def boss(proxyurl):
    finalurl = []
    i = 0
    with open('/home/pc/Desktop/data/mol.txt') as f:
	for line in f.readlines():
	    url = line.strip('\n')
	    i += 1
	    filename = '/home/pc/Documents/mol/'+line.split("/")[-1]
            print filename
	    if os.path.exists(filename):
		continue
	    else:
		value = [proxyurl, url, i]
	    finalurl.append(value)
    return finalurl

if __name__ == '__main__':
    proxyurl = "127.0.0.1:8118"
    pool = threadpool.ThreadPool(10)
    i = 0
    while 1:
        i += 1
        finalurl = boss(proxyurl)       
        requests = threadpool.makeRequests(worker, finalurl)
        [pool.putRequest(req) for req in requests]
        pool.wait()
