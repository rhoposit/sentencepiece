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



def save_sp(outfolder, text, codes, set_):
    n_failed = 0
    os.makedirs(outfolder, exist_ok=True)
    for f in set_:
        try:
            string1 = text[f]
            string2 = codes[f]
            if string1 != "" and string2 != "":
                outfile = outfolder+"/"+f+".txt"
                output = open(outfile, "w")
                outstring = str(string1) + "\t" + string2
                output.write(outstring)
                output.close()
            else:
                n_failed += 1
        except:
            n_failed += 1
            continue
    print("total failed: ", n_failed, " of ", len(set_))

def revise_codes(code, model, set_):
    revised_codes = defaultdict(str)
    s = spm.SentencePieceProcessor(model_file=model)
    for f in set_:
        codestring = code[f].split(".")
        codestring = [c for c in codestring if c]
        # convert to kanji characters
        kanjilist = []
        for c in codestring:
            key = int(c)
            value = kanji[key]
            kanjilist.append(value)
        kanjistring = "".join(kanjilist)
        # get the codes for this string of kanji characters
        rev_code = s.encode(kanjistring, out_type=str)
        rev_code_id = s.encode(kanjistring, out_type=int)
        rev_code_id = [str(c) for c in rev_code_id]
#        print("orig", len(codestring), "kanji", len(kanjilist), "SP", len(rev_code_id))
        revised_codes[f] = " ".join(rev_code_id)
    return revised_codes



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
    spout_folder_text = "/home/s1738075/special/L1_dat_files/sys5/vctk_753011/all_vctk_170_SP_text_"+str(vocab_size)
    spout_folder_phones = "/home/s1738075/special/L1_dat_files/sys5/vctk_753011/all_vctk_170_SP_phones_"+str(vocab_size)
    sp_model = "/home/s1738075/sentencepiece/models/"+outfolder+".code."+vocab_size+".model"
#elif data_type == "phn50":
#    outfolder= "all_vctk_phn_50"
#    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/test.csv"
#    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/train.csv"
#    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/validation.csv"
#    infolder = "/home/s1738075/special/L1_dat_files/sys5_phn50/phn50_nnnn/all_vctk_phn50"
#    phnfolder = "/home/s1738075/data/all_vctk_phn50_phones"
#    spout_folder_text = "/home/s1738075/special/L1_dat_files/sys5_phn50/vctk_nnnn/all_vctk_phn50_SP_text_"+str(vocab_size)
#    spout_folder_phones = "/home/s1738075/special/L1_dat_files/sys5_phn50/vctk_nnnn/all_vctk_phn50_SP_phones_"+str(vocab_size)
#    sp_model = "/home/s1738075/sentencepiece/models/"+outfolder+".code."+vocab_size+".model"
elif data_type == "phn100":
    outfolder= "all_vctk_phn_100"
    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/test.csv"
    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/train.csv"
    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/validation.csv"
    infolder = "/home/s1738075/special/L1_dat_files/sys5_phn100/phn100_648024/all_vctk"
    phnfolder = "/home/s1738075/data/all_vctk_170_phones"
    spout_folder_text = "/home/s1738075/special/L1_dat_files/sys5_phn100/phn100_648024/all_vctk_phn100_SP_text_"+str(vocab_size)
    spout_folder_phones = "/home/s1738075/special/L1_dat_files/sys5_phn100/phn100_648024/all_vctk_phn100_SP_phones_"+str(vocab_size)
    sp_model = "/home/s1738075/sentencepiece/models/"+outfolder+".code."+vocab_size+".model"
elif data_type == "siwis":
#    outfolder = "all_siwis_512"
    outfolder = "all_siwis_161"
    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/test.csv"
    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/train.csv"
    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/validation.csv"
#    infolder = "/home/s1738075/special/L1_dat_files/sys5_lang/siwis_552024/all_siwis_512"
    infolder = "/home/s1738075/special/L1_dat_files/sys5_lang/siwis_552024/all_siwis_161"
    phnfolder = "/home/s1738075/data/SIWIS/phones"
    spout_folder_text = "/home/s1738075/special/L1_dat_files/sys5_lang/siwis_552024/all_siwis_161_SP_text_"+str(vocab_size)
    spout_folder_phones = "/home/s1738075/special/L1_dat_files/sys5_lang/siwis_552024/all_siwis_161_SP_phones_"+str(vocab_size)
    sp_model = "/home/s1738075/sentencepiece/models/"+outfolder+".code."+vocab_size+".model"


print("processing test set")
set_files = load_set(test_set)
T, C = load_txtcode(infolder, set_files)
phn = load_phones(phnfolder, set_files)
code_revised = revise_codes(C, sp_model, set_files)
save_sp(spout_folder_text, T, code_revised, set_files)
save_sp(spout_folder_phones, phn, code_revised, set_files)

print("processing validation set")
set_files = load_set(validation_set)
T, C = load_txtcode(infolder, set_files)
phn = load_phones(phnfolder, set_files)
code_revised = revise_codes(C, sp_model, set_files)
save_sp(spout_folder_text, T, code_revised, set_files)
save_sp(spout_folder_phones, phn, code_revised, set_files)

print("processing training set")
set_files = load_set(training_set)
T, C = load_txtcode(infolder, set_files)
phn = load_phones(phnfolder, set_files)
code_revised = revise_codes(C, sp_model, set_files)
save_sp(spout_folder_text, T, code_revised, set_files)
save_sp(spout_folder_phones, phn, code_revised, set_files)



