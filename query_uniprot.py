import requests

def fetch_uniprot_data(gene_name, output_file):
    url = f"https://rest.uniprot.org/uniprotkb/search?query={gene_name}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(output_file, "w") as file:  # Open file in write mode
            for entry in data.get("results", []):
                function = entry.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", "N/A")
                result_line = f"Gene: {gene_name}, Function: {function}\n"
                file.write(result_line)  # Save each line to the file
        print(f"Results saved to {output_file}")
    else:
        print(f"Error fetching data for {gene_name}, Status Code: {response.status_code}")

# Call the function and specify the output file
fetch_uniprot_data("ureA", "uniprot_results.txt")
