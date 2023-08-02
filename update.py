import requests
import zipfile
import os
import subprocess
import sys

APP_VERSION = "v1.2.0"  # Replace this with your app's current version
GITHUB_REPO_URL = "https://api.github.com/repos/Trenclik/KOK/releases"
HEADERS = {
    "Authorization": "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" #NEMAZAT!!!!!! JE TO API KLÍČ!!!!!!
}

def check_for_updates():
    try:
        response = requests.get(GITHUB_REPO_URL, headers=HEADERS)
        response.raise_for_status()
        releases_data = response.json()
        
        if releases_data:
            latest_release = releases_data[0]
            latest_version = latest_release["tag_name"]
            return latest_version

    except requests.exceptions.RequestException as e:
        print("Error occurred during API request:", e)
    except KeyError as e:
        print("Error parsing response data:", e)

    return None

def update_app(latest_version):
    try:
        download_url = f"https://github.com/Trenclik/KOK/archive/{latest_version}.zip"
        response = requests.get(download_url)
        response.raise_for_status()
        
        # Save the downloaded zip file
        with open("update.zip", "wb") as f:
            f.write(response.content)
        
        # Extract the zip file
        with zipfile.ZipFile("update.zip", "r") as zip_ref:
            zip_ref.extractall(".")
        
        # Clean up the downloaded zip file
        os.remove("update.zip")
        
        print("Update successful. Restarting the app...")
        # Restart the app using the new version
        python = sys.executable
        subprocess.call([python, "main_app.py"])
        sys.exit(0)
    except Exception as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    latest_version = check_for_updates()
    print("Latest version from GitHub:", latest_version)
    print("Current app version:", APP_VERSION)
    latest_version = check_for_updates()
    if latest_version and latest_version != APP_VERSION:
        update_app(latest_version)
    else:
        print("No updates available. Running the app...")
        # Your app's main code goes here

response = requests.get(GITHUB_REPO_URL, headers=HEADERS)
print(response.json())
print(response.status_code)  # Check the HTTP status code