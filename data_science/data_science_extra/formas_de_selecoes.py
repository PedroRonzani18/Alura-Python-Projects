import pandas as pd

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())

# df[['c3','c1']]
# df[1:3]
# df[1:][['c3', 'c1']]

# df.loc['l1', 'c2']
# df.iloc[0,1]

# df.loc[['l3', 'l1'], ['c4','c1']]
# df.iloc[[2,0],[3,0]]
