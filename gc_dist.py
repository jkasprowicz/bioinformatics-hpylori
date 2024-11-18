from Bio.SeqUtils import gc_fraction
from Bio import SeqIO
import matplotlib.pyplot as plt

# Parse GenBank file and calculate GC content
gbk_file = "/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gbk"
gc_contents = []
gene_ids = []

for record in SeqIO.parse(gbk_file, "genbank"):
    for feature in record.features:
        if feature.type == "CDS":
            sequence = feature.extract(record.seq)
            gc_contents.append(gc_fraction(sequence))
            gene_ids.append(feature.qualifiers.get("locus_tag", ["Unknown"])[0])

# Scatter plot of GC content
plt.scatter(range(len(gc_contents)), gc_contents, color='green', alpha=0.7)
plt.xlabel("Gene Index")
plt.ylabel("GC Content")
plt.title("GC Content Across Genes")
plt.show()
