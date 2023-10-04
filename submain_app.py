import subprocess
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
def execute_python_script(script_path):
    try:
        # Run the script and capture both stdout and stderr
        result = subprocess.run(["python", script_path], capture_output=True, text=True, check=True)
        # Print the stdout of the script
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
if __name__ == "__main__":
    execute_python_script("řešení.py")
    execute_python_script("kok.py")