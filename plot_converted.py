import sys
from collections import defaultdict

orig_infile = sys.argv[1]
infile = sys.argv[2]
outfile = sys.argv[3]

refile = "topokanji/lists/wikipedia.txt"


input = open(orig_infile, "r")
data = input.read().split("\n")[:-1]
input.close()

input = open(refile, "r")
kanji = input.read().split("\n")[:-1]
input.close()




mapping = defaultdict(str)
rev_mapping = defaultdict(str)
for line in data:
    codes = line.split(".")
    for c in codes:
        key = int(c)
        value = kanji[key]
        mapping[key] = value
        rev_mapping[value] = key
        
# katakana = 48
# hiragana = 46
# latin = 27
# kanji = 8000



input = open(infile, "r")
data = input.read().split("\n")[:-1]
input.close()


output = open(outfile, "w")
for line in data:
    substrings= line.split(" ")
    print(len(substrings))
    new_codes = []
    for s in substrings:
        substring = s.split("▁")
        new_substring = []
        for char in substring:
            key = rev_mapping[char]
            new_substring.append(str(key))
        ns = ".".join(new_substring)
        new_codes.append(ns)
    outstring = " ".join(new_codes)+"\n"
#    print(outstring)
    output.write(outstring)
output.close()
