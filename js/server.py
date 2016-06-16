import cyclone.web
import sys
import cyclone.websocket
from twisted.internet import reactor
from twisted.python import log
import json

"""
      0                   1                   2                   3
      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
     +-+-+-+-+-------+-+-------------+-------------------------------+
     |F|R|R|R| opcode|M| Payload len |    Extended payload length    |
     |I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
     |N|V|V|V|       |S|             |   (if payload len==126/127)   |
     | |1|2|3|       |K|             |                               |
     +-+-+-+-+-------+-+-------------+xbse - - - - - - - - - - - - - - - +
     |     Extended payload length continued, if payload len == 127  |
     + - - - - - - - - - - - - - - - +-------------------------------+
     |                               |Masking-key, if MASK set to 1  |
     +-------------------------------+-------------------------------+
     | Masking-key (continued)       |          Payload Data         |
     +-------------------------------- - - - - - - - - - - - - - - - +
     :                     Payload Data continued ...                :
     + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
     |                     Payload Data continued ...                |
     +---------------------------------------------------------------+
"""


class ThingHandler( cyclone.web.RequestHandler):
    def initialize(self, path ):
        print "Think %s" % path
        self.path = path

    def get(self):
        print "Getting %s" % self.request
        self.set_header('Content-type', 'application/octet-stream')
        self.write(open('things.fb', 'r').read())
        return True

class WebSocketHandler(cyclone.websocket.WebSocketHandler):
    def initialize(self, *args, **kwargs):
        print "Websocket handler %s %s" % (str(args), str(kwargs))
    
    def connectionMade(self):
        log.msg("ws opened %s" % self)
        #print dir(self)
        #self.sendMessage( (open('things.fb', 'rb').read()) , isBinary = True)
        #self.sendMessage("Woot")

    def messageReceived(self, x):
        print "Got %s" % x
        self.sendMessage( (open('things.fb', 'rb').read()) , isBinary = True)

    def connectionLost(self,x):
        log.msg("ws closed %s " % x)
    
if __name__ == "__main__":
    application = cyclone.web.Application([
        (r'/ws' , WebSocketHandler, { 'path' : '.' } ),
        (r'/things.fb', ThingHandler, { 'path' : '.' } ),
        (r'/(.*)' , cyclone.web.StaticFileHandler, { 'path' : '.' } )
    ], debug = True)
    log.startLogging(sys.stdout)
    reactor.listenTCP(8889,
                      application,
                      interface="127.0.0.1")
    reactor.run()
