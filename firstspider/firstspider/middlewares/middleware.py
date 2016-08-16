from proxy import PROXIES
from agents import AGENTS_ALL

import random

class CustomHttpProxyMiddleware(object):
    def process_request(self, request, spider):
	if self.use_proxy(request):
	    p = random.choice(PROXIES)
	    try:
		request.meta['proxy'] = "http://%s" % p['ip_port']
	    except Exception, e:
                print e
    def use_proxy(self, request):
	return True

class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
	agent = random.choice(AGENTS_ALL)
	request.headers['User-Agent'] = agent

