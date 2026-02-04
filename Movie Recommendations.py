#Import Components
import pandas as pd
import numpy as np

#Read dataset Fils
FullDataset = pd.read_csv("C:/Users/25719211/OneDrive - Edge Hill University/Pro - Practice II/movies.csv")
MovieDataset = pd.read_csv("C:/Users/25719211/OneDrive - Edge Hill University/Pro - Practice II/movies.csv")

#Remove unecessary columns
MovieDataset.pop("index")
MovieDataset.pop("budget")
MovieDataset.pop("homepage")
MovieDataset.pop("id")
MovieDataset.pop("keywords")
MovieDataset.pop("spoken_languages")
MovieDataset.pop("overview")
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


#Output Datasets
FullDataset
MovieDataset

#this is a test
