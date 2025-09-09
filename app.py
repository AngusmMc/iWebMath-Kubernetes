from flask import Flask, jsonify, request
import requests
import numpy as np
import time

# Flask for flask obviously, request for getting POST data, jsonify for JSON formatting, numpy for maths, time for measuring execution time.


# create an instance of the Flask class and call it app
app = Flask(__name__)


# a decorator to define the location of the function of the web app
@app.route('/api/matrix-function', methods=['POST'])
def matrix_function(): # this function will be run when the URL ('/api/matrix-function) is accessed via a POST request
    """a function to ...
    """
    return jsonify({"message":"endpoint working"})

# {"matrixSize": 200, "seed": 1}

    # matrix_A can be the 200*200 random matrix
    A_transpose = np.transpose(A)



@app.route('/')
def hello():
    return ("Sup , this is working so far")



if __name__ == '__main__':
    app.run()
