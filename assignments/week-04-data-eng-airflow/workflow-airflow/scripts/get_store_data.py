import pandas as pd
from pathlib import Path

path = Path(__file__).parent.parent.resolve()
filename = 'dat/train_comb.csv'
data = pd.read_csv(path.joinpath(filename)) 
data_store1 = data[data.Store==1]
ofname = filename.replace('train_comb', 'train-store1')
data_store1.to_csv(path.joinpath(ofname), index=False)
