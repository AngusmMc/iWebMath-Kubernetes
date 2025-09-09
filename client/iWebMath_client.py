# Generate the parallel requests based on the ThreadPool Executor
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import sys
import time
import glob
import requests
import threading
import json
import os

# send http request
def call_large_matrices_multiplier_service(file):
    try:

        url = str(sys.argv[2])
        data = {}

        # file in this case refers to /client/input_matrices/_.txt 
        with open(file, "r") as j:
            mydata = json.load(j) # mydata is the json extracted from that file ie {"matrixSize":200 "seed":25}

        data['file'] = mydata # data['file'] is the mydata json from above
        id = mydata['seed'] # id is the seed value from the json
        data['id'] = str(id) # convert the seed value to a string
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)

        if response.ok:
            output = "Thread : {},  input file : {}, id:{} output:{}".format(threading.current_thread().getName(),
                                                                             file, data['id'], response.text)
            print(output)
        else:
            print("Error, response status:{}".format(response))

    except Exception as e:
        print("Exception in webservice call: {}".format(e))


def get_files_to_be_processed(input_folder):
    files = []
    for _file in glob.iglob(input_folder + "*.txt"):
        files.append(_file)
    return files


def main():
    # provide arguments-> input folder, url, number of threads
    if len(sys.argv) != 4:
        raise ValueError("Arguments list is wrong. Please use the following format: {} {} {} {}".
                         format("python clientScript.py", "<input_folder>", "<URL>", "<number_of_threads>"))

    input_folder = os.path.join(sys.argv[1], "")
    files = get_files_to_be_processed(input_folder)
    num_files = files.__len__()
    num_workers = int(sys.argv[3])
    start_time = time.time()
    # create a worker  thread  to invoke the requests in parallel
    with PoolExecutor(max_workers=num_workers) as executor:
        for _ in executor.map(call_large_matrices_multiplier_service,  files):
            pass
    elapsed_time = time.time() - start_time
    print("Total time spent: {}".format(
        elapsed_time))


if __name__ == "__main__":
    main()



