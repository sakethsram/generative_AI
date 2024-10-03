import requests
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Initialize model for embedding generation
m = SentenceTransformer('all-MiniLM-L6-v2')

#opening the manual.txt
def load(a):
    with open(a, 'r') as f:
        return f.read()

# Generate embeddings for manual text
def gen_e(t):
    return m.encode(t)

# Perform vector search using FAISS
def search(q, e, top_k=5):#query E,e=array of E, top_k = nearest k cluster
    # Create a FAISS index for searching
    dim = e.shape[1]  # Get the embedding dimension and create the FAISS index
    i = faiss.IndexFlatL2(dim)  # find the nearest embeddings 
    i.add(e.astype('float32'))  # Add the embeddings to the index

    dist, idx = i.search(np.array([q.astype('float32')]), top_k)  # Ensure query is the right type
    return dist, idx

# Query handling 
def handle_query(q, man_e, man_t):
    q = m.encode(q)
    dist, idx = search(q, man_e)  
    
    # Out of context handling
    T = 1
    if np.min(dist) > T:
        return "Sorry, I don't know about that product. Ask about some other question."
    
    return [man_t[i] for i in idx[0]]

# Load manual and generate embeddings
manual = load('product_manual.txt')
man_l = manual.split('\n')  
man_e = np.array([gen_e(l) for l in man_l])

while True:
    q = input("Ask your question: ")        
    res = handle_query(q, man_e, man_l)
    print(res)
