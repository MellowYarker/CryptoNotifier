import os

try:
    os.system("sh dependencies.sh")
except Exception:
    os.system("sh retry.sh")
