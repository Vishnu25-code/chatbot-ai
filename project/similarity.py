import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityEngine:
    """
    Handles similarity search using TF-IDF and Cosine Similarity.
    This provides lightweight NLP question matching without heavy models.
    """
    def __init__(self, corpus):
        self.corpus = corpus
        # Initialize the vectorizer to create unigram and bigram features 
        # and remove basic english stop words.
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        # Fit and transform the corpus into TF-IDF vectors
        if self.corpus:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)
        else:
            self.tfidf_matrix = None

    def find_best_match(self, query):
        """
        Finds the closest matching question from the corpus.
        Returns the index of the highest match and the confidence score.
        """
        if not self.corpus:
            return -1, 0.0

        # Vectorize the user's query
        query_vector = self.vectorizer.transform([query])
        
        # Calculate cosine similarity between the query and all questions in the corpus
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        
        # Get the index of the highest similarity score
        best_idx = np.argmax(similarities)
        best_score = similarities[best_idx]
        
        return best_idx, best_score
