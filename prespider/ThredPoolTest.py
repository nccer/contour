import threadpool
import urllib2
import random
import time
import os

def worker(url):
    proxy = {'http':url[0]}
    molbaseurl = url[1]
    finalurl = molbaseurl
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    req = urllib2.Request(finalurl, headers=i_headers)
    try:
	html = urllib2.urlopen(req, timeout=4)
    except Exception:
        pass
    else:
        with open('/home/pc/Desktop/ip.txt', 'a+') as f:
            string = url[0] + '\n'
            f.write(string)
def boss(proxyurl):
    finalurl = []
    for line in proxyurl:
        a = [line, 'www.baiu.com']
        finalurl.append(a)
    return finalurl

if __name__ == '__main__':
    proxyurl = []
    with open('/home/pc/Desktop/proxy.txt') as f:
        for proxystr in f.readlines():
            value = proxystr.strip('\n').strip('\r')
            proxyurl.append(value)
    pool = threadpool.ThreadPool(110)
    finalurl = boss(proxyurl)       
    requests = threadpool.makeRequests(worker, finalurl)
    [pool.putRequest(req) for req in requests]
    pool.wait()
