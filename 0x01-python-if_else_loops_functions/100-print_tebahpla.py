#!/usr/bin/python3
for i in range(-122, -96):
    if i % 2 == 0:
        let = chr(i * -1)
    else:
        let = chr((i * -1) - 32)
    print("{}".format(let), end="")
