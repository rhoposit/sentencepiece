import os, sys
import sentencepiece as spm
from collections import defaultdict

refile = "topokanji/lists/wikipedia.txt"
input = open(refile, "r")
kanji = input.read().split("\n")[:-1]
input.close()


def load_set(infile):
    input = open(infile, "r")
    data = input.read().split("\n")
    input.close()
    return data

def load_txtcode(indir, set_):
    text, codes = defaultdict(str), defaultdict(str)
    for f in set_:
        try:
            fname = indir+"/"+f+".txt"
            input = open(fname, "rb")
            data = input.read().decode('ascii', 'ignore')
            input.close()
            t = data.split("\t")[0]
            c = data.split("\t")[1].replace(" ", ".")
            text[f] = str(t)
            codes[f] = c
#            print(f, t)
#            print(f, c)
        except:
            continue
    return text, codes


def load_phones(indir, set_):
    phones = defaultdict(str)
    for f in set_:
        try:
            fname = indir+"/"+f+".txt"
            input = open(fname, "rb")
            data = input.read()
            input.close()
            if phones != "":
                phones[f] = str(data.decode('utf-8'))
        except:
            continue
    return phones



def save_folds(outfolder, strings, codes, set_, fold, phn_txt):
    outfile1 = outfolder+"/"+fold+".raw."+phn_txt
    outfile2 = outfolder+"/"+fold+".raw.code"
    S, C = [], []
    for f in set_:
        s = strings[f]
        c = codes[f]
        if s != "":
            S.append(s)
            C.append(c)
    outstring1 = "\n".join(S)
    output = open(outfile1, "w")
    output.write(outstring1)
    output.close()
    outstring2 = "\n".join(C)
    output = open(outfile2, "w")
    output.write(outstring2)
    output.close()
                



data_type = sys.argv[1]
vocab_size = sys.argv[2]

if data_type == "vctk":
#    outfolder = "all_vctk_512"
    outfolder= "all_vctk_170"
    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/test.csv"
    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/train.csv"
    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/validation.csv"
#    infolder = "/home/s1738075/special/L1_dat_files/sys5/vctk_753011/all_vctk_512"
    infolder = "/home/s1738075/special/L1_dat_files/sys5/vctk_753011/all_vctk_170"
    phnfolder = "/home/s1738075/data/all_vctk_170_phones"
    folder_text = "/home/s1738075/espnet_private/egs/iwslt16/all_vctk_170.txt/data"
    folder_phones = "/home/s1738075/espnet_private/egs/iwslt16/all_vctk_170.phn/data"
#elif data_type == "phn50":
#    outfolder= "all_vctk_phn_50"
#    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/test.csv"
#    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/train.csv"
#    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/validation.csv"
#    infolder = "/home/s1738075/special/L1_dat_files/sys5_phn50/phn50_nnnn/all_vctk_phn50"
#    phnfolder = "/home/s1738075/data/all_vctk_phn50_phones"
##    spout_folder_text = "/home/s1738075/espnet_private/egs/iwslt16/all_vctk_170.txt"
##    spout_folder_phones = "/home/s1738075/espnet_private/egs/iwslt16/all_vctk_170.phn"
#    sp_model = "/home/s1738075/sentencepiece/models/"+outfolder+".code."+vocab_size+".model"
elif data_type == "phn100":
    outfolder= "all_vctk_phn_100"
    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/test.csv"
    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/train.csv"
    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/validation.csv"
    infolder = "/home/s1738075/special/L1_dat_files/sys5_phn100/phn100_648024/all_vctk"
    phnfolder = "/home/s1738075/data/all_vctk_170_phones"
    folder_text = "/home/s1738075/espnet_private/egs/iwslt16/all_vctk_ph100.txt/data"
    folder_phones = "/home/s1738075/espnet_private/egs/iwslt16/all_vctk_ph100.phn/data"
elif data_type == "siwis":
#    outfolder = "all_siwis_512"
    outfolder = "all_siwis_161"
    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/test.csv"
    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/train.csv"
    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/validation.csv"
#    infolder = "/home/s1738075/special/L1_dat_files/sys5_lang/siwis_552024/all_siwis_512"
    infolder = "/home/s1738075/special/L1_dat_files/sys5_lang/siwis_552024/all_siwis_161"
    phnfolder = "/home/s1738075/data/SIWIS/phones"
    folder_text = "/home/s1738075/espnet_private/egs/iwslt16/all_siwis_161.txt/data"
    folder_phones = "/home/s1738075/espnet_private/egs/iwslt16/all_siwis_161.phn/data"


print("processing test set")
set_files = load_set(test_set)
T, C = load_txtcode(infolder, set_files)
P = load_phones(phnfolder, set_files)
save_folds(folder_text, T, C, set_files, "test", "txt")
save_folds(folder_phones, P, C, set_files, "test", "phn")

print("processing validation set")
set_files = load_set(validation_set)
T, C = load_txtcode(infolder, set_files)
P = load_phones(phnfolder, set_files)
save_folds(folder_text, T, C, set_files, "dev", "txt")
save_folds(folder_phones, P, C, set_files, "dev", "phn")

print("processing training set")
set_files = load_set(training_set)
T, C = load_txtcode(infolder, set_files)
P = load_phones(phnfolder, set_files)
save_folds(folder_text, T, C, set_files, "train", "txt")
save_folds(folder_phones, P, C, set_files, "train", "phn")



