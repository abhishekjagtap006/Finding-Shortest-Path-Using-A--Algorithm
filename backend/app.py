from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
# from crossdomain import *
import astar

app = Flask(__name__)
CORS(app)

# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
# app.config['CORS_HEADERS'] = 'Content-Type'

# cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})


@app.route("/", methods=['GET'])
@cross_origin(origin='*')
# @crossdomain(origin='*')
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# @cross_origin()
def home():
    return render_template('index.html')
# if _name_ == '_main_':
#    app.run()


@app.route('/a-star', methods=['POST', 'OPTIONS', 'GET'])
@cross_origin(origin='*')
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# @cross_origin(origin = "http://127.0.0.1:5000")
def astarRoute():
    if (request.method == 'POST'):
        print(request.form)
        print("Inside A-star")
        response = jsonify(astar.receive(request.form))
        req = request.form
        data = astar.receive(req)
        print(data)
        # Call A-star funtion here

        # response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    else:
        return 'ok'
