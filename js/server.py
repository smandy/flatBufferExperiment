import cyclone.web
import sys
import cyclone.websocket
from twisted.internet import reactor
from twisted.python import log

if __name__ == "__main__":
    
    application = cyclone.web.Application([
        (r'/(.*)' , cyclone.web.StaticFileHandler, { 'path' : '.' } ),
    ])
    log.startLogging(sys.stdout)
    reactor.listenTCP(8889,
                      application,
                      interface="127.0.0.1")
    
    reactor.run()
