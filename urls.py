from handlers.foo import FooHandler
from tornado.web import StaticFileHandler
from settings import settings


url_patterns = [
    (r"/foo", FooHandler),
    (r"/media", StaticFileHandler, dict(path=settings['static_path'])),
]
