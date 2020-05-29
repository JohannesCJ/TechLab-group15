# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:15:27 2020

@author: Johannes Heyn
"""

import argparse
from cleanup import replace_missing_list_column_values, one_hot_encode_genres, breakdown_publish_date

import pandas as pd




def main():
    argsfilenames = ["data/all_books_popularByDate2.jl"]
    argsoutput = "data/all_books_popularByDate2.csv"
    
    #argsfilenames = input("Enter filename")
    #argsoutput = input("Enter output name, e.g. books_list1.csv")
    
    dfs = [pd.read_json(filename, lines=True) for filename in argsfilenames]
    df = pd.concat(dfs)
    df = df.drop_duplicates(subset=['url'])

    replace_missing_list_column_values(df, 'genres')
    replace_missing_list_column_values(df, 'awards')
    # replace_missing_list_column_values(df, 'publish_date')
    # replace_missing_list_column_values(df, 'num_ratings')
    # replace_missing_list_column_values(df, 'num_reviews')
    # replace_missing_list_column_values(df, 'avg_rating')
    # replace_missing_list_column_values(df, 'num_pages')
    # replace_missing_list_column_values(df, 'awards')
    # replace_missing_list_column_values(df, 'original_publish_year')
    # replace_missing_list_column_values(df, 'series')
    

    one_hot_encode_genres(df)
    #breakdown_publish_date(df)

    df['num_awards'] = df['awards'].apply(len)

    print(df.head())
    print(df.info())

    df.to_csv(argsoutput, index=False)




if __name__ == "__main__":
    main()
