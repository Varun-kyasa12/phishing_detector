@echo off
setlocal
set SCRIPT_DIR=%~dp0
set FLASK_DEBUG=false
"%SCRIPT_DIR%..\..\.tools\python-3.12.9\python.exe" "%SCRIPT_DIR%app.py"
