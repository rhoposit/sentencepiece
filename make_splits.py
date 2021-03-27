import os, sys


def load_set(infile):
    input = open(infile, "r")
    data = input.read().split("\n")
    input.close()
    return data

def load_txtcode(indir, set_):
    text, codes = [], []
    for f in set_:
        try:
            fname = indir+"/"+f+".txt"
            input = open(fname, "rb")
            data = input.read().decode('ascii', 'ignore')
            input.close()
            t = data.split("\t")[0]
            c = data.split("\t")[1].replace(" ", ".")
            text.append(t)
            codes.append(c)
        except:
            continue
    return text, codes


def save_text(fold, outfolder, texts):
    outfile = outfolder+"/"+fold+".text"
    output = open(outfile, "w")
    outstring = "\n".join(texts)
    output.write(outstring)
    output.close()
    
def save_code(fold, outfolder, codes):
    outfile = outfolder+"/"+fold+".code"
    output = open(outfile, "w")
    outstring = "\n".join(codes)
    output.write(outstring)
    output.close()




data_type = sys.argv[1]

if data_type == "vctk":
#    outfolder = "all_vctk_512"
    outfolder= "all_vctk_170"
    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/test.csv"
    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/train.csv"
    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes/validation.csv"
#    infolder = "/home/s1738075/special/L1_dat_files/sys5/vctk_753011/all_vctk_512"
    infolder = "/home/s1738075/special/L1_dat_files/sys5/vctk_753011/all_vctk_170"
elif data_type == "siwis":
#    outfolder = "all_siwis_512"
    outfolder = "all_siwis_161"
    test_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/test.csv"
    training_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/train.csv"
    validation_set = "/home/s1738075/taco_modified/self_attention_tacotron/examples/codes_siwis/validation.csv"
#    infolder = "/home/s1738075/special/L1_dat_files/sys5_lang/siwis_552024/all_siwis_512"
    infolder = "/home/s1738075/special/L1_dat_files/sys5_lang/siwis_552024/all_siwis_161"

test_set_files = load_set(test_set)
train_set_files = load_set(training_set)
dev_set_files = load_set(validation_set)


text_test, code_test = load_txtcode(infolder, test_set_files)
save_text("test", outfolder, text_test)
save_code("test", outfolder, code_test)

text_dev, code_dev = load_txtcode(infolder, dev_set_files)
save_text("dev", outfolder, text_dev)
save_code("dev", outfolder, code_dev)

text_train, code_train = load_txtcode(infolder, train_set_files)
save_text("train", outfolder, text_train)
save_code("train", outfolder, code_train)
