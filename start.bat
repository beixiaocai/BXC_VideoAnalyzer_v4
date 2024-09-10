@echo off
setlocal
chcp 65001

tasklist | findstr /i "xcms.exe" >nul
if errorlevel 1 (
    echo xcms.exe is not running
) else (
    echo xcms.exe is running
	
	taskkill /IM xcms.exe /F
)

tasklist | findstr /i "Admin.exe" >nul
if errorlevel 1 (
    echo Admin.exe is not running
) else (
    echo Admin.exe is running
	taskkill /IM Admin.exe /F
)

tasklist | findstr /i "Analyzer.exe" >nul
if errorlevel 1 (
    echo Analyzer.exe is not running
) else (
    echo Analyzer.exe is running
	taskkill /IM Analyzer.exe /F
)

tasklist | findstr /i "MediaServer.exe" >nul
if errorlevel 1 (
    echo MediaServer.exe is not running
) else (
    echo MediaServer.exe is running
	taskkill /IM MediaServer.exe /F
)

tasklist | findstr /i "MediaManager.exe" >nul
if errorlevel 1 (
    echo MediaManager.exe is not running
) else (
    echo MediaManager.exe is running
	taskkill /IM MediaManager.exe /F
)


xcms.exe

endlocal
