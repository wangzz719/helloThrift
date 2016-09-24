# -*- coding: utf-8 -*-

import sys
sys.path.append('gen-py')

from hello import Hello

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    transport = TSocket.TSocket('127.0.0.1', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Hello.Client(protocol)
    transport.open()

    print client.hello_string('string')
    print client.hello_int(123)
    print client.hello_boolean(True)
    print client.hello_void()
    print client.hello_null()
    transport.close()

if __name__ == '__main__':
    main()
