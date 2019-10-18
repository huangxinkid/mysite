# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import datetime
from threading import Thread

from tornado.web import RequestHandler
from tornado.options import define, options
from tornado.websocket import WebSocketHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.render("chat_index.html")


class ChatHandler(WebSocketHandler):

    users = set()  # 用来存放在线用户的容器

    def open(self):
        self.users.add(self)  # 建立连接后添加用户到容器中
        for u in self.users:  # 向已在线用户发送消息
            u.write_message(u"[%s]-[%s]-进入聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def on_message(self, message):
        for u in self.users:  # 向在线用户广播消息
            u.write_message(u"[%s]-[%s]-说：%s" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    def on_close(self):
        self.users.remove(self) # 用户关闭连接后从容器中移除用户
        for u in self.users:
            u.write_message(u"[%s]-[%s]-离开聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/chat', ChatHandler)
        ]
        settings = {"template_path": "./websocket_server"}
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.current().start()


# class WebThread(Thread):
#     def __init__(self):
#         Thread.__init__(self, name='WebThread')

#     def run(self):
#         application = Application()

#         http_server = tornado.httpserver.HTTPServer(application)
#         http_server.listen(8080)
#         tornado.ioloop.IOLoop.current().start()


# if __name__ == "__main__":
#     webThread = WebThread()
#     webThread.daemon = True
#     webThread.start()
#     print('main threading')
#     while True:
#         pass
