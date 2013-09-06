#!/bin/bash

python extract-data.py
python normalize-data.py
python find-immune-genes.py

echo `cat immune-genes.tsv | wc -l` "immune genes found"

rm data-raw.tsv
rm data-normalized.tsv

exit 0
