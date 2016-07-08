import logging.config
import datetime
import tornado
import tornado.options
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.gen
import settings

__author__ = 'Zeus'


logging.config.dictConfig(settings.log_dict)
logger = logging.getLogger(__name__)


class Ping(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def initialize(self):
        logger.info('Request received {}'.format(self.request))

    def get(self, name_received=None):
        self.write('1')
        self.finish()

    def post(self, name_received=None):
        logger.info('Body {}'.format(self.request.body))
        self.write('1')
        self.finish()


def periodic():
    logger.info('<=======================> Tornado Periodic <=======================>')


def init():
    logger.info('<=======================> Tornado Init <=======================>')


def main():
    config = settings.config
    logger.info('<=======================> Server Start <=======================>')
    logger.info('Config: {}'.format(config))
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r'/ping', Ping),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(config['port'])
    tornado.ioloop.PeriodicCallback(periodic, 60000).start()
    tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=0), init)
    tornado.ioloop.IOLoop.instance().start()
    logger.info('<=======================> Server Stop <=======================>')


main()
