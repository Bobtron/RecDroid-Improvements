#!/bin/bash

#!/usr/bin/env bash

# base_path=/home/nlp/aharonr6/

# model_name=sprp_onmt_copy_512_relations_split

# python $base_path/git/OpenNMT-py/train.py \
# -save_model $base_path/git/phrasing/models/${model_name}/${model_name} \
# -data $base_path/git/Split-and-Rephrase/baseline-seq2seq-RDFs-relations/baseline \
# -global_attention mlp \
# -word_vec_size 512 \
# -rnn_size 512 \
# -layers 1 \
# -encoder_type brnn \
# -epochs 20 \
# -seed 777 \
# -batch_size 64 \
# -max_grad_norm 2 \
# -share_embeddings \
# -gpuid 2 \
# -start_checkpoint_at 1 \
# -start_epoch 1 \
# -copy_attn


# -train_from $base_path/git/phrasing/models/${model_name}/sprp_onmt_baseline_256_acc_88.65_ppl_1.79_e12.pt
#-copy_attn_force \





base_path=/Users/personanongrata/Documents/USC/RecDroid-Improvements/preprocess_nlp

model_name=sprp_onmt_copy_512_relations_split

python $base_path/OpenNMT-py/train.py \
-save_model $base_path/sprp-acl2018-master/data/models/${model_name}/${model_name} \
-data $base_path/sprp-acl2018-master/data/baseline-seq2seq-split-RDFs-relations/baseline \
-global_attention mlp \
-word_vec_size 512 \
-rnn_size 512 \
-layers 1 \
-encoder_type brnn \
-epochs 20 \
-seed 777 \
-batch_size 64 \
-max_grad_norm 2 \
-share_embeddings \
-start_checkpoint_at 1 \
-start_epoch 1 \
-copy_attn


