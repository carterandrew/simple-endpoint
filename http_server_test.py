import json
import os
import tempfile
import unittest

import http_server

_PLAIN_HTML_RESPONSE = '<p>Hello, World</p>'


class TestHttpServer(unittest.TestCase):
  
    def setUp(self):
        http_server.app.testing = True
        self.app = http_server.app.test_client()

    def testHttpGetWithoutAcceptHeader(self):
        response = self.app.get('/')
        self.assertEqual(_PLAIN_HTML_RESPONSE, response.data)
  
    def testHttpGetWithAcceptHeader(self):
        response = self.app.get('/', headers={'accept': 'application/json'})
        self.assertEqual({'message': 'Good morning'}, json.loads(response.data))
  
    def testHttpGetWithAcceptHeaderNotJson(self):
        response = self.app.get('/', headers={'accept': 'text/html'})
        self.assertEqual(_PLAIN_HTML_RESPONSE, response.data)
        
    def testHttpPost(self):
        response = self.app.post('/')
        self.assertEqual(_PLAIN_HTML_RESPONSE, response.data)
        
    def testHttpGet404(self):
        response = self.app.get('/foo')
        self.assertEqual(404, response.status_code)
  
  
if __name__ == '__main__':
    unittest.main()