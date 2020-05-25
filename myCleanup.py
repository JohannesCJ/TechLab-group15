# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:15:27 2020

@author: Johannes Heyn
"""

import argparse
from cleanup import replace_missing_list_column_values, one_hot_encode_genres, breakdown_publish_date

import pandas as pd




def main():
    argsfilenames = ["book_popularByDate.jl"]
    argsoutput = "books_popularByDate.csv"
    
    #argsfilenames = input("Enter filename")
    #argsoutput = input("Enter output name, e.g. books_list1.csv")
    
    dfs = [pd.read_json(filename, lines=True) for filename in argsfilenames]
    df = pd.concat(dfs)
    df = df.drop_duplicates(subset=['url'])

    replace_missing_list_column_values(df, 'genres')
    replace_missing_list_column_values(df, 'awards')

    one_hot_encode_genres(df)
    breakdown_publish_date(df)

    df['num_awards'] = df['awards'].apply(len)

    print(df.head())

    df.to_csv(argsoutput, index=False)




if __name__ == "__main__":
    main()
