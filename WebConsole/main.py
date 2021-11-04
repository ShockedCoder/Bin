#!/bin/python

# I just followed a tutorial, so I don't know what half of this even means

import os
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import warnings; warnings.filterwarnings("ignore"); warnings.simplefilter("ignore")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>" # Personal Preference
        #return "<Task %r>" % self.id


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = Todo(content=task_content)

        if not task_content.replace(" ", "") == "":
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect("/")

            except:
                return "There was an issue adding your task"
        else:
            tasks = Todo.query.order_by(Todo.date_created).all()
            return render_template("index.html", tasks=tasks, title="No empty spaces, bro.")

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    if id != 0:
        task_to_delete = Todo.query.get_or_404(id)

        try:
            db.session.delete(task_to_delete)
            db.session.commit()
            return redirect("/")

        except:
            return "There was a problem deleting the provided task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        for task in tasks:
            db.session.delete(Todo.query.get(task.id))
            db.session.commit()
        return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["content"]
    else:
        return render_template("update.html", task=task)

    try:
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting the provided task"

"""
@app.route("/testlist")
def testlist():
    tasks = ["aple", "apple sauce", "peepeepoopooyeah", "go to sawcon", "banana"]
    for task in tasks:
        db.session.add(Todo(content=task))
    db.session.commit()
    return redirect("/")
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
