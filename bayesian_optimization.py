import numpy as np
from skopt import Optimizer
from skopt.space import Real

X = np.array([[ 1., 10, 0.05, 60., 180. ],
              [ 2., 20, 0.2, 25., 60. ],
              [ 3., 10, 0.1, 40., 120. ],
              [ 4., 15, 0.1, 40., 60. ],
              [ 5., 5, 0.05, 25., 120. ]], dtype=float)

Y = -np.array([46, 22, 62, 53, 14], dtype=float)

space = [ 
    Real( 1, 6, name="current"),
    Real( 5, 30, name="Init_molarity"),
    Real( 0.05, 0.25, name="electrolyte"),
    Real( 20, 80, name="temp"),
    Real( 60, 240, name="time"),
    ]

opt = Optimizer(
    dimensions=space,
    base_estimator="GP",
    acq_func="EI",
    random_state=0
)

opt.tell(X.tolist(), Y.tolist())

next_x = opt.ask()
print(next_x)
