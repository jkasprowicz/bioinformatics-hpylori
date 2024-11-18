from Bio import SeqIO
from BCBio import GFF
import numpy as np

# Parse GFF3 file
with open("/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gff") as gff_file:
    for record in GFF.parse(gff_file):
        for feature in record.features:
            print(f"Feature: {feature.type}, Location: {feature.location}")
