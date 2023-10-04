import subprocess
from pip._internal import main as pipmain
pipmain(["install", "python"])
pipmain(['install', "requests"])
def execute_python_script(script_path):
    try:
        result = subprocess.run(["python", script_path], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error occurred while executing {script_path}.")
    except FileNotFoundError:
        print(f"Python executable not found. Make sure Python is installed and added to PATH.")
        input()
    except Exception as e:
        print(f"An error occurred: {e}")
        input()
if __name__ == "__main__":
    execute_python_script("update.py") 