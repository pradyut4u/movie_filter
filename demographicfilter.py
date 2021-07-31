import pandas as pd
import numpy as np

df = pd.read_csv("finalmovie.csv")
c = df["vote_average"].mean()
m = df["vote_count"].quantile(0.9)
j = df.copy().loc[df["vote_count"]>=m]

def ratedrating(x,m=m,c=c):
    v = x["vote_count"]
    r = x["vote_average"]
    return(
        (v/(v+m)*r)+(m/(v+m)*c)
    ) 

j["score"]=j.apply(ratedrating,axis = 1)
j = j.sort_values("score",ascending = False)
output = j[["original_title","movie_poster","release_date","runtime","vote_average","overview"]].head(20).values.tolist()
print(output)