from Bio import SeqIO
from collections import Counter
import matplotlib.pyplot as plt

# Parse GenBank file for CDS features
gbk_file = "/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gbk"
cds_sequences = []

# Extract CDS sequences
for record in SeqIO.parse(gbk_file, "genbank"):
    for feature in record.features:
        if feature.type == "CDS":
            cds_sequences.append(str(feature.extract(record).seq))

# Function to calculate codon usage
def calculate_codon_usage(sequences):
    codon_count = Counter()
    
    # Iterate over each sequence
    for seq in sequences:
        # Split the sequence into codons (3 base pairs each)
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            if len(codon) == 3:  # Only consider complete codons
                codon_count[codon] += 1
                
    return codon_count

# Calculate codon usage for the CDS sequences
codon_usage = calculate_codon_usage(cds_sequences)

# Sort the codon usage dictionary by codon
sorted_codon_usage = dict(sorted(codon_usage.items()))

# Plot the codon usage
plt.figure(figsize=(10, 5))
plt.bar(sorted_codon_usage.keys(), sorted_codon_usage.values())
plt.xlabel("Codon")
plt.ylabel("Frequency")
plt.title("Codon Usage in Helicobacter pylori Genome")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
