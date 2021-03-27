import sys
from collections import defaultdict

infile = sys.argv[1]
outfile = sys.argv[2]
refile = "topokanji/lists/wikipedia.txt"


input = open(infile, "r")
data = input.read().split("\n")[:-1]
input.close()

input = open(refile, "r")
kanji = input.read().split("\n")[:-1]
input.close()




mapping = defaultdict(str)
for line in data:
    codes = line.split(".")
    if codes != ['']:
#        print(codes)
        for c in codes:
            key = int(c)
            value = kanji[key]
            mapping[key] = value

# katakana = 48
# hiragana = 46
# latin = 27
# kanji = 8000

L = []
output = open(outfile, "w")
for line in data:
    codes = line.split(".")
    L.append(len(codes))
    if codes != ['']:
        new_codes = []
        for c in codes:
            key = int(c)
            nc = mapping[key]
            new_codes.append(nc)
        outstring = "".join(new_codes)+"\n"
        output.write(outstring)
output.close()

avg_len = sum(L) / float(len(L))
print("codes avg len:", avg_len)
