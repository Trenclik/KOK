import requests
import zipfile
import os
import subprocess
import sys
import shutil

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

APP_VERSION = "v1.11.0"  # Replace this with your app's current version
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
            print("extrakt do temp") #                             složka se vytvoří pouze ke čtení, tu snad skapu nad tim

        os.mkdir("temp", mode=0o700)
        zdroj = "temp_dir"
        destinace = "temp"
        shutil.copy(zdroj, destinace)
        print("temp 2")

        # Clean up the downloaded zip file
        os.remove("update.zip")
        print("delete zip")
        
        # Copy the updated files to the root directory

        # Define the root and temporary folder paths
        root_folder = "."
        temp_folder = "temp"

        # List files in the temporary folder
        temp_files = os.listdir(temp_folder)

        # Iterate through the temporary files
        for temp_file in temp_files:
            temp_file_path = os.path.join(temp_folder, temp_file)
            root_file_path = os.path.join(root_folder, temp_file)

            # Check if the file exists in the root folder
            if os.path.exists(root_file_path):
                # Remove the existing file in the root folder
                os.remove(root_file_path)

            # Copy the file from the temporary folder to the root folder
            shutil.copy2(temp_file_path, root_folder)
            print(f"Replaced {temp_file} in the root folder.")

        print("All files replaced successfully.")
        
        # Remove the temporary directory
        shutil.rmtree("temp_dir")
        print("delete temp 1")

        shutil.rmtree("temp")
        print("delete temp 2")

        print("Update successful. Restarting the app...")
        # Restart the app using the new version
        python = sys.executable
        subprocess.call([python, "submain_app.py"])

    except Exception as e:
        print(f"Update failed: {e}")

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
#print(response.json())
print(response.status_code)  # Check the HTTP status code