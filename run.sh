#!/bin/bash

python extract-data.py 2>> errors.log
python normalize-data.py 2>> errors.log
python find-immune-genes.py 2>> errors.log

echo `cat immune-genes.tsv | wc -l` "immune genes found"

rm data-raw.tsv
rm data-normalized.tsv

exit 0
