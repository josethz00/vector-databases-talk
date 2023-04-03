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
