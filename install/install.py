import os
import sys
import subprocess

IME_NAME = "MIME-win"

if __name__ == "__main__":
    if sys.version_info < (3, 13):
        print(
            "Python version is insufficient. Python 3.13 or higher is required. current version: %s"
            % sys.version,
        )
        sys.exit(1)

    # Check if PIME is installed

    # TODO make rollback script?

    # Set the working directory for subsequent subprocess calls by using the 'cwd' parameter
    input_methods_dir = r"C:\Program Files (x86)\PIME\python\input_methods"

    # Install MIME-win from GitHub
    if not os.path.exists(input_methods_dir + "\\" + IME_NAME):
        print("Installing MIME-win...")
        subprocess.run(
            ["git", "clone", "https://github.com/Zen-Transform/MIME-win.git"],
            check=True,
            cwd=input_methods_dir,
        )
    else:
        print("MIME-win is already installed.")

    # Create a virtual environment at the specified path
    if not os.path.exists(f"C:\\Program Files (x86)\\PIME\\python\\input_methods\\{IME_NAME}\\venv"):
        print("Creating virtual environment...")
        command = [
            sys.executable,
            "-m",
            "venv",
        f"C:\\Program Files (x86)\\PIME\\python\\input_methods\\{IME_NAME}\\venv",
        ]
        subprocess.run(command, check=True)
    else:
        print("Virtual environment is already created.")

    # print("Activating virtual environment...")
    # # Activate the virtual environment
    # ACTIVATE_SCRIPT = (
    #     r"C:\Program Files (x86)"
    #     r"\PIME\python\input_methods"
    #     r"\MIME-win\venv\Scripts\activate.bat"
    # )
    # subprocess.run(
    #     f'cmd /k "{ACTIVATE_SCRIPT}"',
    #     check=True,
    #     shell=True
    # )


    print("Installing dependencies...")
    REQUIREMENTS_PATH = (
        "C:\\Program Files (x86)"
        "\\PIME\\python\\input_methods"
        "\\MIME-win\\requirements.txt"
    )
    PIP_INSTALL_CMD = [
        r"C:\Program Files (x86)\PIME\python\input_methods\MIME-win\venv\Scripts\pip.exe",
        "install",
        "-r",
        REQUIREMENTS_PATH
    ]
    subprocess.run(
        PIP_INSTALL_CMD,
        check=True
    )