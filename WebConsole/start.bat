@echo off

if not exist "main.db" (
    python3 activation/createdb.py
)

if exist "activation/batchactivated" (
    title Flask Server
    .venv\Scripts\activate.bat
    python3 main.py
) else (
    title Activation
    python3 -m pip install -U virtualenv
    virtualenv .venv
    .venv\Scripts\activate.bat
    python3 -m pip install -U flask flask-sqlalchemy
    type nul > activation/batchactivated
    cls
    title Flask Server
)
