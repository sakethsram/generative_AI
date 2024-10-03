import faiss
import numpy as np
from genai.embeddings import get_embedding

# Load FAISS index
index = faiss.read_index('recipes_index.faiss')

# Load recipe names from the saved file
with open('recipes_index.txt', 'r') as f:
    recipes = f.readlines()

# Input ingredients from the user
user_input = input("Enter the ingredients you have, separated by commas: ")

# Generate embedding for the user's input ingredients
user_embedding = get_embedding(user_input)

# Perform search in the FAISS index
D, I = index.search(np.array([user_embedding]), k=3)  # Return top 3 matches

# Display matching recipes
print("Here are the best matching recipes:")
for idx in I[0]:
    print(recipes[idx].strip())

