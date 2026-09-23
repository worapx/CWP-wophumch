#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("none")
    sys.exit()

def downcase_all(string):
    return string.lower()

for i in range(1, len(sys.argv)):
    print(downcase_all(sys.argv[i]))
