from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi
 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine 
DBSession = sessionmaker(bind = engine) 
session = DBSession()


class webserverHandler(BaseHTTPRequestHandler):
	
	"""docstring for webserverHandler"""
	def do_GET(self):
		try:
			if self.path.endswith("/restaurants"):
				print "print  0000"
				restaurants = session.query(Restaurant).all()
				print "print  11111"
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				print "print  2222"
				output = ""
				output += "<html><body>"  
				output += " <a href='/restaurants/new' > Create a New Restaurant</a></p>"
				for restaurant in restaurants:
					output += restaurant.name
					output += "<a href='/restaurants/%s/edit'> Edit</a> " % restaurant.id
					output += " | <a href='/restaurants/%s/delete'> Delete</a> " % restaurant.id
					output += " </br>"  
				output += "</body></html>"
			
				self.wfile.write(output)
				print output
				return
			if self.path.endswith("/restaurants/new"):
				
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<h2> Add a New Restaurant</h2> " 

				output += "<form method='POST' enctype='multipart/form-data'  action='/restaurants/new' >"
				output += " <input name='restaurantname' type='text' placeholder=' New RestaurantName' > "
				output += " <input type='submit' value='Create'></form> "
				output += " </body></html>"
				print 'in the post 33333 '
				 
				self.wfile.write(output)
				print output
				return			
			if self.path.endswith("/edit"):
				
				restaurantId = self.path.split("/")[2]
				editRestaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
				if editRestaurant != []:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()
					output = ""
					output += "<html><body>"
					output += "<h2> Edit Restaurant</h2> " 

					output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit' >" % restaurantId
					output += " <input name='restaurantname' type='text' placeholder='%s' > " % editRestaurant.name
					output += " <input type='submit' value='Rename'></form> "
					output += " </body></html>"
				print 'in the edit get 33333 '
				 
				self.wfile.write(output)
				
				print output
				return			
		 	if self.path.endswith("/delete"):
				
				restaurantId = self.path.split("/")[2]
				deleteRestaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
				
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "<h2> Are you Sure you want to delete %s?</h2> " % deleteRestaurant.name 

				output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete' >" % restaurantId
				output += " <input type='submit' value='Delete'></form> "
				output += " </body></html>" 
				self.wfile.write(output)
				
				print output
				return			
		except:
			self.send_error(404, "File Not FOund %s" % self.path)

	def do_POST(self):
		try: 
			if self.path.endswith("/delete"):
				
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					print 'in the post 11111 '  
				restaurantId = self.path.split("/")[2] 
				deleteRestaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
				if deleteRestaurant != []: 
					session.delete(deleteRestaurant) 
					session.commit()

				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers() 
				return
			if self.path.endswith("/restaurants/new"):
				
				print 'in the post'
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				print 'in the post 0000 '
				if ctype == 'multipart/form-data':
					print 'in the post 11111 '
					fields=cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('restaurantname')
				print 'in the post 222222 '
				newRestaurant= Restaurant(name = messagecontent [0])
				session.add(newRestaurant)
				session.commit()

				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()
				print 'in the post 33333 '
				 
				return
			if self.path.endswith("/edit"):
				
				print 'in the post'
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				print 'in the post 0000 '
				if ctype == 'multipart/form-data':
					print 'in the post 11111 '
					fields=cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('restaurantname')
				print 'in the post 222222 '
				restaurantId = self.path.split("/")[2]
				print 'in the post 222222 11111'
				editRestaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
				print 'in the post 222222 22222'
				if editRestaurant != []:
					print 'in the post 222222 33333'
					editRestaurant.name =   messagecontent [0]
					print 'in the post 222222 44444'
					session.add(editRestaurant)
					print 'in the post 222222 5555'
					session.commit()

				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()
				print 'in the post 33333 '
				 
				return
			# self.send_response(301)
			# self.end_headers()
			# print 'in the post'
			# ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			# if ctype == 'multipart/form-data':
			# 	fields=cgi.parse_multipart(self.rfile, pdict)
			# 	messagecontent = fields.get('message')
			# print 'in the post 222222 '
			# output = ""
			# output += "<html><body>"
			# output += "<h2> Okey, how about this: </h2>"
			# print 'in the post 33333 '
			# output += "<h1> %s </h1>" % messagecontent [0]

		 # 	print 'in the post 4444 '
			# output += "<form method='POST' enctype='multipart/form-data' action='/hello' >"
			# output += " <h2> What woould you lime to say? </h2> "
			# output += "  <input name='message' type='text' > "
			# output += "<input type='submit' value='Submit'></form> "
			# output += "</body></html>"

			# self.wfile.write(output)
			# print output
			# return			

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
