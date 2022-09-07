#!/usr/bin/env bash
cd data
wget https://repod.icm.edu.pl/api/datasets/251/versions/59/files/download?format=original -O schizophrenia_28_edf.zip
unzip schizophrenia_28_edf.zip
sha256sum -c sha256sums
