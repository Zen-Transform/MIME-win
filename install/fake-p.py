"""Module to run the PIME server using a 64-bit Python interpreter."""

import subprocess

# This script modifies the PIME Server to run on 64-bit Python.

# Create venv.

# Pip install the required packages.
# Multilingual_ime & pyinstaller.
# 1. `pyinstaller -F this_script.py`
# 2. Move the generated executable to the
#    PIME\python\python3 and rename it to python.exe.

# Path to the 64-bit Python interpreter (in the virtual environment)
VENV_PYTHON_PATH = (
    r"C:\Program Files (x86)\PIME\python\input_methods\MIME-win\venv\Scripts\python.exe"
)

# The script to run (can be passed as an argument)
SCRIPT_TO_RUN = r"C:\Program Files (x86)\PIME\python\server.py"
# Execute the 64-bit Python interpreter with the specified script
subprocess.run([VENV_PYTHON_PATH, SCRIPT_TO_RUN], check=True)
