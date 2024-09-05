import subprocess
import os
from sys import executable
script_directory = os.path.dirname(os.path.abspath(__file__))
script_path = "update.py"
dependencies = ["requests", "pillow","ttkthemes"]
os.system(f'{executable} -m pip install --upgrade pip')
for package in dependencies:
    try:
        subprocess.run(["pip", "install","--upgrade" , package], check=True)
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}. Return Code: {e.returncode}")
        print(f"Error Output: {e.stderr}")
    except Exception as e:
        print(f"An error occurred while installing {package}: {e}")
try:
    # Run the script and capture both stdout and stderr
    result = subprocess.run(["python", script_path], capture_output=True, text=True, check=True)
    print(result.stdout)
except FileNotFoundError:
    print(f"Python executable not found. Make sure Python is installed and added to PATH.")
    input()
except subprocess.CalledProcessError as e:
    print(f"Error occurred while executing {script_path}.")
    print(f"Return Code: {e.returncode}")
    print(f"Error Output: {e.stderr}")
    input()
except Exception as e:
    print(f"An error occurred: {e}")
    input()