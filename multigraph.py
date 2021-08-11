import pandas as pd
G_df = (pd.read_csv('email_network.txt', header = None)
                .rename(columns = {0:'data'}))
G_df = (G_df['data'].str.split("\t", n = 2, expand = True)
            .rename(columns={0:'Sender',1:'Recipient', 2:'time'}))
G_df = G_df.loc[1:][['Sender','Recipient']]
records = list(G_df.to_records(index=False))
B = nx.MultiDiGraph()
B.add_edges_from(records)
