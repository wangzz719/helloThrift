# -*- coding: utf-8 -*-

import sys
sys.path.append('gen-py')

from hello import Hello

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport


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
    transport = TSocket.TServerSocket('127.0.0.1', 9090)

    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "starting server"
    server.serve()
    print "done"


if __name__ == '__main__':
    run()
