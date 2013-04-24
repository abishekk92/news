from flask import Flask,render_template,request,url_for
from parser import parse
app=Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')	
@app.route('/query')
def query():
	keyword=request.args.get('keyword')
	response=parse(keyword)
	return render_template('results.html',keyword=keyword,results=response)


if __name__ == '__main__':
	app.run()
