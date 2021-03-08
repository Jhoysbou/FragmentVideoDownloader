import unittest

from src.FragmentVideoDownloader import FragmentVideoDownloader


class DownloadTest(unittest.TestCase):
    def test_simple_download(self):
        downloader: FragmentVideoDownloader = FragmentVideoDownloader(".")
        downloader.download("", None, 0, 281)
        