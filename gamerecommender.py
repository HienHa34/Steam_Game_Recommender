import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class GameRecommender():

def __init__(self):


def fit(self,df,values, index, columns):
		self.df = df
		self.utility_mat = df.pivot_table(values =values, index = index, columns = columns)
		self.sim_mat = cosine_similarity(self.utility_mat.fillna(0).T)

def predict(self,user_id,neighbors):

    sorted_sim_idx = np.argsort(np.array(self.sim_mat))
    nbh = sorted_sim_idx[:, -self.neighbors:]
    items_rated = np.array(self.utility_mat.iloc[user_id].fillna(0)).nonzero()
    pred = np.zeros(self.sim_mat.shape[0])

    for item_to_rate in range(self.sim_mat.shape[0]):

        similar_items = np.intersect1d(nbh[item_to_rate], items_rated, assume_unique =True)
        pred[item_to_rate] = ((self.sim_mat.iloc[item_to_rate,similar_items].values*\
                               self.utility_mat.iloc[user_id,similar_items].values).sum())\
                                /(self.sim_mat.iloc[item_to_rate,similar_items].sum())

    preds= np.nan_to_num(pred)
    return preds

def	predict_all (self, neighbors):
		predictions = [self.predict(user_id,neighbors) for user_id in range(self.utility_mat.shape[0])]
		self.predictions = predictions
		return predictions


def evaluate(self,actual):
		hits = 0
		for i, pred in enumerate(self.predictions):
    	top_10 = pred.argsort()[::-1][:10]
    	test = actual[i]
    	hits += len(np.intersect1d(top_10,test))
		avg_precision = hits/len(self.predictions)
		return avg_precision


