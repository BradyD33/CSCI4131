from http.server import BaseHTTPRequestHandler, HTTPServer

def server(url):
    """
    url is a *PARTIAL* URL. If the browser requests `http://localhost:4131/contact?name=joe`
    then the `url` parameter will have the value "/contact?name=joe". (so the schema and 
    authority will not be included, but the full path, any query, and any anchor will be included)

    This function is called each time another program/computer makes a request to this website.
    The URL represents the requested file.

    This function should return a string.
    """
    ourFile= "lolRn"
    ######
    # TODO: Hey student! This is the function you need to change! Don't miss it!
    ######
  
        
    newUrl=url
    if(url.count("?")>0):
        newUrl = url.rsplit("?")
        newUrl=newUrl[0]   
    if(url.count("#")>0):
        newUrl = url.rsplit("#")
        newUrl=newUrl[0]    
    if(newUrl.endswith("/") or newUrl==("/main")):
        ourFile="mainpage.html"
    elif(newUrl==("/testimonies")):
        ourFile="testimonials.html"
    elif(newUrl==("/contact")):
        ourFile="contactform.html"
    else:
        ourFile="404.html"
    

    return open(ourFile).read()
    

# You shouldn't need to change content below this. It would be best if you just left it alone.

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Call the student-edited server code.
        message = server(self.path)
        
        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # prepare the response object with minimal viable headers.
        self.protocol_version = "HTTP/1.1"
        # Send response code
        self.send_response(200)
        # Send headers
        # Note -- this would be binary length, not string length
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)
        return

def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ('', PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()
run()
