#!/bin/bash

FILES=/home/luuk_janssen/scriptie/laughter-detection/input_078120640820344/*
for f in $FILES; do
    python3 segment_laughter.py $f models/model.h5 output_078120640820344 0.5 1 True  
done