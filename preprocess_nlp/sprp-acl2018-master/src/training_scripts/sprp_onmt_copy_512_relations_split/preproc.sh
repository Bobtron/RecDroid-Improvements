#!/bin/bash

#!/usr/bin/env bash

# base_path=/home/nlp/aharonr6/

# python $base_path/git/OpenNMT-py/preprocess.py \
# -train_src $base_path/git/Split-and-Rephrase/baseline-seq2seq-RDFs-relations/train.complex \
# -train_tgt $base_path/git/Split-and-Rephrase/baseline-seq2seq-RDFs-relations/train.simple \
# -valid_src $base_path/git/Split-and-Rephrase/baseline-seq2seq-RDFs-relations/validation.complex \
# -valid_tgt $base_path/git/Split-and-Rephrase/baseline-seq2seq-RDFs-relations/validation.simple \
# -save_data $base_path/git/Split-and-Rephrase/baseline-seq2seq-RDFs-relations/baseline \
# -src_seq_length 10000 \
# -tgt_seq_length 10000 \
# -src_seq_length_trunc 999 \
# -tgt_seq_length_trunc 999 \
# -dynamic_dict \
# -share_vocab


base_path=/Users/personanongrata/Documents/USC/RecDroid-Improvements/preprocess_nlp

python $base_path/OpenNMT-py/preprocess.py \
-train_src $base_path/sprp-acl2018-master/data/baseline-seq2seq-split-RDFs-relations/train.complex \
-train_tgt $base_path/sprp-acl2018-master/data/baseline-seq2seq-split-RDFs-relations/train.simple \
-valid_src $base_path/sprp-acl2018-master/data/baseline-seq2seq-split-RDFs-relations/validation.complex \
-valid_tgt $base_path/sprp-acl2018-master/data/baseline-seq2seq-split-RDFs-relations/validation.simple \
-save_data $base_path/sprp-acl2018-master/data/baseline-seq2seq-split-RDFs-relations/baseline \
-src_seq_length 10000 \
-tgt_seq_length 10000 \
-src_seq_length_trunc 999 \
-tgt_seq_length_trunc 999 \
-dynamic_dict \
-share_vocab
