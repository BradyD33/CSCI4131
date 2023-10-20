from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
logList=[]
dummyList=[["user-name","Baka"], ["user-email","sus@baka.com"],["date-selection","2023-10-31"],["help-option","Change Phone Number"], ["letter-me","Letter"], ["submit-me","Submit"]]
first_load=0
# PUT YOUR GLOBAL VARIABLES AND HELPER FUNCTIONS HERE.
# It is not required, but is is strongly recommended that you write a function to parse form data out of the URL, and a second function for generating the contact log page html.
def contactLogParse(submittedParameters):
    

    print(submittedParameters)
    url = submittedParameters.pop(0)
    server(url)
    argList = submittedParameters[0].split("&")
    print(argList)
    keyList=["user-name","user-email","date-selection","help-option","call-me","email-me","letter-me","submit-me"]
    validKeyValue = [[]]
    
    i=1
    for param in argList:
        for key in keyList:
            if(param.startswith(key)):
                quick=param.rsplit("=",1)
                validKeyValue.append(quick)
                print("length:",len(validKeyValue))
                print("index",i)
                print("KeyValue",urllib.parse.unquote(validKeyValue[i][1]) )
                validKeyValue[i][1]=urllib.parse.unquote(validKeyValue[i][1])
                validKeyValue[i][1]=validKeyValue[i][1].replace("+", " ")
                i+=1
            else:
                
                validKeyValue[i-1][1]+"&"+param
                validKeyValue[i-1][1]=urllib.parse.unquote(validKeyValue[i-1][1])
                validKeyValue[i-1][1]=validKeyValue[i-1][1].replace("+", " ")
    validKeyValue.pop(0)   
    print("valid") 
    print( validKeyValue)
    print("thing")
    gen = generateLog(validKeyValue)
    return url
    
    


def generateLog(newContactSubmission):
    # logFile = open(r"C:\Users\Brady\OneDrive\Documents\CSCI4131\HW2\admin\contactlog\contactLog.html", "r")
    # currentData = logFile.read()
    # logFile.close()
    logList.append(newContactSubmission)
    logFile = open(r"C:\Users\Brady\OneDrive\Documents\CSCI4131\HW2\admin\contactlog\contactLog.html", "w")
    
    logFile.write(
        """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Contact Log</title>
    <link rel="stylesheet" href="../../main.css">
  </head>
  <body>
  <div class="navBar">

    <a href="/">Main Page</a>
    <a href="/testimonies">Testimonies</a>
    <a href="/contact">Contact Us</a>
  </div>
  <table>
    <tr>
        <th>Name</th>
        <th>Email</th>
        <th>Date</th>
        <th>Help Option</th>
        <th>Contact preference</th>
    </tr>
      
    """
    )
    for row in logList:
        logFile.write("<tr>\n")
        done=0
        for keyValuePair in row:
            if(keyValuePair[0]=="user-name"):
                logFile.write("<td>"+keyValuePair[1]+"</td>\n")
                done=1
                break
        if(done==0):
            logFile.write("<td>" "</td>\n")
        done=0
        for keyValuePair in row:
            if(keyValuePair[0]=="user-email"):
                logFile.write("<td><a href=mailto:${keyValuePair[1]}>"+keyValuePair[1]+"</a></td>\n")
                done=1
                break
        if(done==0):
            logFile.write("<td>" "</td>\n")
        done=0
        for keyValuePair in row:
            if(keyValuePair[0]=="date-selection"):
                logFile.write("<td>"+keyValuePair[1]+"</td>\n")
                done=1
                break
        if(done==0):
            logFile.write("<td>" "</td>\n")
        done=0
        for keyValuePair in row:
            if(keyValuePair[0]=="help-option"):
                logFile.write("<td>"+keyValuePair[1]+"</td>\n")
                done=1
                break
        if(done==0):
            logFile.write("<td>" "</td>\n")
        done=0
        for keyValuePair in row:
            if(keyValuePair[0]=="call-me" or keyValuePair[0]=="email-me" or keyValuePair[0]=="letter-me"):
                logFile.write("<td>"+keyValuePair[1]+"</td>\n")
                done=1
                break
        if(done==0):
            logFile.write("<td>" "</td>\n")
        logFile.write("</tr>\n")

    logFile.write(
        """ </table>
          </body>
    </html>"""
    )
    
            

    




    

    




def server(url):
    """
    url is a *PARTIAL* URL. If the browser requests `http://localhost:4131/contact?name=joe#test`
    then the `url` parameter will have the value "/contact?name=joe". So you can expect the PATH
    and any PARAMETERS from the url, but nothing else.

    This function is called each time another program/computer makes a request to this website.
    The URL represents the requested file.

    This function should return two strings in a list or tuple. The first is the content to return
    The second is the content-type.
    """
    ourFile= "lolRn"
    global first_load
    ######
    # TODO: Hey student! This is the function you need to change! Don't miss it!
    ######
    
    if(first_load==0):
        generateLog(dummyList)
        first_load+=1
    
    newUrl=url
    if(url.count("?")>0):
        newUrl = url.rsplit("?",1)
        url = contactLogParse(newUrl)
         
        
    if(url.count("#")>0):
        newUrl = url.rsplit("#")
        newUrl=newUrl[0]
   
    if(newUrl.endswith("/") or newUrl==("/main")):
        ourFile="static/html/mainpage.html"
    elif(newUrl==("/testimonies")):
        ourFile="static/html/testimonies.html"
    elif(newUrl==("/contact")):
        ourFile="static/html/contactform.html"
    elif(newUrl==("/admin/contactlog")):
        ourFile="admin/contactlog/contactLog.html"
    elif(newUrl.endswith(".png") or newUrl.endswith(".jpg")):
        ourFile=newUrl[1:]
    elif(newUrl.endswith(".css")):
        ourFile="static/css" + newUrl
    else:
        ourFile="static/html/404.html"
    # if(url.endswith("/") or url==("/main")):
    #     ourFile="static/html/mainpage.html"
    # elif(url==("/testimonies")):
    #     ourFile="static/html/testimonies.html"
    # elif(url==("/contact")):
    #     ourFile="static/html/contactform.html"
    # elif(url==("/admin/contactlog")):
    #     ourFile="admin/contactlog/contactLog.html"
    # elif(url.endswith(".png") or url.endswith(".jpg")):
    #     ourFile=url[1:]
    # elif(url.endswith(".css")):
    #     ourFile="static/css" + url
    # else:
    #     ourFile="static/html/404.html"
    

    fileType = ourFile.rsplit('.', 1)
    fileType = fileType[1]



    mimeType = "mimeType"
    if(fileType == "html"):
        mimeType="text/html"
        return open(ourFile).read(), mimeType
    if(fileType == "css"):
        mimeType="text/css"
        return open(ourFile).read(), mimeType
    if(fileType == "png"):
        mimeType="image/png"
        return open(ourFile, "rb").read(), mimeType
    if(fileType == "jpg"):
        mimeType="image/jpeg"
        return open(ourFile, "rb").read(), mimeType

 
    #YOUR CODE GOES HERE!

# You shouldn't need to change content below this. It would be best if you just left it alone.

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Call the student-edited server code.
        message, content_type = server(self.path)

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
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
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

def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ('', PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()
run()