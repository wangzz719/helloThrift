# -*- coding: utf-8 -*-

import sys
sys.path.append('gen-py')

from hello import Hello

from thrift.protocol import TBinaryProtocol
from thrift.server import THttpServer


class HelloHandler:
    def hello_string(self, para):
        print para
        return para

    def hello_int(self, para):
        print para
        return para

    def hello_boolean(self, para):
        print para
        return para

    def hello_void(self):
        print 'void'

    def hello_null(self):
        print 'null'
        return 'null'


def run():
    handler = HelloHandler()
    processor = Hello.Processor(handler)
    pfacotry = TBinaryProtocol.TBinaryProtocolFactory()
    server = THttpServer.THttpServer(processor, ('127.0.0.1', 9090), pfacotry)
    print "starting server"
    server.serve()
    print "done"


if __name__ == '__main__':
    run()
