
## EX01 Developing a Simple Webserver
## Date:25.11.2026

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
sheja.py
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<title>Simplewebserver</title>
</head>
<body align="center">
<h1>Shejashri L J</h1>
<h2>26016939</h2>

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
```

## OUTPUT:

![alt text](<Screenshot 2026-11-28 112841.png>)

![alt text](<Screenshot 2026-11-27 143927.png>)



## RESULT:
The program for implementing simple webserver is executed successfully.
