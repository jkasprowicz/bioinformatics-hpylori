from Bio import SeqIO
import csv

faa_file = "/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.faa"
output_csv = "protein_sequences.csv"

for record in SeqIO.parse(faa_file, "fasta"):
    print(f"Protein ID: {record.id}")
    print(f"Sequence: {record.seq}")
    with open(output_csv, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header row
        csvwriter.writerow(["Protein ID", "Sequence"])
        
        # Parse and write each protein
        for record in SeqIO.parse(faa_file, "fasta"):
            csvwriter.writerow([record.id, str(record.seq)])


