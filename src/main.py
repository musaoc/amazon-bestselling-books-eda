"""
Amazon Top 50 Bestselling Books (2009–2019) — Exploratory Data Analysis
An exploratory data analysis and market intelligence project examining a decade of Amazon bestselling books to extract actionable consumer trends, pricing dynamics, and author market share.

Original Kaggle Notebook: https://www.kaggle.com/code/lazer999/top-selling-books-amazon
Author: Muhammad Musa Khan (Kaggle Master: https://kaggle.com/lazer999)
"""

import os
import sys
import warnings
warnings.filterwarnings("ignore")

# --- Smart Dataset Path Resolution ---
def _resolve_data_path(file_path):
    """Checks local and data/ directories if dataset path is missing."""
    if os.path.exists(file_path):
        return file_path
    base = os.path.basename(file_path)
    candidates = [
        base,
        os.path.join("data", base),
        os.path.join("..", "data", base),
        file_path.replace("/kaggle/input/", "data/"),
        file_path.replace("../input/", "data/"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return file_path

# --- Pipeline Execution ---

# --- Cell 1 ---
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# --- Cell 2 ---
dataset_url = '../input/amazon-top-50-bestselling-books-2009-2019/bestsellers with categories.csv'

# --- Cell 3 ---
df = pd.read_csv(dataset_url)
df.head()

# --- Cell 4 ---
df.info()

# --- Cell 5 ---
### to get an overview of the dataframe
df.describe()

# --- Cell 6 ---
r,c = df.shape
print(f"The dataset has {r} rows and {c} columns.")

# --- Cell 7 ---
#To rename the columns and make it easy to use:
df.columns=['name','author','user_rating','reviews','price','year','genre']

# --- Cell 8 ---
df.head()

# --- Cell 9 ---
#To check if there is any null value in the dataframe
df.isnull().sum()

# --- Cell 10 ---
#For total number of different books
len(df.name.unique())

# --- Cell 11 ---
df['estimated_profit']=df.reviews*df.price

# --- Cell 12 ---
# setting the background to be dark, it looks cool with this ;)
sns.set_style('darkgrid')
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (9, 5)
plt.rcParams['figure.facecolor'] = '#00000000'

# --- Cell 13 ---
fiction_df_values=df[df.genre=='Fiction']
len(fiction_df_values)

# --- Cell 14 ---
Nfiction_df=df[df.genre=='Non Fiction']
len(Nfiction_df)

# --- Cell 15 ---
genre_dist=df.genre.value_counts()
genre_dist

# --- Cell 16 ---
sns.barplot(x=genre_dist.index,y=genre_dist);

# --- Cell 17 ---
plt.pie([240,310],labels=['Fiction','Non Fiction'],autopct='%.0f%%');

# --- Cell 18 ---
df.groupby('genre')['user_rating'].mean()

# --- Cell 19 ---
#Distribution of ratings
sns.histplot(data=df.user_rating,bins=10)
plt.xlabel("Ratings");

# --- Cell 20 ---
# Relationship of ratings with time.
sns.lineplot(y=df.user_rating,x=df.year,hue=df.genre);
plt.ylabel("Ratings")
plt.xlabel("Years");

# --- Cell 21 ---
sns.lmplot(y='user_rating',x='price',data=df)
plt.ylabel('Ratings')
plt.xlabel('Price');

# --- Cell 22 ---
df.groupby('genre')['user_rating'].mean()

# --- Cell 23 ---
sns.barplot(x=df.year,y=df.estimated_profit,hue=df.genre)
plt.xlabel('Years')
plt.ylabel("Eearned(millions)")
plt.title('Money earned each year');

# --- Cell 24 ---
genre_average=df.groupby(['genre'])['estimated_profit'].mean()

# --- Cell 25 ---
sns.barplot(x=genre_average.index,y=genre_average);

# --- Cell 26 ---
rich_df=df.groupby('name')['estimated_profit'].max()
rich_df=rich_df.sort_values(ascending=False).head(10)
rich_df

# --- Cell 27 ---
sns.barplot(x=rich_df,y=rich_df.index)
plt.xlabel("Earned(millions)")
plt.ylabel("Books")
plt.title('Earning by Books');

# --- Cell 28 ---
most_earning_book_per_year=df[df.groupby('year')['estimated_profit'].transform(max) == df['estimated_profit']]
most_earning_book_per_year

# --- Cell 29 ---
most_earning_book_per_year=most_earning_book_per_year.sort_values('year').set_index('year')

# --- Cell 30 ---
most_earning_book_per_year

# --- Cell 31 ---
genres_per_year_mean=df.groupby(['year','genre'])['estimated_profit'].mean().round(2)

# --- Cell 32 ---
pd.DataFrame(genres_per_year_mean)

# --- Cell 33 ---
Earning_Graph=df.groupby('year')['estimated_profit'].sum()

# --- Cell 34 ---
sns.lineplot(data=Earning_Graph)
plt.xlabel('Year')
plt.ylabel("Earned")
plt.title("EARNING PER YEAR")
plt.figure(figsize=(12,12));

# --- Cell 35 ---
authors=df.groupby('author')['estimated_profit'].sum()

# --- Cell 36 ---
authors=authors.sort_values(ascending=False).head(10)
authors

# --- Cell 37 ---
sns.barplot(y=authors.index,x=authors)
plt.title('The Money Makers ');



if __name__ == "__main__":
    print("Pipeline execution complete.")
