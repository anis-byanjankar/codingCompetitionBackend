from flask import Flask, redirect, url_for, request
import subprocess
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def write_to_file(snippet):
    with open('CodeSnippet.py', 'w+') as f:
        f.write(snippet)

def exe():
    process=subprocess.Popen(['timeout' ,'10', 'python', 'CodeSnippet.py'], stdout=subprocess.PIPE)
    out,err = process.communicate()
    print(str(err))
    return out
    proc = subprocess.Popen(["python","CodeSnippet.py"], stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    pid = proc.pid
    print(pid)
    #a = subprocess.check_output("python CodeSnippet.py",shell=True,timeout=10)
    return out

@app.route('/submit',methods = ['POST'])
def login():
    if request.method == 'POST':
        write_to_file(request.get_data(as_text=True))
        return exe();

if __name__ == '__main__':
    app.run(use_reloader=False,debug =False, host='0.0.0.0') 
