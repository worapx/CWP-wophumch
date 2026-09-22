#!/usr/bin/env python3
import sys
message = sys.argv[1:]
if message:
    print(f"parameters: {len(message)}\n" + "\n".join(f"{s}: {len(s)}" for s in message))
else:
    print("none")