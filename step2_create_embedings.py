import openai
import os
import csv

# Set up OpenAI API credentials
def open_file(filepath):
	with open(filepath, 'r', encoding='utf-8') as infile:
		return infile.read()

openai.api_key = open_file('key_openai.txt')

# Define a function to embed text using OpenAI
def embed_text(text):
    # Define the model and parameters for the Embeddings API
    model_engine = "text-embedding-ada-002"
    input_data = {"text": text}

    # Call the OpenAI API to generate the embeddings
    response = openai.Embedding.create(model=model_engine, input=input_data)

    # Extract the embeddings from the API response
    embeddings = response["data"][0]["vector"]
    return embeddings

# Define the directory where the output files are saved
output_dir = 'output_chunked'

# Define the output file name
output_file = 'embeddings.csv'

# Create a CSV file to store the embeddings
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['filename', 'embeddings'])

    # Loop through all files in the output directory and its subdirectories
    for root, dirs, files in os.walk(output_dir):
        for filename in files:
            if filename.endswith('.txt'):
                # Read the text from the file
                with open(os.path.join(root, filename), 'r') as f:
                    text = f.read()

                # Embed the text using OpenAI
                embeddings = embed_text(text)

                # Write the embeddings to the CSV file
                writer.writerow([filename, embeddings])

########
###GERANDO O ERRO DE FORMAção!