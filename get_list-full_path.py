#!/usr/bin/python
import glob
import os

# Find files with a given list of filename extensions with a full path
d = os.getcwd()
extensions = [".jpg", ".jpeg", ".png"]
l = [f for f in glob.glob(os.path.join(d, "**/*"), recursive=True) if os.path.splitext(f)[1] in extensions]
print(l)
