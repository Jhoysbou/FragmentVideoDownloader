from typing import Optional

from loguru import logger

from src.FragmentVideoDownloader import FragmentVideoDownloader
from src.view.AppWindow import AppWindow


def callback(video_url: Optional[str], audio_url: Optional[str], from_: int, to_: int):
    downloader: FragmentVideoDownloader = FragmentVideoDownloader(".",
                                                                  video_url,
                                                                  audio_url, from_=from_, to_=to_)
    downloader.download()
    downloader.concat()


if __name__ == '__main__':
    logger.info("starting app")
    app_window = AppWindow(callback=callback)
    app_window.show()
