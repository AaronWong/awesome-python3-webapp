import logging; logging.basicConfig(level=logging.INFO)
#logging  标准日志模板
#日志级别等级CRITICAL > ERROR > WARNING（默认） > INFO > DEBUG > NOTSET
#http://blog.csdn.net/zyz511919766/article/details/25136485/

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='UTF-8')
	
@asyncio.coroutine
def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8000)
	logging.info('server started at http://127.0.0.1:8000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()