#!/bin/bash

#!/usr/bin/env bash

# base_path=/home/nlp/aharonr6/

# model_name=sprp_onmt_copy_512_relations_split

# model_file=sprp_onmt_copy_512_relations_split_acc_47.53_ppl_15.83_e1.pt


# python $base_path/git/forks/OpenNMT-py/translate.py \
# -gpu 2 \
# -batch_size 1 \
# -model $base_path/git/phrasing/models/${model_name}/${model_file} \
# -src $base_path/git/Split-and-Rephrase/baseline-seq2seq-RDFs-relations/test.complex.unique \
# -output $base_path/git/phrasing/models/${model_name}/test.complex.unique.output \
# -beam_size 12 \
# -replace_unk

# python ${base_path}/git/phrasing/src/nmt_scripts/opennmt-py/${model_name}/test.py



base_path=/Users/personanongrata/Documents/USC/RecDroid-Improvements/preprocess_nlp

model_name=sprp_onmt_copy_512_relations_split

model_file=sprp_onmt_copy_512_relations_split_step_20.pt


python $base_path/OpenNMT-py/translate.py \
-model $base_path/sprp-acl2018-master/data/models/${model_name}/${model_file} \
-src $base_path/sprp-acl2018-master/data/baseline-seq2seq-split-RDFs-relations/test.complex.unique \
-output $base_path/sprp-acl2018-master/data/models/${model_name}/test.complex.unique.output \
-beam_size 12 \
-replace_unk

# python ${base_path}/git/phrasing/src/nmt_scripts/opennmt-py/${model_name}/test.py



