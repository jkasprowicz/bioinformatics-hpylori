import matplotlib.pyplot as plt
from Bio import SeqIO

# Parse gene locations
gbk_file = "/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gbk"
gene_positions = []

for record in SeqIO.parse(gbk_file, "genbank"):
    for feature in record.features:
        if feature.type == "CDS":
            start = int(feature.location.start)  # Convert ExactPosition to integer
            end = int(feature.location.end)    # Convert ExactPosition to integer
            gene_positions.append((start, end))

# Scatter plot of gene start and end positions
starts, ends = zip(*gene_positions)
plt.scatter(starts, ends, alpha=0.6, color="blue")
plt.xlabel("Start Position")
plt.ylabel("End Position")
plt.title("Gene Locations on the Contig")
plt.show()
