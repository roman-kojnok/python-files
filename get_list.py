#!/usr/bin/python
import os

# Find files with a given list of filename extensions
d = os.getcwd()
extensions = [".jpg", ".jpeg", ".png"]
l = [f for f in os.listdir(d) if os.path.splitext(f)[1] in extensions]
print(l)
