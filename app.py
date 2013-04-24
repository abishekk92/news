from flask import Flask,render_template,request,Response
import json
from parser import parse
app=Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')	
@app.route('/query')
def query():
	keyword=request.args.get('keyword')
	response=parse(keyword)
	return Response(json.dumps(response),mimetype='application/json')


if __name__ == '__main__':
	app.run()
