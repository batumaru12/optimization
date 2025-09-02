import pandas as pd
import numpy as np
from skopt import Optimizer
from skopt.space import Real
import glob

data_file_name = glob.glob("./optimization/data/*optimization.csv")[0]
maxmin_file_name = glob.glob("./optimization/data/*setup.csv")[0]

df = pd.read_csv(data_file_name)
maxmin = pd.read_csv(maxmin_file_name)
target_col = "yield"

X = df.drop([target_col], axis=1)
Y_score = df[target_col].values

Y = -Y_score

space = []
for i in range(X.shape[1]):
    space.append(Real(maxmin.iloc[0, i], maxmin.iloc[1, i], name=X.columns.values[i]))

opt = Optimizer(
    dimensions=space,
    base_estimator="GP",
    acq_func="EI",
    random_state=0
)

opt.tell(X.values.tolist(), Y.tolist())

next_X = opt.ask()

suggestion = {name: round(val, 4) for name, val in zip(X.columns.values, next_X)}
print(suggestion)

append_row = {**suggestion, target_col: np.nan}
append_df = pd.DataFrame([[append_row.get(c, np.nan) for c in df.columns]], columns=df.columns)

append_df.to_csv(data_file_name, mode="a", header=False, index=False, float_format="%.4f")

print(f"最適化結果を{data_file_name}に追記しました")
