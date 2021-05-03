from flask import Flask
from flask_restful import Api

app = Flask(__name__)

api = Api(app)


@app.route('/')
def hello_world():
    return 'Aplicacao Green'


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

