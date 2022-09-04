#!/usr/bin/python
import re

with open("some_file_with_url.txt") as file:
    for line in file:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
        print(urls)
