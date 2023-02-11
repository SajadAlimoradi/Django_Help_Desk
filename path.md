import os
from pathlib import Path

# dirname = os.path.dirname(__file__)
# print(dirname)
# filename = os.path.join(dirname, 'relative/path/to/file/you/want')
# print(filename)

# absolutepath = os.path.abspath(__file__)
# print(absolutepath)

# x = os.getcwd()

# x = Path(__file__).resolve().parent.parent
# print(x)
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
filename = os.path.join(BASE_DIR, 'sounds', 'winning.mp3')
print(filename)

# print(filename)
# fileDir = os.path.dirname(os.path.realpath('__file__'))
# print(fileDir)