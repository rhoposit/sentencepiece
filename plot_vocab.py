# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

folder = sys.argv[1]
outfile = ""
Vsize = [256, 512, 1024, 2048, 4096]
S = ["train", "valid", "test"]

SetVocab = {"train":defaultdict(float), "valid":defaultdict(float), "test":defaultdict(float)}
for s in S:
    for v in Vsize:
        UttLengths = []
        Vocab = defaultdict(int)
        infile = folder+"/"+s+".code.conv."+str(v)
        input = open(infile, "r")
        data = input.read().split("\n")[:-1]
        input.close()
        
        for line in data:
            substrings= line.split(" ")
            UttLengths.append(len(substrings))
            for s in substrings:
                Vocab[s] += 1

        total_vocab = len(list(Vocab.keys()))
        avg_utt_length = sum(UttLengths) / float(len(UttLengths))
        this_dict = SetVocab[s]
        this_dict[v] = avg_utt_length
        SetVocab[s] = this_dict

for fold,dist in SetVocab.items():
    print(fold, dist)
