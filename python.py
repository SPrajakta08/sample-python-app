from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


@app.route('/fetch')
def facilityy():
	resp = "this is code"
	return resp
    
            


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
