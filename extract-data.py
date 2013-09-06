#!/usr/bin/env python

FILENAMES = [
    "data/GSM357847-naive-1.tsv",
    "data/GSM357848-naive-2.tsv",
    "data/GSM357844-Th1-1.tsv",
    "data/GSM357842-Th1-2.tsv",
    "data/GSM357839-Th2-1.tsv",
    "data/GSM357841-Th2-2.tsv",
    "data/GSM357843-Th17-1.tsv",
    "data/GSM357845-Th17-2.tsv",
    "data/GSM534250-non-Tfh-1.tsv",
    "data/GSM534251-non-Tfh-2.tsv",
    "data/GSM534252-Tfh-1.tsv",
    "data/GSM534253-Tfh-2.tsv",
    "data/GSM534256-naive.tsv",
]
OUTPUT_FILE = "data-raw.tsv"

def make_data_dictionary(filename):
    """Generates a dictionary of affy id's to string-typed values."""

    def make_kv(line):
        words = line.split()
        return (words[0], words[1])

    def skip(line):
        return line.strip() == "" \
               or line.startswith("#") \
               or line.startswith("ID_REF")

    with open(filename, "r") as f:
        data_dictionary = dict([make_kv(l) for l in f if not skip(l)])
    return data_dictionary

def make_column_header(filename):
    return filename.split("-", 1)[-1].replace(".tsv", "")

def main():
    """Compiles all of the microarray measurements from multiple GSM data
    files into a single tsv file."""

    headers = map(make_column_header, FILENAMES)
    dictionaries = map(make_data_dictionary, FILENAMES)
    affy_id_sets = map(lambda d: set(d.keys()), dictionaries)
    common_affy_ids = reduce(lambda a,b: a&b, affy_id_sets)

    with open(OUTPUT_FILE, "w") as f:
        f.write("{0}\t{1}\n".format("probeset", "\t".join(headers)))
        for affy_id in sorted(list(common_affy_ids)):
            value_strings = [d[affy_id] for d in dictionaries]
            f.write("{0}\t{1}\n".format(affy_id, "\t".join(value_strings)))
    return

if __name__ == "__main__":
    main()
