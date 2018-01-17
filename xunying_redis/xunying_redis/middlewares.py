# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from .settings import USER_AGENTS
from .settings import PROXY as proxy_url


# 随机的User-Agent
class RandomUserAgent(object):
    def process_request(self, request, spider):
        userAgent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", userAgent)


class ProxyMiddleWare(object):
    def process_request(self, request, spider):
        r = requests.get(proxy_url)
        proxy = r.text

        proxy = proxy.encode("utf-8")

        request.meta['proxy'] = proxy




