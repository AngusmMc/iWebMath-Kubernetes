from flask import Flask, jsonify, request
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





# when someone sends a POST request (sends data) to the URL: /api/matrix-function run the following function:
@app.route('/matrix', methods=['POST'])
def matrix_function():
    # get the json data from the http request body
    json_data = request.get_json() 



    start_time = time.time()
    # run the function with the matrix and seed values
    M, M_transpose = get_m_and_transpose(json_data["file"]["matrixSize"], json_data["file"]["seed"])
    trace_answer = get_trace(M, M_transpose)
    end_time = time.time()
    time_taken = end_time - start_time

    # information to be returned in json format
    return jsonify({"id":json_data["id"], "result": trace_answer, "processing_time": time_taken})


if __name__ == '__main__':
    app.run()
