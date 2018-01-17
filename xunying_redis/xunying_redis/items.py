# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class XunyingItem(scrapy.Item):
    name = scrapy.Field()         # 名字
    director = scrapy.Field()  # 导演
    screenwriter = scrapy.Field()  # 编剧
    star = scrapy.Field()  # 主演
    type = scrapy.Field()  # 类型
    address = scrapy.Field()  # 地区
    language = scrapy.Field()  # 语言
    time = scrapy.Field()  # 上映时间
    long = scrapy.Field()  # 时长
    score = scrapy.Field()  # 评分
    introduce = scrapy.Field()    # 介绍
    tags = scrapy.Field()         # 标签
    source = scrapy.Field()
