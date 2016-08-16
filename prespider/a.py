import threadpool
import urllib2

def worker(url):
    proxy = {'http':url[0]}
    molurl = url[1]
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    req = urllib2.Request(molurl, headers=i_headers)
    try:
	html = urllib2.urlopen(req, timeout=4)
	doc = html.read()
    except Exception:
        print Exception
    else:
        with open('/home/pc/Desktop/ip.txt', 'a+') as f:
            url=url[0]+'\n'
            f.write(url)
def boss(proxyurl):
    finalurl = []
    for line in proxyurl:
	value = [line, 'http://www.chemicalbook.com/']
	finalurl.append(value)
    return finalurl

if __name__ == '__main__':
    proxyurl = []
    with open('/home/pc/Desktop/ip2.txt') as f:
        for proxystr in f.readlines():
            value = proxystr.strip('\n').strip('\r')
            proxyurl.append(value)
    pool = threadpool.ThreadPool(10)
    finalurl = boss(proxyurl)       
    requests = threadpool.makeRequests(worker, finalurl)
    [pool.putRequest(req) for req in requests]
    pool.wait()
