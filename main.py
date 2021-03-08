from typing import Optional

from loguru import logger
import os
import sys
import platform

from src.FragmentVideoDownloader import FragmentVideoDownloader
from src.view.AppWindow import AppWindow


def callback(video_url: Optional[str], audio_url: Optional[str], from_: int, to_: int):
    downloader: FragmentVideoDownloader = FragmentVideoDownloader(CURRENT_DIR,
                                                                  video_url,
                                                                  audio_url, from_=int(from_), to_=int(to_))
    downloader.download()
    downloader.concat()


if __name__ == '__main__':
    if platform.system() == "Darwin":
        CURRENT_DIR = os.sep.join(sys.argv[0].split("/")[:-1])
    else:
        CURRENT_DIR = os.getcwd()
    logger.add(f'{CURRENT_DIR + os.sep}log{os.sep}DrillingEvents.log', format="{time} {level} {message}",
               rotation="1 MB", level="DEBUG")

    logger.info("starting app")
    app_window = AppWindow(callback=callback)
    app_window.show()
