#!/bin/python

# I just followed a tutorial, so I don't know what half of this even means

import os
import subprocess
from flask import Flask, render_template, redirect, request, jsonify


import importlib.util as imp
spec = imp.spec_from_file_location("charcrypt", f"{os.path.dirname(os.path.realpath(__file__))}/../charcrypt.py")
charcrypt = imp.module_from_spec(spec)
spec.loader.exec_module(charcrypt)


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

        try:
            command = request.form["command"]
            return redirect(f"/command/{charcrypt.encrypt(command)}")
        except Exception as excheep:
            return render_template("console.html", command=None, error=excheep)

    else:
        return render_template("console.html", command=None, error=None)


@app.route("/command/<string:cmd>")
def command(cmd):

    cmd = charcrypt.decrypt(cmd)

    try:
        command = subprocess.Popen(cmd.split("..__.."), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, error = command.communicate()
        return render_template("console.html", command=str(output)[:-1][2:].replace("\\\\", "\\"), error=str(error))
    
    except Exception as exceept:
        return render_template("console.html", command=None, error=exceept)
    
@app.route("/api/command/<string:cmd>")
def apicommand(cmd):

    cmd = charcrypt.decrypt(cmd)

    try:
        command = subprocess.Popen(cmd.split("..__.."), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, error = command.communicate()
        return jsonify(output=str(output)[:-1][2:].replace("\\\\", "\\"), error=str(error))
    
    except Exception as exceept:
        return jsonify(output=None, error=exceept)

@app.route("/test")
def test():
    return jsonify(apple="fuck you homie", cheese="you absolute cunt")



if __name__ == "__main__":
    app.run(debug=True, port=5001, host="127.42.0.69")
