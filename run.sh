folder=$1
vsize=$2

python convert_codes.py ${folder}/train.code ${folder}/train.code.conv
python convert_codes.py ${folder}/dev.code ${folder}/dev.code.conv
python convert_codes.py ${folder}/test.code ${folder}/test.code.conv

#spm_train --input=${folder}/train.code.conv --model_prefix=models/${folder}.code.${vsize} --vocab_size=$vsize

#spm_encode --model=models/${folder}.code.${vsize}.model --output_format=piece < ${folder}/train.code.conv > ${folder}/train.code.conv.${vsize}
#spm_encode --model=models/${folder}.code.${vsize}.model --output_format=piece < ${folder}/dev.code.conv > ${folder}/dev.code.conv.${vsize}
#spm_encode --model=models/${folder}.code.${vsize}.model --output_format=piece < ${folder}/test.code.conv > ${folder}/test.code.conv.${vsize}

#python convert_clean.py ${folder}/train.code.conv.${vsize} ${folder}/train.code.conv.${vsize}.clean
#python convert_clean.py ${folder}/dev.code.conv.${vsize} ${folder}/dev.code.conv.${vsize}.clean
#python convert_clean.py ${folder}/test.code.conv.${vsize} ${folder}/test.code.conv.${vsize}.clean



