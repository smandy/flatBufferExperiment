import cyclone.web
import sys
import cyclone.websocket
from twisted.internet import reactor
from twisted.python import log

class ThingHandler( cyclone.web.RequestHandler):
    def initialize(self, path ):
        print "Think %s" % path
        self.path = path

    def get(self):
        print "Getting %s" % self.request
        self.set_header('Content-type', 'application/octet-stream')
        self.write(open('things.fb', 'r').read())
        return True


if __name__ == "__main__":
    application = cyclone.web.Application([
        (r'/things.fb', ThingHandler, { 'path' : '.' } ),
        (r'/(.*)' , cyclone.web.StaticFileHandler, { 'path' : '.' } )
    ], debug = True)
    log.startLogging(sys.stdout)
    reactor.listenTCP(8889,
                      application,
                      interface="127.0.0.1")
    reactor.run()
