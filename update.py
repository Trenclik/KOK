import requests
import zipfile
import os
import subprocess
import sys
import shutil

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

APP_VERSION = "v1.8.0"  # Replace this with your app's current version
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
        
        # Extract the zip file in a temporary directory
        with zipfile.ZipFile("update.zip", "r") as zip_ref:
            zip_ref.extractall("temp_dir")
        
        # Clean up the downloaded zip file
        os.remove("update.zip")
        
        # Copy the updated files to the root directory
        source_dir = os.path.join("temp_dir", f"KOK-{latest_version}")
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_dir)
                destination_path = os.path.join(".", relative_path)
                shutil.copy2(source_path, destination_path)
        
        # Remove the temporary directory
        shutil.rmtree("temp_dir")
        
        print("Update successful. Restarting the app...")
        # Restart the app using the new version
        python = sys.executable
        subprocess.call([python, "submain_app.py"])

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
        for i in range(1):
            print("No updates available. Running the app...")
            python = sys.executable
            subprocess.call([python, "submain_app.py"])

response = requests.get(GITHUB_REPO_URL, headers=HEADERS)
print(response.json())
print(response.status_code)  # Check the HTTP status code
