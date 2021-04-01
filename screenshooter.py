import wget
import zipfile
import os
import subprocess
import pyautogui
import shutil
import time


class ScreenShooter:
    def __init__(self, url: str, branch_name: str) -> None:
        self.__url = url
        self.__branch_name = branch_name
        self.__download_url = url + f"/archive/refs/heads/{self.__branch_name}.zip"

    def download_dir(self) -> None:
        wget.download(self.__download_url, "./temp.zip")
        with zipfile.ZipFile("./temp.zip", 'r') as zip_ref:
            zip_ref.extractall("./temp")
        os.remove("./temp.zip")

    def take_screenshots(self) -> None:
        dirname = self.__url.split('/')[-1]
        path = f"./temp/{dirname}-{self.__branch_name}"
        pyfiles = [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames if
                   os.path.splitext(f)[1] == '.py']
        try:
            shutil.rmtree("./screenshots")
            os.mkdir("./screenshots")
        except Exception as e:
            print(e)
        for pyfile in pyfiles:
            subprocess.Popen(["notepad.exe", f"{pyfile}"])
            filename = pyfile.split('\\')[-1]
            time.sleep(1)
            pyautogui.click(x=50, y=10, clicks=2)
            time.sleep(1)
            screenshot = pyautogui.screenshot()
            screenshot.save(f"./screenshots/{filename}.screenshot.png")
            os.system("taskkill /IM notepad.exe")
        time.sleep(1)
        try:
            shutil.rmtree("./temp")
        except Exception as e:
            print(e)
