@echo off
setlocal enabledelayedexpansion

:: Define the Python version and download URL
set PYTHON_VERSION=3.11.0
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

:: Define the destination file paths
set CURL_URL=https://curl.se/windows/dl-7.78.0/curl-7.78.0-win64-mingw.zip
set CURL_ZIP=curl-7.78.0-win64-mingw.zip
set DESTINATION_PYTHON=python-%PYTHON_VERSION%-amd64.exe
set DESTINATION_CURL=curl.exe

:: Download and extract curl
curl -o "%CURL_ZIP%" "%CURL_URL%"
if not exist "%CURL_ZIP%" (
    echo Error: Downloading curl failed. Please check your internet connection and try again.
    goto :EOF
)
echo Extracting curl...
powershell -command "Expand-Archive -Path .\%CURL_ZIP% -DestinationPath .\curl"
if errorlevel 1 (
    echo Error: Extracting curl failed.
    goto :EOF
)

:: Install Python
echo Installing curl...
copy "curl\curl.exe" "%DESTINATION_CURL%" /Y

:: Cleanup the downloaded curl files
del "%CURL_ZIP%"
rmdir /s /q "curl"

:: Download Python installer
echo Downloading Python %PYTHON_VERSION%...
curl -o "%DESTINATION_PYTHON%" "%PYTHON_URL%"
if not exist "%DESTINATION_PYTHON%" (
    echo Error: Downloading Python failed. Please check your internet connection and try again.
    goto :EOF
)

:: Install Python
echo Installing Python %PYTHON_VERSION%...
start /wait "" "%DESTINATION_PYTHON%" /quiet
if errorlevel 1 (
    echo Error: Python installation failed.
    goto :EOF
)

:: Cleanup the downloaded Python installer
del "%DESTINATION_PYTHON%"

echo Python %PYTHON_VERSION% and curl have been successfully installed.
goto :EOF