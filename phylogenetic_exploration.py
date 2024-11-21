from Bio import AlignIO, Phylo
from Bio.Align.Applications import ClustalwCommandline
from Bio.Phylo import PhyloXML
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import SeqIO
from Bio.AlignIO import read

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



# Step 1: Align the sequences using ClustalW
clustalw_cline = ClustalwCommandline("clustalw2", infile="rRNA_sequences.fasta")
clustalw_cline()


# Step 2: Read the aligned sequences
alignment = AlignIO.read("rRNA_sequences.aln", "clustal")  # Read the .aln file
print("Aligned sequences:")
print(alignment)

# Step 3: Calculate the distance matrix using the 'identity' method
calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)
print("Distance Matrix:")
print(distance_matrix)

# Step 4: Construct the phylogenetic tree using Neighbor Joining
constructor = DistanceTreeConstructor()
# Pass the distance matrix (not the DistanceCalculator object)
tree = constructor.build_tree(distance_matrix)  

# Step 5: Visualize the tree
Phylo.draw(tree)