**Company Emails:**

The dataset includes a company's email network where each node corresponds to a person at the company, and each edge indicates that at least one email has been sent between two people. The network also contains the node attributes Department and ManagementSalary. Department indicates the department in the company which the person belongs to, and ManagementSalary indicates whether that person is receiving a management position salary.

Using network G ('email_prediction.txt'), we identify the people in the network with missing values for the node attribute ManagementSalary and predict whether or not these individuals are receiving a management position salary.

To accomplish this, we create a matrix of node features using networkx, train a sklearn classifier on nodes that have ManagementSalary data, and predict a probability of the node receiving a management salary for nodes where ManagementSalary is missing.

The predictions will be given as the probability that the corresponding employee is receiving a management position salary. The evaluation metric is the Area Under the ROC Curve (AUC).

**New Connections Prediction**

We also predict future connections between employees of the network. The future connections information has been loaded into the variable future_connections (see code). The index is a tuple indicating a pair of nodes that currently do not have a connection, and the Future Connection column indicates if an edge between those two nodes will exist in the future, where a value of 1.0 indicates a future connection.

Using network G and future_connections, we identify the edges in future_connections with missing values and predict whether or not these edges will have a future connection.

To accomplish this, we create a matrix of features for the edges found in future_connections using networkx, train a sklearn classifier on those edges in future_connections that have Future Connection data, and predict a probability of the edge being a future connection for those edges in future_connections where Future Connection is missing. The predictions are given as the probability of the corresponding edge being a future connection and the evaluation metric is the Area Under the ROC Curve (AUC).

#################

The multigraph.py file quickly demosntrates how to convert raw data to a multigraph. 
