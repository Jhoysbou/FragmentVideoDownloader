import os
from typing import Optional
import requests
from loguru import logger
from requests import Response
from pathlib import Path


class FragmentVideoDownloader:
    def __init__(self, path: str,
                 video_url: Optional[str],
                 audio_url: Optional[str],
                 to_: int, from_: int = 0):
        self.to_ = to_
        self.from_ = from_
        self.audio_url = audio_url
        self.video_url = video_url
        self._path: str = path + os.sep + "temp"

    @logger.catch
    def download(self):
        if self.video_url is None:
            raise ValueError("video_url is none")

        logger.info("starting downloading")

        path = self._path + os.sep + "video"
        self._download(self.video_url, path, self.from_, self.to_)

        logger.info("finished downloading video files")

        if self.audio_url is not None:
            path = self._path + os.sep + "audio"
            self._download(self.audio_url, path, self.from_, self.to_)
            logger.info("finished downloading video files")

    def concat(self):
        self._prepare()
        logger.info("starting videos concatenation")
        os.system(
            f'ffmpeg -f concat -i {self._path + os.sep + "video" + os.sep + "videos.list"}'
            f' -c copy output.{self.video_url.split(".")[-1]} -y'
        )

    def _prepare(self):
        name = self.video_url.split("/")[-1]
        result = [f"file '{name.replace('{i}', str(i))}'" for i in range(self.from_, self.to_)]
        with open(self._path + os.sep + "video" + os.sep + "videos.list", "w") as file:
            file.write("\n".join(result))

    @staticmethod
    def _download(dirty_url, path, from_, to_):
        Path(path).mkdir(parents=True, exist_ok=True)
        for i in range(from_, to_):
            url = dirty_url.replace("{i}", str(i))
            name = url.split("/")[-1]
            logger.info(f"downloading {name}")

            with open(path + os.sep + name, "wb") as file:
                data: Response = requests.get(url, allow_redirects=True)
                file.write(data.content)
