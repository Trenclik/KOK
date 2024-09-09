import os
import subprocess
import sys
import shutil
import re
import stat
import requests
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
ver = open("version", "r")
APP_VERSION = ver.read()  # Replace this with your app's current version
GITHUB_REPO_URL = "https://api.github.com/repos/Trenclik/KOK/releases"
HEADERS = {}

response = requests.get(GITHUB_REPO_URL, headers=HEADERS)
response.raise_for_status()
releases_data = response.json()
        
if releases_data:
    latest_release = releases_data[0]
    latest_version = latest_release["tag_name"]
verze = [latest_version]
res = [re.sub(r'^.', '', s) for s in verze]
verzebez_v = str(res[0])

