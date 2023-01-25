import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)

''' preencche com 0 '''
s.fillna(0)

''' null vira o anterior '''
# print(s.fillna(method='ffill'))
print(s.fillna(method='ffill', limit=1))

''' ffil reverso '''
# print(s.fillna(method='ffill'))

print(s.fillna(s.mean()))