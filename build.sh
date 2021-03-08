#!/bin/bash
pyinstaller --onefile --hidden-import loguru --icon=down-arrow.ico --clean --name FragmentVideoDownloader main.py
