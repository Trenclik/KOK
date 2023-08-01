import requests
import zipfile
import os
import subprocess
import sys






# btw tohle zatim nefachá










APP_VERSION = "1.0"  # Replace this with your app's current version
GITHUB_REPO_URL = "https://api.github.com/repos/Trenclik/KOK/releases/latest"

def check_for_updates():
    try:
        response = requests.get(GITHUB_REPO_URL)
        response.raise_for_status()
        release_data = response.json()
        latest_version = release_data["kok"]
        return latest_version
    except (requests.exceptions.RequestException, KeyError):
        pass
    return None

def update_app(latest_version):
    try:
        # Replace this URL with the direct download link to the zip file of the latest release
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
    if latest_version and latest_version != APP_VERSION:
        update_app(latest_version)
    else:
        print("No updates available. Running the app...")
        # Your app's main code goes here