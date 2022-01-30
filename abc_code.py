from flask import Flask
app=Flask(__name__)
@app.route('/try')
def _try():
	return '<h1>Try Successful</h1>'
if __name__=='__main__':
	app.run(debug=False,host="0.0.0.0")
	
