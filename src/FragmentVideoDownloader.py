import os
from typing import Optional
import requests
from loguru import logger
from requests import Response


class FragmentVideoDownloader:
    def __init__(self, path: str):
        self._path: str = path


    @logger.catch
    def download(self, video_url: Optional[str], audio_url: Optional[str],
                 to_: int, from_: int = 0):
        if video_url is None:
            raise ValueError("video_url is none")

        logger.info("starting downloading")

        for i in range(from_, to_):
            url = video_url.replace("{i}", str(i))
            name = url.split("/")[-1]
            with open(self._path + os.sep + name, "wb") as file:
                data: Response = requests.get(url, allow_redirects=True)
                file.write(data.content)

