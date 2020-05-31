import pandas as pd
import numpy as np

def post_timer(age, publish_date):
    """
    takes the age & publish_date of a book to output a random post date. The post_date is sampled randomly (&uniformly) from the range (start = 0, end = age)
    input: num_reviews, publish_date
    returns: post_date
    """
    #draw random day difference from age
    x = np.random.randint(0, age + 1, 1)

    #define timedelta
    offset = pd.Timedelta(x[0], 'D')

    #define post_date
    post_date = publish_date + offset

    return post_date

def post_applier(row):
    """
    applies the post_timer function to a whole data frame to output new post_date column. The column automatically has the right datetime format

    input: data frame row
    output: new post_date column
    """
    #get input variables
    age = row.age 
    publish_date = row.publish_date

    return post_timer(age, publish_date)




