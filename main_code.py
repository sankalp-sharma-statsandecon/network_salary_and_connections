#Import libraries

import networkx as nx
import pandas as pd
import numpy as np
import pickle

G = nx.read_gpickle('email_prediction.txt')

import warnings as wr
wr.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier

df = pd.DataFrame(index=G.nodes())
df['Department'] = pd.Series(nx.get_node_attributes(G, 'Department'))
df['ManagementSalary'] = pd.Series(nx.get_node_attributes(G, 'ManagementSalary')).fillna(2)
df['clustering'] = pd.Series(nx.clustering(G))
df['degree'] = pd.Series(G.degree())
dfNaN = df[df['ManagementSalary'] == 2]
df = df[(df['ManagementSalary'] == 0)|(df['ManagementSalary'] == 1)]
df['dept'] = df['Department'].astype('category').cat.codes
df['mgmt'] = df['ManagementSalary'].astype('category').cat.codes
dfNaN['dept'] = dfNaN['Department'].astype('category').cat.codes
X = df[['dept','clustering','degree']]
y = df['mgmt']
clf = (RandomForestClassifier(n_jobs = -1, n_estimators = 100, random_state = 0)
           .fit(X, y))
X_test = dfNaN[['dept','clustering','degree']]
d = {'no.': dfNaN.index, 'probs': clf.predict_proba(X_test)[:,1]}
dfnew = pd.DataFrame(data=d).set_index('no.')
del dfnew.index.name
del dfnew.columns.name 
dfnew['probs'].astype(np.float64)

#Results: 

#1     0.00
#2     0.56
#5     0.92
#8     0.37
#14    0.09

future_connections = pd.read_csv('Future_Connections.csv', index_col=0, converters={0: eval})

fc = future_connections
fc['n1'] = [fc.index[t][0] for t in range(len(fc['Future Connection']))]
fc['n2'] = [fc.index[t][1] for t in range(len(fc['Future Connection']))]
fc = fc.reset_index()
#fc1 = fc[(fc['Future Connection'] == 0)|(fc['Future Connection'] == 1)]
G1 = nx.from_pandas_dataframe(fc, 'n1', 'n2', edge_attr='Future Connection')
df = pd.DataFrame(index=G1.edges())
df['weight'] = pd.Series(nx.get_edge_attributes(G1, 'Future Connection'))
df['preferential attachment'] = [i[2] for i in nx.preferential_attachment(G1, df.index)]
df['Common Neighbors'] = df.index.map(lambda edge: len(list(nx.common_neighbors(G1, edge[0], edge[1]))))
df1 = df[(df['weight'] == 0)|(df['weight'] == 1)]
X = df1[['preferential attachment','Common Neighbors']]
y = df1['weight']

from sklearn.ensemble import GradientBoostingClassifier
clf2 = GradientBoostingClassifier(learning_rate = 0.1, random_state = 0, n_estimators = 1000).fit(X, y)
df['weight'] = df['weight'].fillna(2)
dfNaN = df[df['weight'] == 2]
X_test = dfNaN[['preferential attachment','Common Neighbors']]
d = {'no.': dfNaN.index, 'probs': clf2.predict_proba(X_test)[:,1]}
dfnew1 = pd.DataFrame(data=d).set_index('no.')
del dfnew1.index.name
return dfnew1['probs'].astype(np.float64)
