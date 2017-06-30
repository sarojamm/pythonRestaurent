from flask import Flask
app = Flask(_name_)
@app.route('/')
@app.route('/hell0')

def HelloWorld():
	return "Hello World"

if __name__ == '__main__':
	app.debug = true
	app.run(host = '0.0.0.0', posrt = 5000)