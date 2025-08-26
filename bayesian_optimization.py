import pandas as pd
import numpy as np
from skopt import Optimizer
from skopt.space import Real

df = pd.read_csv("./data/table.csv")
target_col = "yield"

X = df.drop(["yield"], axis=1)
Y_score = df["yield"].values

Y = -Y_score  

space = [
    Real(df["current"].min(),       df["current"].max(),       name="current"),
    Real(df["Init_molarity"].min(),df["Init_molarity"].max(), name="Init_molarity"),
    Real(df["electrolyte"].min(),  df["electrolyte"].max(),   name="electrolyte"),
    Real(df["temp"].min(),         df["temp"].max(),          name="temp"),
    Real(df["time"].min(),         df["time"].max(),          name="time"),
]

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
