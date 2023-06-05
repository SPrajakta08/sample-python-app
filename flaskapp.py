from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def facilityy():
	resp = "Done Successfully"
	return resp
    
            


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
