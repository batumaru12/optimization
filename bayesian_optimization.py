import pandas as pd
from skopt import Optimizer
from skopt.space import Real
import glob

data_file_name = glob.glob("./data/*optimization.csv")[0]
maxmin_file_name = glob.glob("./data/*maxmin.csv")[0]

df = pd.read_csv(data_file_name)
maxmin = pd.read_csv(maxmin_file_name)
target_col = "yield"

X = df.drop(["yield"], axis=1)
Y_score = df["yield"].values

Y = -Y_score

space = []
for i in range(len(X)):
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
