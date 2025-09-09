import numpy as np

json_data = {"matrixSize": 200, "seed": 85}

def get_m_and_transpose(matrixSize, seed):
    np.random.seed(seed)  # Use the seed parameter
    M = np.random.random((matrixSize, matrixSize))  # Use matrixSize parameter
    M_transpose = np.transpose(M)
    return(M, M_transpose)

def get_trace(M, M_transpose):
    M_dot_M = np.dot(M, M)
    Mt_dot_M = np.dot(M_transpose, M)
    M_dot_M_dot_Mt_dot_M = np.dot(M_dot_M, Mt_dot_M)
    trace = np.trace(M_dot_M_dot_Mt_dot_M)
    return(trace)

# Call with actual parameters from json_data
M, M_transpose = get_m_and_transpose(json_data["matrixSize"], json_data["seed"])
trace_answer = get_trace(M, M_transpose)

print(f"Matrix size: {json_data['matrixSize']}")
print(f"Seed: {json_data['seed']}")
print(f"Trace result: {trace_answer}")