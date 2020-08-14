# -*- coding: utf-8 -*-
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

class JulContentBased():
    """docstring for Content"""

    def __init__(self, df):
        self.df_new = df[df.columns[1]]
        self.df_new.index = df['title']
        self.cv = CountVectorizer()
        
        #print(self.df_new)
        self.df_new = self.cv.fit_transform(self.df_new)
        #print("Changed:",self.df_new)
        self.cosine_sim = cosine_similarity(self.df_new,self.df_new)
        self.indices = df['title']

    def predict(self, name_film):
        #print(self.cosine_sim,"--------------------")
        #print(self.cosine_sim.shape)
        recom = self.recommendations(name_film, self.indices, self.cosine_sim)
        return recom
        
    def recommendations(self, title, indices, cosine_sim):

        recommended_movies = []
        # gettin the index of the movie that matches the title
        print(indices)
        idx = indices[indices == title].index[0]
        

        # creating a Series with the similarity scores in descending order
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
        #print(score_series,"-----&&&&&&&&&&&&&&&&&&&&&-")
        
        # getting the indexes of the 3 most similar movies
        top = list(score_series.iloc[0:5].index)
        # populating the list with the titles of the best 3 matching movies
        print("MovieList:")

        for i in top:
            print(indices[i])
            recommended_movies.append(i+1)
        
        return recommended_movies