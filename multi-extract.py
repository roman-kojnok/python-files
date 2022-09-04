#!/usr/bin/python
import os
import re

#dir_path = os.getcwd()
dir_path = r'/home/m0rph3us/Videos/TUTORIALS/test/docs'
print(dir_path)

for file in os.listdir(dir_path):
    cur_path = os.path.join(dir_path, file)
    if os.path.isfile(cur_path):
        with open(cur_path, 'r') as f:
            for line in f:
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                  line)
                print(urls, file=open('links.txt', 'a'))

with open('links.txt', 'r') as f:
    text = f.read()
    patn = re.sub(r"[\([{''})\]]", "", text)
    print(patn, file=open('links.txt', 'w'))

output = ""
with open("links.txt") as file:
    for line in file:
        if not line.isspace():
            output += line

file = open("links.txt", "w")
file.write(output)
file.truncate()
file.close()
print("Done")

