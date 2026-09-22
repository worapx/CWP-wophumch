#!/usr/bin/env python3
origin_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x + 2 for x in origin_array if x > 5]
print(f"Original array: {origin_array}")
print(f"New array: {new_array}")