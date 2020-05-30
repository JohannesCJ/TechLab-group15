import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

#other:
from ast import literal_eval
from collections import Counter

#get the counts of all genres in the genre column
def gen_dicker(genre_col):
    dic = {}
    for value in genre_col:
        try:
            liste = literal_eval(value)
            for genre in liste:
                if genre not in dic:
                    dic[genre] = 1
                else:
                    dic[genre] += 1
        except ValueError:
            continue

    return dic