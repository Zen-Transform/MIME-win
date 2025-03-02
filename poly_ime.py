
import os
import sys
import time
import json
import logging
import threading
import subprocess
from pathlib import Path
from logging.handlers import RotatingFileHandler

from multilingual_ime.key_event_handler import KeyEventHandler


from keycodes import *  # for VK_XXX constants
from textService import *


# 選單項目和語言列按鈕的 command ID
ID_SWITCH_LANG = 1
ID_SWITCH_SHAPE = 2
ID_SETTINGS = 3
ID_MODE_ICON = 4
ID_ABOUT = 5
ID_WEBSITE = 6
ID_GROUP = 7
ID_BUGREPORT = 8
ID_DICT_BUGREPORT = 9
ID_CHEWING_HELP = 10
ID_HASHED = 11
ID_MOEDICT = 13j
ID_DICT = 14
ID_SIMPDICT = 15
ID_LITTLEDICT = 16
ID_PROVERBDICT = 17
ID_OUTPUT_SIMP_CHINESE = 18
ID_USER_PHRASE_EDITOR = 19

# 按鍵內碼和名稱的對應
keyNames = {
    VK_ESCAPE: "Esc",
    VK_RETURN: "Enter",
    VK_TAB: "Tab",
    VK_DELETE: "Del",
    VK_BACK: "Backspace",
    VK_UP: "Up",
    VK_DOWN: "Down",
    VK_LEFT: "Left",
    VK_RIGHT: "Right",
    VK_HOME: "Home",
    VK_END: "End",
    VK_PRIOR: "PageUp",
    VK_NEXT: "PageDown",
}

# PolyKey Logger
log_file_path = Path(os.getenv("LOCALAPPDATA")) / "PIME" / "polykey" / "polykey.log"
temp_input_file_path = (
    Path(os.getenv("LOCALAPPDATA")) / "PIME" / "polykey" / "pimeinput.json"
)
temp_output_file_path = (
    Path(os.getenv("LOCALAPPDATA")) / "PIME" / "polykey" / "pimeoutput.json"
)

if not log_file_path.exists():
    log_file_path.parent.mkdir(parents=True, exist_ok=True)
    log_file_path.write_text("")
if not temp_input_file_path.exists():
    temp_input_file_path.parent.mkdir(parents=True, exist_ok=True)
    temp_input_file_path.write_text("")
if not temp_output_file_path.exists():
    temp_output_file_path.parent.mkdir(parents=True, exist_ok=True)
    temp_output_file_path.write_text("")

LOG_MODE = logging.DEBUG

logger = logging.getLogger(f"{__name__}")
logger.setLevel(LOG_MODE)

file_handler = RotatingFileHandler(
    log_file_path, encoding="utf-8", maxBytes=1024 * 1024, backupCount=1
)
file_handler.setLevel(LOG_MODE)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.info("PolyKey Logger Initialized")


# Host Test Path
host_test_path = Path(__file__).parent / "T" / "host_test.py"

script_path = Path(__file__)


class PolyTextService(TextService):
    def __init__(self, client):
        TextService.__init__(self, client)
        self.curdir = os.path.abspath(os.path.dirname(__file__))
        self.icon_dir = os.path.join(self.curdir, "icons")
        self.my_keyeventhandler = KeyEventHandler(verbose_mode=True)

        # States
        self.langMode = None

        # Variables
        self.composition_string = ""
        self._run_timer = None

        self.last_composition_string = ""

        self.customizeUI(
            candFontName="MingLiu", candFontSize=16, candPerRow=1, candUseCursor=True
        )

        self.last_seqNum = None

    def onActivate(self):
        TextService.onActivate(self)
        logger.info("PolyKey Activated")

    def addLangButtons(self):
        # TODO
        pass

    def removeLangButtons(self):
        # TODO
        pass

    def onDeactivate(self):
        logger.info("PolyKey Deactivated")
        # TODO
        pass

    def setAutoLearn(self, autoLearn):
        # TODO
        pass

    def onCompositionTerminated(self, forced):
        self.my_keyeventhandler.handle_key("enter")

    def convertKeyEvent(self, keyEvent):
        charCode = keyEvent.charCode
        keyCode = keyEvent.keyCode
        charStr = chr(charCode)

        key_event = ""
        if keyCode == VK_RETURN:
            key_event = "enter"
        elif keyCode == VK_LEFT:
            key_event = "left"
        elif keyCode == VK_RIGHT:
            key_event = "right"
        elif keyCode == VK_UP:
            key_event = "up"
        elif keyCode == VK_DOWN:
            key_event = "down"
        elif keyCode == VK_BACK:
            key_event = "backspace"
        elif keyCode == VK_DELETE:
            key_event = "delete"
        elif keyCode == VK_ESCAPE:
            key_event = "esc"
        elif keyCode == VK_SPACE:
            key_event = "space"
        elif keyCode == VK_SHIFT:
            key_event = "shift"
        elif keyCode == VK_CONTROL:
            key_event = "ctrl"
        else:
            key_event = charStr

        return key_event

    def updateUI(self):
        # Get Result from Test Side
        logger.info("Updating UI")
        if self.my_keyeventhandler.in_selection_mode:
            self.setShowCandidates(True)
            self.setCandidateList(self.my_keyeventhandler.candidate_word_list)
            self.setCandidateCursor(self.my_keyeventhandler.selection_index)
        else:
            if self.my_keyeventhandler.get_composition_string() == "":
                self.setCommitString(self.last_composition_string)

            self.setShowCandidates(False)
            self.setCompositionString(self.my_keyeventhandler.get_composition_string())
            self.setCompositionCursor(self.my_keyeventhandler.composition_index)
            self.last_composition_string = (
                self.my_keyeventhandler.get_composition_string()
            )

    def slow_updateUI(self):
        self.my_keyeventhandler.slow_handle()
        self.updateUI()

    def onKeyDown(self, keyEvent):
        # if self._run_timer != None:
        #     self._run_timer.cancel()

        key_event = self.convertKeyEvent(keyEvent)
        logger.info(f"key_event: {key_event}")

        # if key_event in ["enter", "left", "right", "down", "up", "esc"]:
        #     self.my_keyeventhandler.handle_key(key_event)
        # else:
        # if keyboard.is_pressed("ctrl") and key_event != "ctrl":
        #     self.my_keyeventhandler.handle_key("©" + key_event)
        # elif keyboard.is_pressed("shift") and key_event != "shift":
        #     self.my_keyeventhandler.handle_key(key_event.upper())
        # else:
        # self.my_keyeventhandler.handle_key(key_event)

        # self._run_timer = threading.Timer(0.25, self.slow_handle)
        # self._run_timer.start()
        self.my_keyeventhandler.handle_key(key_event)
        self.my_keyeventhandler.slow_handle()
        self.updateUI()

        return True

    def filterKeyUp(self, keyEvent):
        return True

    def onKeyUp(self, keyEvent):
        return True

    def filterKeyDown(self, keyEvent):
        return True
