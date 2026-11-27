from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<title>Top Programming Languages</title>
</head>
<body>
<table border="2" cellspacing="10" cellpadding="6">
<caption>Top 5 Programming Languages</caption>
<tr>
<th>S.No</th>
<th>Language</th>
<th>Uses</th>
</tr>
<tr>
<th>1</th>
<th>Python</th>
<th>Artificial Intelligence</th>
</tr>
<tr>
<th>2</th>
<th>Java</th>
<th>Application Development</th>
</tr>
<tr>
<th>3</th>
<th>JavaScript</th>
<th>Web Development</th>
</tr>
<tr>
<th>4</th>
<th>C++</th>
<th>Game Development</th>
</tr>
<tr>
<th>5</th>
<th>C</th>
<th>System Programming</th>
</tr>
</table>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)

print("my webserver is running...")
httpd.serve_forever()