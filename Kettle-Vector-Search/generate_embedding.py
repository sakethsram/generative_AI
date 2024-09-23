import requests
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# initialize model for embedding 
m = SentenceTransformer('all-MiniLM-L6-v2')
# query handling 

def context(q, m_e, m_t):
    q = m.encode(q)
    dist, idx = search(q, m_e)  
    
    # conext handling
    T = 0.5
    if np.min(dist) > T:
        return "Sorry, i don't know about that product.anything else ?."
    
    return [m_t[i] for i in idx[0]]

def load(a):
    with open(a, 'r') as f:
        return f.read()

# generate embeddings for manual text
def gen_e(t):
    return m.encode(t)

#  vector search with FAISS
def search(q, e, top_k=5):
    # generate the  FAISS index for searching
    dim = e.shape[1]  
    i = faiss.IndexFlatL2(dim) #these 3 are for dimension,indexr and addition 
    i.add(e.astype('float32'))  

    dist, idx = i.search(np.array([q.astype('float32')]), top_k)
    return dist, idx



m = load('manual.txt')
m_l = m.split('\n')  
 
m_e = np.array([gen_e(l) for l in m_l])

while 1:
    q = input("Ask your question: ")     
    if q == 'done' or 'exit' or 'thanks' :break    
    res = context(q, m_e, m_l)
    print(res)
