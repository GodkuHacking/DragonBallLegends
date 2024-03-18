# invert.py
# decrypts your game file so you can edit it!
# how to edit stuff: go to README.md in this folder to get more info.
# made by mindsetpro

import sys

arr = bytearray()
with open(sys.argv[1], "rb") as f:
    for b in f:
        arr += bytearray(b)
    for i in range(len(arr)):
        arr[i] = ~arr[i] + 256

with open(sys.argv[1], "wb") as f:
    f.write(arr)
