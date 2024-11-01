import os

def available_cpu_count():
    """ Number of *available* virtual or physical CPUs on this system """
    # Tested with Python 3.3 - 3.13 on Linux
    try:
        res = len(os.sched_getaffinity(0))
        if res > 0:
            return res
    except (KeyError, ValueError):
        pass

from sklearn.ensemble import (
    GradientBoostingRegressor,
    RandomForestRegressor,
    AdaBoostRegressor
)
import xgboost as xgb
from scipy.stats import uniform, randint


N_EDGES = 2

DATA_DIR = 'data/01_raw'
PROCESSED_DIR = 'data/02_processed'
MODEL_DIR = 'models'
RESULTS_DIR = 'results'
PLOT_DIR = 'plots'
PARAM_FILE = 'data/01_raw/clustersim_lhs_Zuordnung_Messdaten__FW.xlsx'

OUT_LABELS = ['dx', 'dy']

FONTSIZE = 8

RANDOM_SEED = 1234

TEST_SIZE = 0.2
INPUT_SIZE = 10
OUTPUT_SIZE = 2

CV_FOLDS = 5
N_ITER_SEARCH = 20

VERBOSE = False

PROBLEM_CASES = [
    16001,
    20002,
    21001,
    29001,
    30001,
    31001,
    36001,
    38001,
    40001,
    41001,
    44001,
    48001,
    49001,
    50001,
    58001,
    60002,
    61001,
    62003,
    64001
]

CLUSTER_MODELING = False
N_CLUSTER = 12
N_CLUSTER_SILH = [3, 8, 12]
CLUSTER_COLS = [4, 5]

PARAM_DICTS = [
    # {
        # 'learning_rate': uniform(0.0001, 0.1),
        # 'max_depth': randint(2, 32),
        # 'subsample': uniform(0.5, 0.5),
        # 'n_estimators': randint(100, 1000),
        # 'colsample_bytree': uniform(0.4, 0.6),
        # 'lambda': randint(1, 100),
        # 'gamma': uniform()
    # }
    # {
        # 'learning_rate': uniform(0.0001, 0.1),
        # 'n_estimators': randint(100, 1000)
    # },
    # {
        # 'learning_rate': uniform(0.0001, 0.1),
        # 'n_estimators': randint(100, 1000),
        # 'max_depth': randint(2, 32),
        # 'min_samples_split': randint(2, 11),
        # 'min_samples_leaf': randint(2, 11),
        # 'max_features': randint(1, INPUT_SIZE)
    # },
    {
        'n_estimators': randint(100, 250),
        'max_depth': randint(2, 16),
        'min_samples_split': randint(2, 11),
        'min_samples_leaf': randint(2, 11),
        'max_features': randint(1, INPUT_SIZE)
    }
]
REGRESSORS = [
    # [xgb.XGBRegressor(objective='reg:squarederror') for __ in range(OUTPUT_SIZE)]
    # [AdaBoostRegressor(random_state=RANDOM_SEED) for __ in range(OUTPUT_SIZE)],
    # [GradientBoostingRegressor(random_state=RANDOM_SEED) for __ in range(OUTPUT_SIZE)],
    [
        RandomForestRegressor(
            random_state=RANDOM_SEED,
            n_jobs=available_cpu_count()//2
        ) for __ in range(OUTPUT_SIZE)
    ]
]
