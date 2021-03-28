# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

infile = sys.argv[1]
outfile = sys.argv[2]


input = open(infile, "r")
data = input.read().split("\n")[:-1]
input.close()

L = []
large_L = 0
output = open(outfile, "w")

V = defaultdict(int)
for line in data:
    substrings= line.split(" ")
    L.append(len(substrings))
    if len(substrings) >= 1000:
        large_L += 1
    new_codes = []
    for s in substrings:
        V[s] += 1
        substring = s.split("▁")
        new_substring = []
        for char in substring:
            new_substring.append(char)
        ns = "".join(new_substring)
        new_codes.append(ns)
    outstring = " ".join(new_codes)+"\n"
#    print(outstring)
    output.write(outstring)
output.close()

avg_len = sum(L) / float(len(L))
min_len = min(L)
max_len = max(L)

print("CP avg len", avg_len)
#print("CP min len", min_len)
#print("CP max len", max_len)
#print("CP num >= 1000", large_L)
#print("CP total", len(L))
print("CP unique vocab:", len(list(V.keys())))
