# -*- coding: utf-8 -*-
from math import sqrt
import pandas as pd
# from optparse import OptionParser
# import os
# import sys
# os.chdir('..')
# cwd = os.getcwd() + '/Dataset'
# sys.path.insert(0, cwd)#'/path/to/application/app/folder')

# #rec = os.getcwd()+'/'
# from recommendation_data import datasets
# 
class JulCollaborative(object):
    """docstring for JulCollaborative"""
    def __init__(self, df):
        self.dataset = df

#load data from dataset

    def similarity_score(self, person1, person2):

        # this Returns the ration euclidean distancen score of person 1 and 2

        # To get both rated items by person 1 and 2
        both_viewed = {}

        for item in dataset[person1]:
            if item in dataset[person2]:
                both_viewed[item] = 1
            
            # The Conditions to check if they both have common rating items
            if len(both_viewed) == 0:
                return 0

            # Finding Euclidean distance
            sum_of_eclidean_distance = []

            for item in dataset[person1]:
                if item in dataset[person2]:
                    sum_of_eclidean_distance.append(pow(dataset[person1][item] - dataset[person2][item], 2))
            sum_of_eclidean_distance = sum(sum_of_eclidean_distance)
            
            return 1/(1+sqrt(sum_of_eclidean_distance))

    def person_correlation(self, person1, person2):

       # To get both rated items
        both_rated = {}
        for item in list(person1[person1.columns[2]]):
            if item in list(person2[person2.columns[2]]):
                both_rated[item] = 1

        number_of_ratings = len(both_rated)

        # Checking for ratings in common
        if number_of_ratings == 0:
            return 0
        # Add up all the preferences of each user
        person1_preferences_sum=0
        person2_preferences_sum=0
        person2_square_preferences_sum=0
        person1_square_preferences_sum=0
        product_sum_of_both_users=0
        for item in both_rated:
            per_comm=list(person1[person1['movie_id']==item].rating)
            i=per_comm[0]
            person1_preferences_sum+=i
            person1_square_preferences_sum+=i*i
            per_ra=i
            other_comm=list(person2[person2['movie_id']==item].rating)
            i=other_comm[0]
            person2_preferences_sum+=i
            person2_square_preferences_sum+=i*i
            oth_ra=i
            product_sum_of_both_users+=per_ra*oth_ra
        #print(product_sum_of_both_users,"sdjfjsdhfudfhusdf--------------")
        #print(person1_preferences_sum,"sd--------------")
        #print()
        #print(person2_preferences_sum)    
    

        numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
        denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))

        if denominator_value == 0:
            return 0
        else:
            r = numerator_value / denominator_value
            return r

    def most_similar_users(self, person, number_of_users=24):

        # returns the number_of_users (similar persons) for a given specific person
        scores = [(self.person_correlation(person, other_person), other_person) for other_person in self.dataset if other_person != person]

        # Sort the similar persons so the highest scores person will appear at the first
        scores.sort()
        scores.reverse()
        return scores[0:number_of_users]
            
    def user_recommendations(self, person):
        # Gets recommendations for a person by using a weighted average of every other user's rankings
        totals = {}
        simSums = {}
        #rankings_list =[]
        person_ratings={}
        person_matrix=self.dataset[self.dataset['user_id']==person]
        #print("jsdbhsdbf")
        #print(person_matrix)
        #print(self.dataset.user_id.unique())
        for other in self.dataset.user_id.unique():
            # don't compare me to myself
            
            if other == person:
                continue
            #print(other)
            other_matrix=self.dataset[self.dataset['user_id']==other]
            #print(other_matrix)
            sim = self.person_correlation(person_matrix, other_matrix)
            #print ">>>>>>>",sim
            #print("ksdhjhsdjhdsf",sim)
            # ignore scores of zero or lower
            if sim <=0: 
                continue
            for item in other_matrix.movie_id.unique():

                # only score movies i haven't seen yet
                #print()
                if 'true' not in list(person_matrix['movie_id']==item):

                # Similrity * score
                    totals.setdefault(item,0)
                    totals[item] += list(other_matrix[other_matrix['movie_id']==item].rating)[0]* sim
                    # sum of similarities
                    simSums.setdefault(item,0)
                    simSums[item]+= sim

            # Create the normalized list

        rankings = [(total/simSums[item],item) for item,total in totals.items()]
        rankings.sort()
        rankings.reverse()
        # returns the recommended items
        recommendataions_list = [recommend_item for score,recommend_item in rankings]
        print("ksncjjsdfh")
        print(recommendataions_list)
        return recommendataions_list, rankings
            
    def main():
        #optParser = OptionParser()

        #optParser.add_option('-n', '--nama', dest='nama',
         #   help='Nama pelanggan',
          #  type='string',
           # default=None)

        #(options, args) = optParser.parse_args()
        #nama = options.nama
        recommendation = self.user_recommendations('jul')
        #print('Recommendation for jul: ',recommendation)
        return recommendation
        #print('Person correlation: ',person_correlation('jul','Hania'))
        #print('Similarity score: ',similarity_score('jul','Hania'))
        #print('most similar person to jul: ',most_similar_users('jul',24))