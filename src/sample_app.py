import tornado.ioloop
import tornado.web

version=0.0.1
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world! Welcome to the version: " + str(version))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()