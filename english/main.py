import os
import pickle
from process import Process

# Define file paths
alphabet_file_path = '/embeddings/english/alphabet_en'
text_file_path = '/Users/murilo/PycharmProjects/personal/embeddings/txt_to_add'
normalized_embeddings_file_path = '/Users/murilo/PycharmProjects/personal/embeddings/normalized_embeddings.pkl'

process = Process(alphabet_file_path, text_file_path)

if not os.path.exists('normalized_embeddings.pkl'):

    # create embeddings
    txt, embeddings = process.load_text()
    # normalize embeddings
    normalized_embeddings = Process.normalize_embedding(embeddings)

    # Save the normalized embeddings
    Process.save_embedding(normalized_embeddings, normalized_embeddings_file_path)

else:
    # read previous pickle file
    with open('normalized_embeddings.pkl', 'rb') as f:
        normalized_embeddings = pickle.load(f)

    # create embeddings
    txt, embeddings = process.load_text()

    # normalize embeddings
    new_normalized_embeddings = Process.normalize_embedding(embeddings)

    # drop value if already exists
    for i in txt:
        Process.check_key(embeddings, i)

    # Save the normalized embeddings
    Process.save_embedding(new_normalized_embeddings, normalized_embeddings_file_path)

