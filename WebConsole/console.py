#!/bin/python

# I just followed a tutorial, so I don't know what most of this even means

import os
from flask import Flask, render_template, redirect, request, jsonify
from common import _pathdir


import importlib.util as imp
spec = imp.spec_from_file_location("charcrypt", f"{_pathdir}../charcrypt.py")
charcrypt = imp.module_from_spec(spec)
spec.loader.exec_module(charcrypt)

# TODO: Make my own jsonify(). Should be able to parse nested dictonaries.

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            cmd = request.form["command"]
            print(cmd)
            os.system(f"{cmd} > {_pathdir}/temporarytmp")
            with open(f"{_pathdir}/temporarytmp") as f:
                output = f.read()
            os.remove(f"{_pathdir}/temporarytmp")
            return render_template("console.html", output=output)
        
        except Exception as exceept:
            return render_template("console.html", output=exceept)
    else:
        return render_template("console.html", output=None)


@app.route("/api", methods=["POST", "GET"])
def api(): # Just print the output to a file and read output from there
    if request.method == "POST":

        try:
            cmd = request.data.decode()
            print(cmd)
            os.system(f"{cmd} > {_pathdir}/temporarytmp")
            with open(f"{_pathdir}/temporarytmp") as f:
                output = f.read()
            os.remove(f"{_pathdir}/temporarytmp")
            return jsonify(output=output)
        
        except Exception as exceept:
            return jsonify(output=exceept)

    else:
        return redirect("/")

@app.route("/api/test")
def test():
    return jsonify(apple="fuck you homie", cheese="you absolute cunt")

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
