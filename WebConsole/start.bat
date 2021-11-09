@echo off

if not exist "activation\batchactivated" (
    title Activation
    python3 -m pip install -U virtualenv
    virtualenv .venv
    .venv\Scripts\activate
    python3 -m pip install -r lethinigs.txt
    type nul > "activation\batchactivated"
    cls
)

if not exist "main.db" (
    .venv\Scripts\activate
    python3 activation/createdb.py
)

title Flask Server
.venv\Scripts\activate.bat
flask run
