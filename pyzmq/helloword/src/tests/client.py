# -*- coding: utf-8 -*-

# Copyright (c) the Contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import time
from zmq.eventloop import ioloop

from core.connectors import CommandConnector

loop = ioloop.IOLoop().instance()


class MyCommandConnector(CommandConnector):

    def __init__(self, name, end_point):
        CommandConnector.__init__(self, name, end_point)
        self._stream.on_recv_stream(self._on_recv)

    def _on_recv(self, stream, msg):
        print('command executed: {0}'.format(msg[0]))


if __name__ == "__main__":
    server = 'tcp://127.0.0.1:5555'
    client = MyCommandConnector('MyCommandConnector', server)
    client.connect()

    data = 'hello word'

    client.send(data)

    loop.start()