最后就是将写好的代码上传到各个服务器中。
ubuntu16系统为master端
ubuntu14位slave端

master端不爬取数据，只是运行redis，保存数据用的，
两个slave端则爬取数据保存到master端的redis数据库，为了能把数据保存到master，所以两个slave端代码settings中设置REDIS_HOST和REDIS_PORT要设置成master端的ip和端口。

执行方式：

通过runspider方法执行爬虫的py文件，爬虫（们）将处于等待准备状态：

scrapy runspider xunying_spider.py


在Master端的redis-cli输入push指令，参考格式：

lpush movieSpider:start_urls http://www.xunyingwang.com/movie/?page=1


爬虫获取url，开始执行。

注意：push指令中movieSpider:start_urls这个就是movieSpider中设置的redis_key，必须一致，不然爬虫不能运行。

截图示例：

左边的两个slave服务器处于等待状态，当右边的主服务push一个url入口，左边的两个便有一个获取到这个链接的request，然后返回更多的request到请求队列中，然后两个slave服务器便开始从队列获取请求开始爬了。


