from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
from model_interface import train, predict

app = Flask(__name__)
CORS(app)

# demo form
@app.route('/')
def hello():
	return '<form action = "/upload" method = "POST" enctype = "multipart/form-data"> <input type = "file" name = "file" /><input type = "submit"/></form> <form action = "/search" method = "POST" enctype = "multipart/form-data"> <input type = "text" name = "query" /><input type = "submit"/></form>'

# upload txt files
@app.route('/upload', methods=['POST'])
def upload():
	f = request.files['file']
	f.save(secure_filename(f.filename))
	train()
	return 'file uploaded successfully'

@app.route('/search', methods=['POST'])
def search():
	f = request.form.get('query')
	return predict()

if __name__ == '__main__':
	app.run(debug = True)