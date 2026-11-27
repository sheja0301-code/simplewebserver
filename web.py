from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Information</title>
</head>
<body>
    <h1>Welcome to My Student Webpage</h1>

    <h2>About Me</h2>
    <p>This is my first webpage using Python Simple Web Server.</p>

    <h2>Student Details</h2>
    <table border="1" cellpadding="10">
        <tr>
            <th>S.No</th>
            <th>Subject</th>
            <th>Technology</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Programming</td>
            <td>Python</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Web Development</td>
            <td>HTML</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Database</td>
            <td>MySQL</td>
        </tr>
    </table>

    <h2>My Learning Goals</h2>
    <ul>
        <li>Learn Python</li>
        <li>Learn HTML</li>
        <li>Understand Web Servers</li>
    </ul>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)

print("My webserver is running...")
httpd.serve_forever()

