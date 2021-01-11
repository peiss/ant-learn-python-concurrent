import gevent.monkey

gevent.monkey.patch_all()

import gevent
import blog_spider
import time

begin = time.time()
for url in blog_spider.urls:
    blog_spider.craw(url)
end = time.time()
print("single thread, cost = ", end - begin)

begin = time.time()
tasks = [gevent.spawn(blog_spider.craw, url) for url in blog_spider.urls]
gevent.joinall(tasks)
end = time.time()
print("gevent, cost = ", end - begin)
