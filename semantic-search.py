from datasets import load_dataset
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# Load the dataset
dataset = load_dataset('openwebtext', split='train[:2000]')

# Preprocess the dataset
texts = [simple_preprocess(article['text']) for article in dataset]

# Train a Word2Vec model
model = Word2Vec(texts, vector_size=200, window=5, min_count=1, workers=4)

# Find the most similar words to "politics", "global", and "economy
similar_words = model.wv.most_similar(positive=['politics', 'global', 'economy'], topn=10)
print(similar_words)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Extract the words and their vectors
words = [word for word, _ in similar_words]
word_vectors = np.array([model.wv[word] for word in words])

# Perform dimensionality reduction using t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=9)
word_vectors_2d = tsne.fit_transform(word_vectors)

# Plot the words and their 2D vectors
plt.figure(figsize=(8, 8))
plt.scatter(word_vectors_2d[:, 0], word_vectors_2d[:, 1], c='red', edgecolors='k')

# Annotate the points with their respective words
for i, word in enumerate(words):
    plt.annotate(word, xy=(word_vectors_2d[i, 0], word_vectors_2d[i, 1]), xytext=(5, 2),
                 textcoords='offset points', ha='right', va='bottom')

plt.title('t-SNE visualization of word vectors')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()