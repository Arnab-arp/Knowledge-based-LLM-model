# Vector store + retrieval logic Implementation 

# Sentence transformer docs: https://sbert.net/docs/sentence_transformer/usage/usage.html
# My Guide: https://www.pinecone.io/learn/series/faiss/faiss-tutorial/

import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer as ST


class VectorRetriever:
    def __init__(self, data_dir = 'data'):
        self.root_data = data_dir
        self.docs = []
        self.index = None
        self.model = ST('all-MiniLM-L6-v2')
        self.load_data()  # loading and storing the data during class initialization

    def load_data(self):
        ''' 
        (1) Loading all the txt source data files from the data directory 
        (2) Creating Embeddings using Sentence Trainsformer
        (3) Creating Faiss indexes
        '''

        for file in os.listdir(self.root_data):
            file_path = os.path.join(self.root_data, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = f.read().strip()
                self.docs.append(
                    {
                        'file_id': file,
                        'text_info': data
                    }
                )
        
        # Data embedding generation
        all_texts = [doc['text_info'] for doc in self.docs]
        data_embeddings = self.model.encode(
            all_texts,
            show_progress_bar=False
        )
        # print(len(data_embeddings)) -- 10
        # print(len(data_embeddings[0])) -- 384
        # print(data_embeddings.shape) -- (10, 384)

        # Faiss indexing.
        d = data_embeddings.shape[1]
        self.index = faiss.IndexFlatL2(d)
        self.index.add(data_embeddings.astype('float32'))

    def retrieve(self, query, k=5):
        '''
        This method retrives the best matching file_names and its content
        from the faiss vector db in a list[dictionary] format.
        Query: User query or prompt
        k: top k matches; default : 3
        '''
        query_embedding = self.model.encode([query])
        distance, indices = self.index.search(query_embedding.astype('float32'), k=k)
        # print(f'--- Distance: {distance}\n--- Indices: {indices}')

        # returning the original file names and data from the faiss index output
        return [self.docs[i] for i in indices[0]]

if __name__ == '__main__':
    vr = VectorRetriever()
    print(vr.retrieve(query='SaaS'))
