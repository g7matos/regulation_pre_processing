import os

def split_text(input_path):
    # Open the input file using a context manager
    with open(input_path, 'r') as f:
        alltext = f.read()
    
    # Split the text into chunks that end before "Art."
    max_chunk_size = 4000
    art_expression = 'Art.'
    art_index = alltext.rfind(art_expression)
    chunks = []
    chunk_counter = 1
    while art_index >= 0:
        chunk = alltext[art_index:].strip()
        chunks.insert(0, chunk)
        alltext = alltext[:art_index]
        art_index = alltext.rfind(art_expression)
        if len("".join(chunks)) > max_chunk_size:
            # Save the current chunk to a file in the output directory
            output_dir = os.path.join('output_chunked', os.path.splitext(os.path.basename(input_path))[0])
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_path))[0]}_{chunk_counter}.txt")
            with open(output_path, 'w') as f:
                f.write("".join(chunks))
            chunks = []
            chunk_counter += 1
    if len(alltext) > 0:
        # Save the last chunk to a file in the output directory
        chunks.insert(0, alltext.strip())
        output_dir = os.path.join('output_chunked', os.path.splitext(os.path.basename(input_path))[0])
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_path))[0]}_{chunk_counter}.txt")
        with open(output_path, 'w') as f:
            f.write("".join(chunks))

if __name__ == '__main__':
    input_dir = 'input_files'
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_dir, filename)
            split_text(input_path)
