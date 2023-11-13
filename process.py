import ast
import pickle
import numpy as np


class Process:
    def __init__(self, alphabet_file_path, text_file_path):
        self.alphabet_file_path = alphabet_file_path
        self.text_file_path = text_file_path
        self.alphabet_dict = self.load_alphabet()
        self.words, self.embedding = self.load_text()

    def load_alphabet(self):
        with open(self.alphabet_file_path, 'r') as file:
            return ast.literal_eval(file.read())

    def load_text(self):
        with open(self.text_file_path, 'r') as file:
            text = file.read().replace("\n", " ").lower()
            words = text.split(" ")
            return words, {word: np.asarray([self.alphabet_dict.get(char, 0) for char in word]) for word in words}

    def normalize_embedding(embedding, min_val=None, max_val=None):
        if min_val is None or max_val is None:
            all_values = np.concatenate(list(embedding.values()))
            min_val, max_val = all_values.min(), all_values.max()
        return {word: 2 * (emb - min_val) / (max_val - min_val) - 1 for word, emb in embedding.items()}

    def save_embedding(embedding, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(embedding, file)

    def check_key(dic, key):
        if key in dic.keys():
            dic.pop(key)
