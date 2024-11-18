from Bio import SeqIO

# Read a GenBank file
file_path = "/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.gbk"
for record in SeqIO.parse(file_path, "genbank"):
    print(f"Genome ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Number of features: {len(record.features)}")
    
    for feature in record.features:
        if feature.type == "CDS":
            gene = feature.qualifiers.get("gene", ["Unknown"])[0]
            product = feature.qualifiers.get("product", ["Unknown"])[0]
            print(f"Gene: {gene}, Product: {product}")
