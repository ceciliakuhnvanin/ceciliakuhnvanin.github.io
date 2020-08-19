from flask import Flask
from flask import jsonify
import sonetos

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def getSoneto():
	return jsonify(sonetos.getSonetoJson())
   