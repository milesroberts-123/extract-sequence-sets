# extract-sequence-sets

Extract multiple sets of sequences, mutually exclusive or not, from a single fasta file.

This script takes multiple lists of sequence ids as input and then extracts the sequences in each list from a single fasta file. A seperate fasta file is created for each list of sequence ids. This is an especially useful operation if one has, for example, clustered genes based on expression patterns and now wants to extract sequences for the genes in each cluster for further analysis (see [here]() for how to extract promoter sequences from a list of 

## USAGE

python3 extract_sequence_sets.py <FASTA FILE> <LIST OF SEQUENCE SETS>

For example:

`python3 extract_sequence_sets.py example_sequences.fasta example_cluster_membership.txt`

the above code will take the lists of sequence ids stored in `example_cluster_membership.txt` and extract the sequence ids

The output fasta files will be named as `seq_<CLUSTER NAME>.fasta`. The name for each cluster is defined as the first element of each row in `example_cluster_membership.txt` (see format notes below)

## FORMAT

The list of sequence sets should be written as a tab-delimited text file. Each row lists the sequence membership of a given set. For example:

```
Cluster1  gene1 gene2 ...
Cluster2  gene11  gene12  ...
Cluster3  gene21  gene22 ...
```

The first column contains the set/cluster names. gene1, gene2, etc. belong to the set named Cluster1. gene11, gene12, etc. belong to the set named Cluster2 and so on.

***IMPORTANT:*** If the sequence sets/clusters are not of the same size, then add "NA" elements to the lines of the other clusters until they are the same length as the longest
cluster.

## DEPENDENCIES

1. Biopython

`pip install biopython`

If that doesn't work, see installation instructions [here](https://biopython.org/wiki/Download).

2. Python3 - I wrote this script in python v3.8

