#!/usr/bin/env python

import SocketServer
import SimpleHTTPServer
import urllib2
import logging
from urlparse import urlparse


logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        logging.info(parsed_url)
        if parsed_url.netloc == "localhost":
            self.copyfile(urllib2.urlopen(self.path), self.wfile)


SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.ForkingTCPServer(('', 8080), Proxy)
httpd.serve_forever()
