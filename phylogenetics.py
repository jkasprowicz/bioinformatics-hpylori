from Bio import SeqIO, Phylo
from Bio.Align.Applications import MafftCommandline
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO
from io import StringIO  # Required to handle stdout as a file-like object

# Extract the 16S rRNA sequences from GenBank file
sequences = []
for record in SeqIO.parse("/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gbk", "genbank"):
    for feature in record.features:
        if feature.type == "rRNA" and "16S" in feature.qualifiers.get("product", []):
            sequences.append(str(feature.extract(record).seq))

# Perform multiple sequence alignment using MAFFT
with open("16S_sequences.fasta", "w") as out_file:
    for i, seq in enumerate(sequences):
        out_file.write(f">seq{i}\n{seq}\n")

        

# Align the sequences using MAFFT
mafft_cline = MafftCommandline("mafft", input="16S_sequences.fasta")
stdout, stderr = mafft_cline()


print(stdout)

print(stderr)

# Use StringIO to treat the stdout (bytes) as a file-like object
alignment_stream = StringIO(stdout)



# Parse the alignment
alignment = AlignIO.read(alignment_stream, "fasta")

# Calculate distance matrix based on identity
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)

# Construct the phylogenetic tree using the distance matrix
constructor = DistanceTreeConstructor()
tree = constructor.build_tree(dm)

# Plot the tree
Phylo.draw(tree)
