import subprocess
import sys
import os
def install_dependencies():
    dependencies = ["requests", "pillow"]
    os.system(f'{sys.executable} -m pip install --upgrade pip')
    for package in dependencies:
        try:
            subprocess.run(["pip", "install","--upgrade" , package], check=True)
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}. Return Code: {e.returncode}")
            print(f"Error Output: {e.stderr}")
        except Exception as e:
            print(f"An error occurred while installing {package}: {e}")

def execute_python_script(script_path):
    try:
        # Get the full path to update.py
        script_directory = os.path.dirname(os.path.abspath(__file__))
        full_update_path = os.path.join(script_directory, script_path)

        # Run the script and capture both stdout and stderr
        result = subprocess.run(["python", full_update_path], capture_output=True, text=True, check=True)

        # Print the stdout of the script
        print(result.stdout)
    except FileNotFoundError:
        print(f"Python executable not found. Make sure Python is installed and added to PATH.")
        input()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {script_path}.")
        print(f"Return Code: {e.returncode}")
        print(f"Error Output: {e.stderr}")
        print("Current working directory:", os.getcwd())
        print("Full path to update.py:", full_update_path)
        input()
    except Exception as e:
        print(f"An error occurred: {e}")
        input()

if __name__ == "__main__":
    install_dependencies()
    execute_python_script("update.py")