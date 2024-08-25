#!/usr/bin/python3
from mrjob.job import MRJob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

nltk.download('stopwords', force=True, download_dir='/home/hdoop/nltk_data')
nltk.download('wordnet', force=True, download_dir='/home/hdoop/nltk_data')
nltk.download('punkt', force=True, download_dir='/home/hdoop/nltk_data')

class MRQueryGrouping(MRJob):

    def mapper(self, _, line):
        # Split the CSV line into fields
        fields = line.strip().split(',')
        # Check if the record is valid (contains 11 fields)
        if len(fields) == 13:
            # Extract the query text (field index 10)
            query = fields[12].lower()
            
            # Tokenize the query text
            tokens = word_tokenize(query)
            
            # Remove punctuation and stopwords
            tokens = [token for token in tokens if token not in string.punctuation and token not in stopwords.words('english')]
            
            # Lemmatize the tokens
            lemmatizer = WordNetLemmatizer()
            tokens = [lemmatizer.lemmatize(token) for token in tokens]
            
            # Emit key-value pairs for each token in the query
            for token in tokens:
                print(f"{token}, {query}")
                yield json.dumps(token), json.dumps(query)

    def reducer(self, key, values):
        # Collect all queries corresponding to the same token
        queries = [json.loads(value) for value in values]
        
        # Calculate TF-IDF vectors for the queries
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(queries)
        
        # Calculate pairwise cosine similarity between queries
        similarity_matrix = cosine_similarity(tfidf_matrix)
        
        # Group similar queries based on cosine similarity threshold
        grouped_queries = {}
        for i in range(len(similarity_matrix)):
            for j in range(i+1, len(similarity_matrix)):
                if similarity_matrix[i,j] > 0.7:  # Adjust similarity threshold as needed
                    grouped_queries.setdefault(i, []).append(queries[j])
        
        # Yield the grouped queries
        for group_id, similar_queries in grouped_queries.items():
            yield key, similar_queries

if __name__ == '__main__':
    MRQueryGrouping.run()
