@echo off
REM Start PostgreSQL 18 database server
cd /d "C:\Program Files\PostgreSQL\18\bin"
echo Starting PostgreSQL 18...
pg_ctl.exe -D "C:\Program Files\PostgreSQL\18\data" -l logfile.log start
if %ERRORLEVEL% EQU 0 (
    echo PostgreSQL started successfully
) else (
    echo Failed to start PostgreSQL. Check the log file.
)
pause
