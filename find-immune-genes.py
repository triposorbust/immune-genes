#!/usr/bin/env python

import numpy as np
import scipy.stats as stats

P_VALUE = 0.005
INPUT_FILE = "data-normalized.tsv"
OUTPUT_FILE = "immune-genes.tsv"
LOOKUP_FILE = "affy-id-genes.tsv"
SPECS = [
    (stats.ttest_ind, (0,1), (2,3), "Th1"),
    (stats.ttest_ind, (0,1), (4,5), "Th2"),
    (stats.ttest_ind, (0,1), (6,7), "Th17"),
    (stats.ttest_ind, (8,9), (10,11), "Tfh"),
]

def make_id_dict():
    d = {}
    fr = open(LOOKUP_FILE, 'r')
    for line in fr:
        words = line.strip().split("\t")
        at_id = words[0]
        gene = words[1]
        d[at_id] = gene
    return d

def main():
    id_dict = make_id_dict()
    fr = open(INPUT_FILE, 'r')
    fw = open(OUTPUT_FILE, 'w')
    results = [ ] # nothing here yet

    _ = fr.readline()
    for line in fr:
        words = line.split()
        at_id = words[0]
        name = id_dict.get(at_id, "-")
        values = np.array(words[1:], dtype='float')

        result = [at_id, name]
        for func, (a,b), (x,y), label in SPECS:
            ab = values[a:b+1]
            xy = values[x:y+1]
            t,p = func(ab, xy)
            result.append(p)

        results.append(result)

    header = "{0}\t{1}\n".format("\t".join(["Affx-ID", "Gene"]),
                                 "\t".join([spec[-1] for spec in SPECS]))
    fw.write(header)
    for result in results:
        if all(map(lambda p: p > P_VALUE, result[2:])):
            continue
        lstring = "\t".join(map(str, result))
        fw.write(lstring + "\n")

    fw.close()
    fr.close()
    return

if __name__ == "__main__":
    main()
