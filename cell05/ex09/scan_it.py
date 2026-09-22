#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
    sys.exit()

keyword = sys.argv[1]
text = sys.argv[2]

matches = re.findall(re.escape(keyword), text)
count = len(matches)

if count == 0:
    print("none")
else:
    print(count)
