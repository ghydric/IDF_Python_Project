import os

print(os.getlogin())
print(os.stat('help.txt'))
print(os.getpid())
print(os.getppid())

import sys

print(sys.executable)
print(sys.getwindowsversion())
print(sys.hash_info)
print(sys.maxsize)
sys.setrecursionlimit(800)