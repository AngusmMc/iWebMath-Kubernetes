from flask import Flask, jsonify, request
import requests
import numpy as np
import time

# Flask for flask obviously, request for getting POST data, jsonify for JSON formatting, numpy for maths, time for measuring execution time.


# create an instance of the Flask class and call it app
app = Flask(__name__)

def get_m_and_transpose(matrixSize, seed):
    np.random.seed(seed) 
    # Generate a 200x200 matrix of random floats
    M = np.random.random((matrixSize, matrixSize)) # matrix M is now a random matrix of 200 by 200 size
    M_transpose = np.transpose(M)
    return(M, M_transpose)

def get_trace(M, M_transpose):
    M_dot_M = np.dot(M,M)
    Mt_dot_M = np.dot(M_transpose, M)
    M_dot_M_dot_Mt_dot_M = np.dot(M_dot_M, Mt_dot_M)
    trace = np.trace(M_dot_M_dot_Mt_dot_M)
    return(trace)


def get_time_taken():
    start_time = time.time()
    M, M_transpose = get_m_and_transpose(json_data["matrixSize"], json_data["seed"])
    trace_answer = get_trace(M, M_transpose)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Trace result = {trace_answer} \n Calculation time taken: {time_taken} seconds or rounded: {time_taken:e} seconds")



# a decorator to define the location of the function of the web app
@app.route('/api/matrix-function', methods=['POST'])
def matrix_function(): # this function will be run when the URL ('/api/matrix-function) is accessed via a POST request
    """a function to ...
    """
    return jsonify({"message":"endpoint working"})


@app.route('/')
def hello():
    return ("Sup , this is working so far")



if __name__ == '__main__':
    app.run()
