from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi
class webserverHandler(BaseHTTPRequestHandler):
	"""docstring for webserverHandler"""
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<h2> Hello Okey, how about this: </h2> " 

				output += "<form method='POST' enctype='multipart/form-data'  action='/hello' >"
				output += " <h2> What would you like to say? </h2> "
				output += "  <input name='message' type='text' > "
				output += "<input type='submit' value='Submit'></form> "
				output += "</body></html>"
			
				self.wfile.write(output)
				print output
				return
			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<h2> Okey, how about this: </h2>"
				output += "<h1> %s </h1>" % messagecontent [0]

				output += "<form method='POST' enctype='multipart/form-data' action='/hello' >"
				output += " <h2> What would you like to say? </h2> "
				output += "  <input name='message' type='text' > "
				output += "<input type='submit' value='Submit'></form> "
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return
		except:
			self.send_error(404, "File Not FOund %s" % self.path)
	def do_POST(self):
		try: 
			self.send_response(301)
			self.end_headers()
			print 'in the post'
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields=cgi.parse_multipart(self.rfile, pdict)
				messagecontent = fields.get('message')
			print 'in the post 222222 '
			output = ""
			output += "<html><body>"
			output += "<h2> Okey, how about this: </h2>"
			print 'in the post 33333 '
			output += "<h1> %s </h1>" % messagecontent [0]

		 	print 'in the post 4444 '
			output += "<form method='POST' enctype='multipart/form-data' action='/hello' >"
			output += " <h2> What woould you lime to say? </h2> "
			output += "  <input name='message' type='text' > "
			output += "<input type='submit' value='Submit'></form> "
			output += "</body></html>"

			self.wfile.write(output)
			print output
			return			

		except:
			pass
		
def main():
	try:
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print "web server running on port %s" % port
		server.serve_forever()
	except KeyboardInterrupt:
		print "^C entered, stopping web server ...."
		server.socket.close()

if __name__ == '__main__':
	main()
	
""" to start the webserver python mywebserver.py it should give message 
web server running on port 8080 
then navigate to 
localhost:8080/hello
127.0.0.1 - - [29/Jun/2017 19:07:37] "GET /hello HTTP/1.1" 200 -
<html><body>Hello ! </body></html> """
