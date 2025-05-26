import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('movies.csv')
texts = df['spoken_languages'].fillna('')

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

cos_sim = cosine_similarity(tfidf_matrix)

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(tfidf_matrix.toarray())

plt.figure(figsize=(10, 7))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], alpha=0.7, c='teal')

plt.title('Vizualization TF-IDF vectors')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.grid(True)
plt.tight_layout()
plt.show()