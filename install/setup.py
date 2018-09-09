import os

print("Installing dependencies...")
try:
    os.system("sh dependencies.sh")
except Exception:
    print("You do not have pip3 installed, trying to install with pip")
    os.system("sh retry.sh")
print("Done! Exiting.")