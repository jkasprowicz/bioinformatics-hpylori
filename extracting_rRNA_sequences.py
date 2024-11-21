from Bio import SeqIO

# Load the GenBank file
genbank_file = "/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gbk"  # Replace with your GenBank file name
genbank_record = SeqIO.read(genbank_file, "genbank")

# Extract rRNA sequences from the GenBank record
rRNA_sequences = []
for feature in genbank_record.features:
    if feature.type == "rRNA":
        # Extract the rRNA sequence using the location
        rRNA_seq = feature.extract(genbank_record.seq)
        
        # Store rRNA sequence and related data
        rRNA_sequences.append({
            "id": feature.qualifiers.get('locus_tag', ['Unknown'])[0],
            "sequence": rRNA_seq,
            "location": feature.location,
            "product": feature.qualifiers.get('product', ['N/A'])[0]
        })

# Saving rRNA sequences to a FASTA file
with open("rRNA_sequences.fasta", "w") as output_file:
    for rRNA in rRNA_sequences:
        # Write the sequence in FASTA format
        output_file.write(f">{rRNA['id']}\n{rRNA['sequence']}\n")

# Print a confirmation message
print("rRNA sequences have been saved to rRNA_sequences.fasta")
