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
        
        # Stáhne aktualizaci z githubu
        with open("update.zip", "wb") as f:
            f.write(response.content)
        
#                             složka se vytvoří pouze ke čtení, tu snad skapu nad tim

        os.mkdir("temp", mode=0o700)    #hotfix
        zdroj = "update.zip"
        destinace = "temp"
        shutil.unpack_archive(zdroj, destinace)
        print("temp 2")

        # odstraní zip
        os.remove("update.zip")
        print("delete zip")
        
        # zkopíruje z tempu do root složky

        root_folder = "."
        temp_folder = "temp"

        # dá všechny soubory složky do listu
        temp_files = os.listdir(temp_folder)

        # nevim nějaká pičovina co si vymyslelo gpt
        for temp_file in temp_files:
            temp_file_path = os.path.join(temp_folder, temp_file)
            root_file_path = os.path.join(root_folder, temp_file)

            # zkontroluje jestli existuje složka a pokud ano tak jí odstraní
            if os.path.exists(root_file_path):
                os.remove(root_file_path)

            # zkopíruje z tempu do root složky
            shutil.copy2(temp_file_path, root_folder)
            print(f"Replaced {temp_file} in the root folder.")

        print("All files replaced successfully.")
        
        # odstraní temp_dir
        shutil.rmtree("temp_dir")
        print("delete temp 1")

        shutil.rmtree("temp")
        print("delete temp 2")

        print("Update successful. Restarting the app...")
        # restartuje v nový verzi
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
print("HTTPS status code",response.status_code)  # HTTP status code