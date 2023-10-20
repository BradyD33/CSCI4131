from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

logList=[]
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
        newUrl = url.rsplit("?",1)
        url = contactLogParse(newUrl)
         
        
    if(url.count("#")>0):
        newUrl = url.rsplit("#")
        newUrl=newUrl[0]
        
    if(url.endswith("/") or url==("/main")):
        ourFile="static/html/mainpage.html"
    elif(url==("/testimonies")):
        ourFile="static/html/testimonials.html"
    elif(url==("/contact")):
        ourFile="static/html/contactform.html"
    else:
        ourFile="static/html/404.html"
    
    #if txt then open in default


    #else open in rb

    return (open(ourFile).read(), RequestHandler(url,))



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
def contactLogParse(submittedParameters):
    
    
    #practice list brady
    
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
    <link rel="stylesheet" href="../../static/css/styling.css">
  </head>
  <body>
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
                logFile.write("<td>"+keyValuePair[1]+"</td>\n")
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
        for keyValuePair in row:
            if(keyValuePair[0]=="help-option"):
                logFile.write("<td>"+keyValuePair[1]+"</td>\n")
                done=1
                break
        if(done==0):
            logFile.write("<td>" "</td>\n")
        for keyValuePair in row:
            if(keyValuePair[0]=="email-me" or keyValuePair[0]=="letter-me" or keyValuePair[0]=="call-me"):
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
    
            

    




    

    


def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ('', PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()
run()

