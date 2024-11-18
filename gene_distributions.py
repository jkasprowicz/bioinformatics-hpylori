from BCBio import GFF
from Bio import SeqIO
import matplotlib.pyplot as plt
# File path to Prokka's GFF output
gff_file = "/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gff"

with open(gff_file) as f:
    for rec in GFF.parse(f):
        print(f"Contig: {rec.id}, Length: {len(rec)}")
        for feature in rec.features:
            if feature.type == "CDS":  # CDS features are genes
                gene_name = feature.qualifiers.get("gene", ["Unknown"])[0]
                product = feature.qualifiers.get("product", ["Unknown"])[0]
                print(f"Gene: {gene_name}, Product: {product}")


gene_lengths = []

for record in SeqIO.parse("/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gbk", "genbank"):
    for feature in record.features:
        if feature.type == "CDS":
            length = len(feature.location)
            gene_lengths.append(length)

plt.hist(gene_lengths, bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Gene Length (bp)")
plt.ylabel("Frequency")
plt.title("Gene Length Distribution")
plt.show()
