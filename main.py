from flask import Flask, redirect, url_for, request
import subprocess
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def write_to_file(request):
    snippet = request.get_data(as_text=True)
    
    participant_code = request.headers["Submission-Code"]
    question_code = request.headers["Question-Code"]

    # TODO: P1 
    #Check if submission_code is valid
    #   i.e., Check for the participant is registered. (participant_code
    #          exists at our database/file)
    #   if participant is not registered return and do not execute the code.

    file_name = 'SUBMISSION_'+participant_code+'_'+question_code+'_'+'.py'

    with open(file_name, 'w+') as f:
        f.write(snippet)

    return file_name

def exe(file_to_execute):
    try:
        # TODO: P1
        # Only allow the process to run the code for 10 seconds max. 
        # If any code is trying to access it for more than 10 seconds, then kill the process
        # and return Timeout Error to the front end. 

        process=subprocess.Popen(['timeout' ,'10', 'python', file_to_execute], stdout=subprocess.PIPE)
        out,err = process.communicate()
        return out
    except Error as e:
        return e

@app.route('/submit',methods = ['POST'])
def login():
    if request.method == 'POST':
        file_to_execute = write_to_file(request)
        return exe(file_to_execute);

if __name__ == '__main__':
    app.run(use_reloader=False,debug =False, host='0.0.0.0',processes=os.cpu_count()-1, threaded=False)#TODO: Explore processes and threaded flag in depth. 
