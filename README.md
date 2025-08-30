# MIME-win

MIME-win is a Windows input method developed on top of [MIME](https://github.com/Zen-Transform/Multilingual-IME) and [PIME](https://github.com/EasyIME/PIME).

## Related Projects

* [Multilingual IME](https://github.com/Zen-Transform/Multilingual-IME) : The core of the Multilingual IME
* [MIME-web](https://github.com/Zen-Transform/MIME-web) : Input method editor as Chrome extension

## Installation

### Requirements

* Windows 10 or above
* Python >=3.13, <3.14

### 1. Step 1: Install Python 3.13 or above

* Download [Python 3.13](https://www.python.org/downloads/)
* Add Python to the environment variables
* (You can skip this if you already have Python 3.13)

### 2. Step 2: Install PIME

* 2.1 Download [PIME 1.3.0-stable](https://github.com/EasyIME/PIME/releases/tag/v1.3.0-stable)
* 2.2 Follow the setup process and select 新酷音輸入法.

### 3. Step 3: Install MIME-win

* 3.1 Download the MIME-win [install.py]()
* 3.2 Open a terminal as **administrator**
* 3.3 Run `python` to execute `install.py` in the terminal

    ```shell
    > cd [path to where install.py is located]
    
    > python install.py
    ```

* 3.4 Wait for the installation to complete
* 3.5 If you see **'Installation complete'** in the terminal, MIME-win has been installed successfully.

### 4. Final reminders

* 4.1 After installing **MIME-win**, 新酷音輸入法 will no longer be available. (This is because PIME has not been maintained for a long time and does not support Python 3.13.)

## Bug Report

Please report any issues [here](https://github.com/Zen-Transform/MIME-win/issues).

## License

MIME-win is release under [MIT License](https://github.com/Zen-Transform/MIME-win/blob/master/LICENSE.txt).
