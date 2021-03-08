from typing import Optional

from view.AppWindow import AppWindow
from loguru import logger


def callback(video_url: Optional[str], audio_url: Optional[str]):
    print("callback")


if __name__ == '__main__':
    logger.info("starting app")
    app_window = AppWindow(callback=callback)
    app_window.show()
