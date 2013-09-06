#!/usr/bin/env python

import sys
import string
import numpy as np

RAW_DATA_FILENAME = "data-raw.tsv"
OUTPUT_FILENAME = "data-normalized.tsv"

class DataColumn():
    def __init__(self, series_dict, index):
        """Useful abstraction class: the value dictionary holds k,v pairs
        giving numbers at each id, while the rank dictionary holds the ranks
        corresponding to each k (id)."""

        # populates the value dictionary
        self.__value_dict__ = {}
        for k in series_dict.keys():
            v = series_dict[k][index]
            self.__value_dict__[k] = v

        # sort-based ranking routine
        kvs = zip(self.__value_dict__.keys(), self.__value_dict__.values())
        kvs.sort(key=lambda kv: kv[1])
        keys = [kv[0] for kv in kvs]
        ranks = range(len(keys))

        # populates the rank dictionary
        self.__rank_dict__ = {}
        for rank,key in zip(ranks, keys):
            self.__rank_dict__[rank] = key

    def get_value_for_key(self, key):
        return self.__value_dict__[key]

    def get_value_for_rank(self, rank):
        k = self.__rank_dict__[rank]
        v = self.__value_dict__[k]
        return v

    def set_value_for_rank(self, rank, value):
        k = self.__rank_dict__[rank]
        self.__value_dict__[k] = value

def build_series_dict(lines):
    d = {}
    for line in lines:
        d[line[0]] = np.array(line[1:], dtype='float')
    return d

def main(filenm):
    fr = open(filenm, 'r')
    headers = fr.readline()
    lines = [string.split(l) for l in fr]
    fr.close()

    series_dict = build_series_dict(lines)
    all_keys = [line[0] for line in lines]
    n = len(lines[0]) - 1
    l = len(lines)

    dcs = [DataColumn(series_dict, i) for i in range(n)]

    for rank in range(l):
        norm = np.average([dc.get_value_for_rank(rank) for dc in dcs])
        for dc in dcs:
            dc.set_value_for_rank(rank, norm)

    with open(OUTPUT_FILENAME, 'w') as fw:
        fw.write(headers)
        for key in all_keys:
            values = [dc.get_value_for_key(key) for dc in dcs]
            lstring = "{0}\t{1}\n".format(key, "\t".join(map(str, values)))
            fw.write(lstring)
    return

if __name__ == "__main__":
    main(RAW_DATA_FILENAME)
