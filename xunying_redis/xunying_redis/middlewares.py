# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from .settings import USER_AGENTS


# 随机的User-Agent
class RandomUserAgent(object):
    def process_request(self, request, spider):
        userAgent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", userAgent)




