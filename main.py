from flask import Flask, jsonify
from flask_cors import CORS

from file import Search, Download


app = Flask(__name__)
CORS(app)

@app.after_request
def response(response):
	response.headers['Content-Type'] = 'application/json'
	return response
	
@app.route("/")
def index():
	return jsonify(
		{
			"author": "Latip176",
			"data": {},
			"msg": "welcome to my api"
		}
	), 200
	
@app.route("/download/<id>")
def download(id):
	Main = Download()
	
	return jsonify(
		{
			"author": "Latip176",
			"data": Main.getData(id),
			"msg": "success"
		}
	), 200

@app.route("/search/<keyword>")
@app.route("/search/<keyword>/<page>")
def search(keyword, page=None):
	Main = Search()
	keyword = keyword.replace("%20", "+").replace(" ", "+")
	if page:
		return jsonify(
			{
				"author": "Latip176",
				"data": Main.search(keyword, f"&page={page}"),
				"msg": "success"
			}
		), 200
		
	return jsonify(
		{
			"author": "Latip176",
			"data": Main.search(keyword),
			"msg": "success"
		}
	), 200
	

@app.route("/search/")
@app.route("/download/")
def validation():
	return jsonify(
		{
			"author": "Latip176",
			"data": {},
			"msg": "data required!"
		}
	), 400
	

if __name__ == "__main__":
	app.run()