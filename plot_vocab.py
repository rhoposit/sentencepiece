# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
import matplotlib.pyplot as plt

folder = sys.argv[1]
outfile = ""
Vsize = [256, 512, 1024, 2048, 4096]
FOLDS = ["train", "dev", "test"]




def create_plot(SetVocab, title, filename):
    plt.xlabel("Vocabulary Size")
    plt.ylabel("Avg. Utterance Length")
    plt.title(title)
    train = SetVocab["train"]
    dev = SetVocab["dev"]
    test = SetVocab["test"]
    plt.plot(list(train.keys()), list(train.values()), linewidth=2, color='c', label="train")
    plt.plot(list(dev.keys()), list(dev.values()), linewidth=2, color='g', label="dev")
    plt.plot(list(test.keys()), list(test.values()), linewidth=2, color='b', label="test")
    plt.legend(loc="lower left")
    plt.ylim((0,1000))
#    plt.xlim((0,10))
    plt.savefig(filename)
    plt.clf()
    plt.close()


SetVocab = {"train":defaultdict(float), "dev":defaultdict(float), "test":defaultdict(float)}
for fold in FOLDS:
    for v in Vsize:
        UttLengths = []
        Vocab = defaultdict(int)
        infile = folder+"/"+fold+".code.conv."+str(v)
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
        this_dict = SetVocab[fold]
        this_dict[v] = avg_utt_length
        SetVocab[fold] = this_dict

for fold,dist in SetVocab.items():
    print(fold, dist)

create_plot(SetVocab, "Avg Utterance Length per Sentencepiece Vocab Size", "FoldsVocabUttLength.png")
