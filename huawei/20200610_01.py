# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    m = int(sys.stdin.readline().strip())
    char_list = sys.stdin.readline().strip().split("-")

    first = char_list[0]
    new = "".join(char_list[1:])
    output = []

    i = 0
    while new:
        output.append(new[0: m])
        i += m
        new = new[i:]
    output_list = []
    for out in output:
        small = 0
        big = 0
        new_ch = ""
        for ch in out:
            if "a" <= ch <= "z":
                small += 1
            if "A" <= ch <= "Z":
                big += 1
        if small > big:
            for ch in out:
                if "a" <= ch <= "z":
                    new_ch += ch.upper()
        elif small < big:
            for ch in out:
                if "A" <= ch <= "Z":
                    new_ch += ch.lower()
        else:
            new_ch = out

        output_list.append(new_ch)
    output_list.reverse()
    output_list.append(char_list[0])
    output_list.reverse()
    print("-".join(output_list))
