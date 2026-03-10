#Import Components
import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Read dataset Files
FullDataset = pd.read_csv("C:/Users/26159295/OneDrive - Edge Hill University/PPractice2/movies.csv")
MovieDataset = pd.read_csv("C:/Users/26159295/OneDrive - Edge Hill University/PPractice2/movies.csv")

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





#Method to giverandom movie recommendation based on genre
def recommend_by_genre(genre):
    
    genre = genre.lower()
    
    filtered_movies = MovieDataset[
        MovieDataset['genres'].str.lower().str.contains(genre, na=False)
        ]
    
    if filtered_movies.empty:
        return "No Movies Found For This Genre. Please Try Again."
    
    recommend_movie = filtered_movies.sample(1)
    
    return recommend_movie['original_title'].values[0]


def recommend_by_director(director):
    
    director = director.lower()
    
    filtered_movies = MovieDataset[
        MovieDataset['director'].str.lower().str.contains(director, na=False)
        ]
    
    if filtered_movies.empty:
        return "No Movies Found From This Director. Please Try Again."
    
    recommend_movie = filtered_movies.sample(1)
    
    return recommend_movie['original_title'].values[0]


def recommend_by_movie_title(title):
    
    title = title.lower()
    
    selected_movie = MovieDataset[
        MovieDataset['original_title'].str.lower() == title
                                  ]
    if selected_movie.empty:
        return "No Movies found Similar to this Movie, Please check Spelling."
    
    selected_genre = selected_movie['genres'].values[0]
    
    filtered_movies = MovieDataset[
        (MovieDataset['genres'] == selected_genre) &
        (MovieDataset['original_title'].str.lower() !=title)
        ]
    
    if filtered_movies.empty:
        return "No similar Movies found."
    
    return filtered_movies['original_title'].sample(5)
    




#Movie Reccomendation Method
def recommend(movie_title, cosine_sim=cosine_sim):
    
    indices = pd.Series(MovieDataset.index, index=MovieDataset['original_title'])
    
    idx = indices[movie_title]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:6]
    
    movie_indices = [i[0] for i in sim_scores]
    
    return MovieDataset['original_title'].iloc[movie_indices]


# print(recommend("Robin Hood"))

user_genre = input("Enter a Genre: ")
print("Recommended Movie 1: ", recommend_by_genre(user_genre))
print("Recommended Movie 2: ", recommend_by_genre(user_genre))
print("Recommended Movie 3: ", recommend_by_genre(user_genre))
print("Recommended Movie 4: ", recommend_by_genre(user_genre))
print("Recommended Movie 5: ", recommend_by_genre(user_genre))

user_director = input("Enter a Director: ")
print("Recommended Movie by Director 1: ", recommend_by_director(user_director))
print("Recommended Movie by Director 2: ", recommend_by_director(user_director))
print("Recommended Movie by Director 3: ", recommend_by_director(user_director))
print("Recommended Movie by Director 4: ", recommend_by_director(user_director))
print("Recommended Movie by Director 5: ", recommend_by_director(user_director))

user_movie = input("Enter a Movie: ")
print("Recommended Similar Movies: ", recommend_by_movie_title(user_movie))



#Output Datasets
FullDataset
MovieDataset
