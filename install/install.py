import os
import sys
import subprocess
from colorama import init, Fore, Style


if __name__ == "__main__":
    IME_NAME = "MIME_win"
    init()

    if sys.version_info < (3, 13):
        print(
            Fore.RED
            + "Python version is insufficient. Python 3.13 or higher is required. current version: %s"
            % sys.version,
            Fore.RESET,
        )
        sys.exit(1)

    # Check if PIME is installed

    # TODO make rollback script?

    # Set the working directory for subsequent subprocess calls by using the 'cwd' parameter
    input_methods_dir = r"C:\Program Files (x86)\PIME\python\input_methods"

    # Install MIME-win from GitHub
    if not os.path.exists(input_methods_dir + "\\" + IME_NAME):
        print(Fore.WHITE + "Installing MIME-win..." + Style.RESET_ALL)
        subprocess.run(
            [
                "git",
                "clone",
                "https://github.com/Zen-Transform/MIME-win.git",
                IME_NAME,
            ],
            check=True,
            cwd=input_methods_dir,
        )
    else:
        print(Fore.GREEN + "MIME-win is already installed." + Style.RESET_ALL)

    # Create a virtual environment at the specified path
    if not os.path.exists(
        f"C:\\Program Files (x86)\\PIME\\python\\input_methods\\{IME_NAME}\\venv"
    ):
        print(Fore.WHITE + "Creating virtual environment..." + Style.RESET_ALL)
        command = [
            sys.executable,
            "-m",
            "venv",
            f"C:\\Program Files (x86)\\PIME\\python\\input_methods\\{IME_NAME}\\venv",
        ]
        subprocess.run(command, check=True)
    else:
        print(Fore.GREEN + "Virtual environment is already created." + Style.RESET_ALL)

    print(Fore.WHITE + "Installing dependencies..." + Style.RESET_ALL)
    REQUIREMENTS_PATH = (
        "C:\\Program Files (x86)"
        "\\PIME\\python\\input_methods"
        f"\\{IME_NAME}\\requirements.txt"
    )
    PIP_INSTALL_CMD = [
        r"C:\Program Files (x86)\PIME\python\input_methods\MIME_win\venv\Scripts\pip.exe",
        "install",
        "-r",
        REQUIREMENTS_PATH,
    ]
    subprocess.run(PIP_INSTALL_CMD, check=True)
    print(Fore.GREEN + "Dependencies installed successfully." + Style.RESET_ALL)

    print(Fore.WHITE + "Creating Server..." + Style.RESET_ALL)
    # Skip creating server if old_python3 already exists
    old_python3_path = r"C:\Program Files (x86)\PIME\python\old_python3"
    if os.path.exists(old_python3_path):
        print(
            Fore.YELLOW
            + "Server already created. Skipping server creation steps."
            + Style.RESET_ALL
        )
    else:
        subprocess.run(
            [
                "move",
                r"C:\Program Files (x86)\PIME\python\python3",
                r"C:\Program Files (x86)\PIME\python\old_python3",
            ],
            shell=True,
            check=True,
        )

        subprocess.run(
            ["mkdir", r"C:\Program Files (x86)\PIME\python\python3"],
            shell=True,
            check=True,
        )

        subprocess.run(
            [
                "copy",
                r"C:\Program Files (x86)\PIME\python\input_methods\MIME_win\dist\fake-p.exe",
                r"C:\Program Files (x86)\PIME\python\python3\python.exe",
            ],
            shell=True,
            check=True,
        )
        subprocess.run(
            [
                "copy",
                r"C:\Program Files (x86)\PIME\python\input_methods\MIME_win\install\modify-server\server.py",
                r"C:\Program Files (x86)\PIME\python\server.py",
            ],
            shell=True,
            check=True,
        )
        print(Fore.GREEN + "Server created successfully." + Style.RESET_ALL)

    print(Fore.WHITE + "Registering MIME-win..." + Style.RESET_ALL)
    subprocess.run(
        ["Regsvr32", "C:\\Program Files (x86)\\PIME\\x64\\PIMETextService.dll"],
        check=True,
    )
    print(Fore.GREEN + "MIME-win registered successfully." + Style.RESET_ALL)
    print(Fore.WHITE + "\nInstallation complete!" + Style.RESET_ALL)
    print(
        Fore.WHITE
        + "MIME-win is now installed and ready to use as an input method."
        + Style.RESET_ALL
    )
    print(
        Fore.YELLOW
        + "IMPORTANT: A system restart is required to finish the installation "
        "and activate MIME-win." + Style.RESET_ALL
    )
    answer = input("Restart now? (y/n): ").strip().lower()
    if answer == "y":
        subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
    else:
        print(
            Fore.YELLOW
            + "Restart cancelled. Please restart your computer manually to complete "
            "the installation." + Style.RESET_ALL
        )
