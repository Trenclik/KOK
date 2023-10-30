import requests
import os
import subprocess
import sys
import shutil
import re
import stat

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

APP_VERSION = "v1.5.1"  # Replace this with your app's current version
GITHUB_REPO_URL = "https://api.github.com/repos/Trenclik/KOK/releases"
HEADERS = {
    "Authorization": "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" #NEMAZAT!!!!!! JE TO API KLÍČ!!!!!!
}

response = requests.get(GITHUB_REPO_URL, headers=HEADERS)
response.raise_for_status()
releases_data = response.json()
        
if releases_data:
    latest_release = releases_data[0]
    latest_version = latest_release["tag_name"]
verze = [latest_version]
res = [re.sub(r'^.', '', s) for s in verze]
verzebez_v = str(res[0])

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
        input()
    except KeyError as e:
        print("Error parsing response data:", e)
        input()

    return None

def update_app(latest_version):
    print("Updating...")
    try:
        download_url = f"https://github.com/Trenclik/KOK/archive/{latest_version}.zip"
        response = requests.get(download_url)
        response.raise_for_status()
        
        # Stáhne aktualizaci z githubu
        with open("update.zip", "wb") as f:
            f.write(response.content)

        shutil.unpack_archive("update.zip")

        os.rename(f"kok-{verzebez_v}","temp")

        # Define the root folder and the subfolder name
        root_folder = '.'  # You can change this to the path of your root folder
        subfolder_name = 'temp'  # Change this to the name of your subfolder

        # Get a list of files in the subfolder
        subfolder_path = os.path.join(root_folder, subfolder_name)
        subfolder_files = os.listdir(subfolder_path)

        # Iterate through the files in the subfolder
        for subfolder_file in subfolder_files:
            # Construct the full paths to the source and destination files
            source_file_path = os.path.join(subfolder_path, subfolder_file)
            destination_file_path = os.path.join(root_folder, subfolder_file)

            # Check if the destination file already exists and remove it
            if os.path.exists(destination_file_path):
                os.remove(destination_file_path)

            # Copy the source file to the root folder
            shutil.copy(source_file_path, destination_file_path)

            print(f'Replaced: {subfolder_file}')
        os.chmod("temp", stat.S_IWRITE)
        os.chmod("update.zip", stat.S_IWRITE)
        
        directory_path = "temp"

        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        for filename in os.listdir(directory_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                shutil.move(".", "jozi_fotky")
        os.rmdir("temp")
        os.remove("update.zip")
        print('File replacement completed.')

        #                                                restartuje v nový verzi
        #python = sys.executable
        #subprocess.call([python, "submain_app.py"])

    except Exception as e:
        print(f"Update failed: {e}")
        input()

if __name__ == "__main__":
    latest_version = check_for_updates()
    print("Latest version from GitHub:", latest_version, "\nCurrent app version:", APP_VERSION)

    if latest_version  != APP_VERSION:
        update_app(latest_version)
    else:
        for i in range(1):
            print("No updates available. Running the app...")
            python = sys.executable
            subprocess.call([python, "submain_app.py"])

response = requests.get(GITHUB_REPO_URL, headers=HEADERS)
print("HTTPS status code:",response.status_code)  # HTTP status code