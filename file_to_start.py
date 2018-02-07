import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import ast
import itertools
import main_recommend


user_feat = pd.read_csv('user_features.csv')
new_user_feat = pd.read_csv('new_user_feat.csv')

#user_feat['Calories'] = np.random.randint(150,500, size=len(user_feat))
#user_feat['meal_size_rating'] = pd.DataFrame(np.random.randint(0,3, size = (len(user_feat),1)))
#user_feat['previous_meal_size'] = pd.DataFrame(np.random.randint(0,3, size = (len(user_feat),1)))


spice_feat = pd.read_excel('test4.xls')
spice_feat = spice_feat.iloc[:,:7]


def getrecommendation(user_id,user_feat = user_feat,new_user_feat = new_user_feat):
    if user_id not in (new_user_feat['user_guid'].values):
        #print ("enter the correct user_id between 500 and "+str(500-2+len(new_user_feat['user_guid'])))
        return

    indexer = np.where(new_user_feat['user_guid']==user_id)[0]
    indexer = indexer[0]
    #print indexer
    result = main_recommend.main_recommendation(new_user_feat,user_feat,indexer)
    #print result
    recolist = result['recommend_list']
    new_meal_size = result['next_meal']
    #print recolist[0]
    #print new_meal_size
    return result

# print(getrecommendation(520))
