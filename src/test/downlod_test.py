import unittest

from src.FragmentVideoDownloader import FragmentVideoDownloader


class DownloadTest(unittest.TestCase):
    @staticmethod
    def test_simple_download():
        downloader: FragmentVideoDownloader = FragmentVideoDownloader(".",
                                                                      "",
                                                                      None, from_=0, to_=50)
        downloader.download()
        downloader.concat()
