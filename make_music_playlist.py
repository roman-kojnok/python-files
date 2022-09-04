#!/usr/bin/python
import os

path = os.getcwd()
dir = os.path.basename(path)
ext = ('mp3','ogg', 'flac', 'wma', 'wav')
# ext = ('avi','mp4', 'mov', 'wmv', 'mkv') #  replace for a video playlist

if os.path.exists(dir + '.m3u'):
    os.remove(dir + '.m3u')
    print("\n   ***   The playlist has been replaced successfully!   ***\n")
else:
    print("\n   ***   The playlist does not exist!   ***\n")

for file in os.listdir(path):
    if file.endswith(ext):
        f = open(dir + '.m3u', 'a', encoding='utf-8')
        f.write(file + '\n')
        print(file)
        f.close() 
