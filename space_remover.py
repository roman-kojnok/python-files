import os

path = os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
    # os.rename(filename, filename.replace(" ", "-").lower())
    os.rename(filename, filename.replace(" . ", "-"))
