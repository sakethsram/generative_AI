import faiss
import numpy as np
from genai.embeddings import get_embedding

# Load ingredients from ingredients.txt
with open('ingredients.txt', 'r') as f:
    ingredients = f.readlines()

# Generate embeddings for each set of ingredients
ingredient_embeddings = [get_embedding(ingredient.strip()) for ingredient in ingredients]

# Convert embeddings to a numpy array
embedding_matrix = np.array(ingredient_embeddings)

# Initialize FAISS index for L2 distance (Euclidean)
index = faiss.IndexFlatL2(embedding_matrix.shape[1])
index.add(embedding_matrix)

# Save FAISS index to a file for later use
faiss.write_index(index, 'recipes_index.faiss')

# Load recipe names from recipes.txt
with open('recipes.txt', 'r') as f:
    recipes = f.readlines()

# Save recipe names into a separate file
with open('recipes_index.txt', 'w') as f:
    for recipe in recipes:
        f.write(recipe.strip() + "\n")

print("Embeddings generated and stored successfully!")
