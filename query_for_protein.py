from Bio import SeqIO
import requests

def fetch_uniprot_annotation(sequence):
    """
    Query UniProt with a protein sequence to retrieve potential annotations.
    """
    url = "https://rest.uniprot.org/uniprotkb/search"
    params = {
        "query": f"sequence:{sequence}",
        "format": "json"
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        annotations = []
        for entry in data.get("results", []):
            protein = entry.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", "N/A")
            annotations.append(protein)
        return annotations
    else:
        print(f"Error fetching data. Status Code: {response.status_code}")
        return []

def annotate_hypothetical_proteins(fasta_file, output_file):
    """
    Reads a FASTA file, queries UniProt for each sequence, and writes annotations to a file.
    """
    with open(output_file, "w") as outfile:
        for record in SeqIO.parse(fasta_file, "fasta"):
            protein_id = record.id
            sequence = str(record.seq)
            annotations = fetch_uniprot_annotation(sequence)
            
            if annotations:
                outfile.write(f"{protein_id}\t{'; '.join(annotations)}\n")
            else:
                outfile.write(f"{protein_id}\tNo annotation found\n")


input_fasta = "/Users/joaokasprowicz/Documents/Dev/bioinformatics/annotation_results/helicobacter_pylori.fna"  
output_annotations = "annotations_results.txt"
annotate_hypothetical_proteins(input_fasta, output_annotations)
