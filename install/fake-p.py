import subprocess
from pathlib import Path

# this this script that will modify the PIME Server to run on 64-bit Python

# Create venv

# Pip install the required packages
# Multilingual_ime & pyinstaller

# Path to the 64-bit Python interpreter (in the virtual environment)
venv_python_path = Path(__file__).parent / "venv" / "Scripts" / "python.exe"

# The script to run (can be passed as an argument)
script_to_run = "server.py"

# Execute the 64-bit Python interpreter with the specified script
subprocess.run([venv_python_path, script_to_run])
