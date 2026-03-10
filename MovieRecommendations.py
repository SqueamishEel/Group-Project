import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read dataset Files
FullDataset = pd.read_csv(r"C:/Users/fitz_/Downloads/movies.csv")
MovieDataset = pd.read_csv(r"C:/Users/fitz_/Downloads/movies.csv")

USER_HISTORY = "user_ratings.csv"

# Remove unnecessary columns
MovieDataset.pop("index")
MovieDataset.pop("budget")
MovieDataset.pop("homepage")
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

# Removing Missing Values from dataset
MovieDataset["runtime"] = MovieDataset["runtime"].replace(0, np.nan)
MovieDataset["runtime"] = MovieDataset["runtime"].fillna(
    MovieDataset["runtime"].median()
)

MovieDataset["genres"] = MovieDataset["genres"].fillna("").astype(str)
MovieDataset["original_language"] = MovieDataset["original_language"].fillna("").astype(str)
MovieDataset["original_title"] = MovieDataset["original_title"].fillna("").astype(str)
MovieDataset["release_date"] = MovieDataset["release_date"].fillna("").astype(str)
MovieDataset["director"] = MovieDataset["director"].fillna("").astype(str)
MovieDataset["overview"] = MovieDataset["overview"].fillna("").astype(str)

MovieDataset["Joined"] = (
        MovieDataset["genres"] + " " +
        MovieDataset["original_language"] + " " +
        MovieDataset["original_title"] + " " +
        MovieDataset["release_date"] + " " +
        MovieDataset["director"] + " " +
        MovieDataset["overview"]
)
MovieDataset["Joined"] = MovieDataset["Joined"].str.lower()

# Converting Text to Numerical vectors via TFIDF
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(MovieDataset["Joined"])

# Calculates Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Lookups
indices = pd.Series(MovieDataset.index, index=MovieDataset["original_title"]).drop_duplicates()
id_to_idx = pd.Series(MovieDataset.index, index=MovieDataset["id"]).drop_duplicates()


# Movie Recommendation Method
def recommend(movie_title, cosine_sim=cosine_sim):
    idx = indices[movie_title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]

    movie_indices = [i[0] for i in sim_scores]

    return MovieDataset.iloc[movie_indices]


def year_only(text):
    return text[:4] if isinstance(text, str) and len(text) >= 4 else ""


def apply_filters(genre, director="", year="", language=""):
    FilteredDataset = MovieDataset.copy()

    genre = genre.strip()
    if genre:
        parts = [p.strip() for p in genre.replace(",", " ").split() if p.strip()]
        for p in parts:
            FilteredDataset = FilteredDataset[
                FilteredDataset["genres"].str.contains(p, case=False, na=False, regex=False)
            ]

    if director.strip():
        FilteredDataset = FilteredDataset[
            FilteredDataset["director"].str.contains(director.strip(), case=False, na=False, regex=False)
        ]

    if year.strip():
        FilteredDataset = FilteredDataset[
            FilteredDataset["release_date"].str.contains(year.strip(), case=False, na=False, regex=False)
        ]

    if language.strip():
        FilteredDataset = FilteredDataset[
            FilteredDataset["original_language"].str.contains(language.strip(), case=False, na=False, regex=False)
        ]

    return FilteredDataset


def top_filtered_movies(genre, director="", year="", language="", n=20):
    FilteredDataset = apply_filters(genre, director, year, language)
    return FilteredDataset.sort_values("vote_average", ascending=False).head(n).reset_index(drop=True)


def get_history(user_id):
    if not os.path.exists(USER_HISTORY):
        return pd.DataFrame(columns=["user_id", "movie_id", "rating"])

    HistoryDataset = pd.read_csv(USER_HISTORY)
    return HistoryDataset[HistoryDataset["user_id"] == user_id].copy()


def save_rating(user_id, movie_id, rating):
    NewRow = pd.DataFrame([{
        "user_id": user_id,
        "movie_id": int(movie_id),
        "rating": int(rating)
    }])

    if os.path.exists(USER_HISTORY):
        HistoryDataset = pd.read_csv(USER_HISTORY)
        HistoryDataset = HistoryDataset[
            ~((HistoryDataset["user_id"] == user_id) &
              (HistoryDataset["movie_id"] == int(movie_id)))
        ]
        HistoryDataset = pd.concat([HistoryDataset, NewRow], ignore_index=True)
    else:
        HistoryDataset = NewRow

    HistoryDataset.to_csv(USER_HISTORY, index=False)


def recommend_from_history(user_id, filtered_df, n=20, min_rating=4):
    HistoryDataset = get_history(user_id)
    liked = HistoryDataset[HistoryDataset["rating"] >= min_rating]

    if liked.empty:
        raise ValueError("Rate some movies 4 or 5 first.")

    seed_indices = [int(id_to_idx[mid]) for mid in liked["movie_id"].tolist() if mid in id_to_idx.index]

    if not seed_indices:
        raise ValueError("Rated movies not found.")

    scores = cosine_sim[seed_indices].sum(axis=0)

    rated_ids = set(HistoryDataset["movie_id"].tolist())
    CandidateDataset = filtered_df[~filtered_df["id"].isin(rated_ids)]

    if CandidateDataset.empty:
        raise ValueError("No movies left after removing rated ones.")

    ranked = sorted(CandidateDataset.index.tolist(), key=lambda i: scores[i], reverse=True)[:n]
    return MovieDataset.loc[ranked].reset_index(drop=True)


