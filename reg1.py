import pandas as pd
import re
from datetime import datetime
import numpy as np

p = pd.DataFrame.from_csv("final.csv")

# to get train data from the DataFrame
train_data = p[np.isfinite(p['price'])]
train_data.to_csv("final_train_data.csv")

# to separate test data from the DataFrame
test_data = p[pd.isnull(p['price'])]
test_data.to_csv("final_test_data.csv")
