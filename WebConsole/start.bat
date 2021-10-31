@echo off

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
    mkdir activation
    type nul > activation/batchactivated
    cls
    title Flask Server
    python3 main.py
)
