#!/bin/bash
pyinstaller --onefile --hidden-import loguru --clean --name FragmentVideoDownloader main.py
