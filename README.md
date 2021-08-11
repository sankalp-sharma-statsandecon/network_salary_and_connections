Company Emails:

The dataset includes a company's email network where each node corresponds to a person at the company, and each edge indicates that at least one email has been sent between two people. The network also contains the node attributes Department and ManagementSalary. Department indicates the department in the company which the person belongs to, and ManagementSalary indicates whether that person is receiving a management position salary.

Using network G ('email_prediction.txt'), we identify the people in the network with missing values for the node attribute ManagementSalary and predict whether or not these individuals are receiving a management position salary.

To accomplish this, we create a matrix of node features using networkx, train a sklearn classifier on nodes that have ManagementSalary data, and predict a probability of the node receiving a management salary for nodes where ManagementSalary is missing.

The predictions will be given as the probability that the corresponding employee is receiving a management position salary. The evaluation metric is the Area Under the ROC Curve (AUC).
