# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XunyingRedisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class XunyingItem(scrapy.Item):
    name = scrapy.Field()         # 名字
    rename = scrapy.Field()       # 又名
    screenwriter = scrapy.Field() # 编剧
    director = scrapy.Field()     # 导演
    star = scrapy.Field()         # 主演
    type = scrapy.Field()         # 类型
    address = scrapy.Field()      # 地区
    language = scrapy.Field()     # 语言
    long = scrapy.Field()         # 时长
    douban_score = scrapy.Field() # 豆瓣评分
    IMDB_score = scrapy.Field()
    score = scrapy.Field()        # 临时存评分
    time = scrapy.Field()         # 上映时间
    introduce = scrapy.Field()    # 介绍
    tags = scrapy.Field()         # 标签
    source = scrapy.Field()       # 资源
