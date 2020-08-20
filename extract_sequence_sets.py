from Bio import SeqIO
import re
import sys


"""
EXTRACT PROMOTER SEQ FOR EACH CLUSTER
"""

#Load sequences
sequences_slyco = SeqIO.to_dict(SeqIO.parse(sys.argv[1], "fasta"))

file = open(sys.argv[2], "r")
file = file.readlines()

#Count number of clusters in file
clusters = len(file)

#Iterate over the sequences in each cluster, extract them from fasta file
for cluster in file:
	result = []

	#Remove newline
	cluster = re.sub("\n", "", cluster)
	cluster = re.sub('"', '', cluster)

	#Split into list
	cluster = cluster.split("\t")

	#Remove headers, extract name
	clustname = cluster[0]
	cluster.pop(0)
	print("Extracting sequences for cluster %s" % clustname)

	#Remove NA's
	cluster = [x for x in cluster if x != "NA"]

	#Extract seqs
	for seq in cluster:
		result.append(sequences_slyco[seq])
	print("Sequences extracted: %i" % len(result))
	SeqIO.write(result, "seq_" + clustname + ".fasta", "fasta")
