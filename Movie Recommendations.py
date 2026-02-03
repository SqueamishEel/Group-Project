#Import Components
import pandas as pd
import numpy as np

#Read dataset Fils
FullDataset = pd.read_csv("C:/Users/25719211/OneDrive - Edge Hill University/Pro - Practice II/movies_dataset.csv")
MovieDataset = pd.read_csv("C:/Users/25719211/OneDrive - Edge Hill University/Pro - Practice II/movies_dataset.csv")

#Remove unecessary columns
MovieDataset.pop("BudgetUSD")
MovieDataset.pop("US_BoxOfficeUSD")
MovieDataset.pop("Global_BoxOfficeUSD")
MovieDataset.pop("Opening_Day_SalesUSD")
MovieDataset.pop("One_Week_SalesUSD")
MovieDataset.pop("NumVotesIMDb")
MovieDataset.pop("ReleaseYear")
MovieDataset.pop("NumVotesRT")

#Replacing Missing Values with NaN
MovieDataset['IMDbRating'] = MovieDataset['IMDbRating'].replace(0, np.nan)
MovieDataset['IMDbRating'].fillna(MovieDataset['IMDbRating'].median(), inplace = True)

#Output Datasets
FullDataset
