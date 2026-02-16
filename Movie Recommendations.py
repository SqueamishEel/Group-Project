#Import Components
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Read dataset Fils
FullDataset = pd.read_csv("C:/Users/sahil/OneDrive/PP2/movies.csv")
MovieDataset = pd.read_csv("C:/Users/sahil/OneDrive/PP2/movies.csv")

#Remove unecessary columns
MovieDataset.pop("index")
MovieDataset.pop("budget")
MovieDataset.pop("homepage")
MovieDataset.pop("id")
MovieDataset.pop("keywords")
MovieDataset.pop("spoken_languages")
MovieDataset.pop("popularity")
MovieDataset.pop("production_companies")
MovieDataset.pop("production_countries")
MovieDataset.pop("revenue")
MovieDataset.pop("status")
MovieDataset.pop("tagline")
MovieDataset.pop("title")
MovieDataset.pop("vote_count")
MovieDataset.pop("cast")
MovieDataset.pop("crew")


#Removing Missing Values from dataset
MovieDataset['runtime'] = MovieDataset['runtime'].replace(0, np.nan)
MovieDataset['runtime'].fillna(MovieDataset['runtime'].median(), inplace = True)

MovieDataset['Joined'] = (
    MovieDataset['genres'].fillna('') + ' ' +
    MovieDataset['original_language'].fillna('') + ' ' +
    MovieDataset['original_title'].fillna('') + ' ' +
    MovieDataset['release_date'].fillna('') + ' ' +
    MovieDataset['director'].fillna('')
)
MovieDataset['Joined'] = MovieDataset['Joined'].str.lower()

#Converting Text to Numerical vectors via TFIDF
tfidf = TfidfVectorizer(stop_words = 'english')

tfidf_matrix = tfidf.fit_transform(MovieDataset['Joined'])


#Calculates Cosine Similarity, 0-90 degrees
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


#Movie Reccomendation Method
def recommend(movie_title, cosine_sim=cosine_sim):
    
    indices = pd.Series(MovieDataset.index, index=MovieDataset['original_title'])
    
    idx = indices[movie_title]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:6]
    
    movie_indices = [i[0] for i in sim_scores]
    
    return MovieDataset['original_title'].iloc[movie_indices]



print(recommend("Robin Hood"))

#Output Datasets
FullDataset
MovieDataset
