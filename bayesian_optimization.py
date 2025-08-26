import pandas as pd
import numpy as np
from skopt import Optimizer
from skopt.space import Real
import glob

file_name = glob.glob("./data/*result.csv")[0]

df = pd.read_csv(file_name)
target_col = "yield"

X = df.drop(["yield"], axis=1)
Y_score = df["yield"].values

Y = -Y_score  

space = []


opt = Optimizer(
    dimensions=space,
    base_estimator="GP",
    acq_func="EI",
    random_state=0
)

opt.tell(X.values.tolist(), Y.tolist())

next_x = opt.ask()
print("次に試すパラメータ:", next_x)

suggestion = {name: val for name, val in zip(["current","Init_molarity","electrolyte","temp","time"], next_x)}
print(suggestion)
