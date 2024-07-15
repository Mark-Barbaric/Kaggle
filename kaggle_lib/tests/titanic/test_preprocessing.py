import pandas as pd
import numpy as np
from kaggle_lib.kaggle_helpers import pickle_to_dict
from kaggle_lib.titanic.preprocessing import replace_missing_age_values, get_mean_age_pickle_dir


def test_get_mean_age_pickle_dir():
    dir = get_mean_age_pickle_dir()
    assert dir.find('titanic/mean_age_by_titles.pickle') != -1
    dict1 = pickle_to_dict(dir)
    assert dict1.get('Mrs', -1.0) != -1.0


def test_titanic_preprocessing():
    test_titanic_df = pd.DataFrame([['Mr', np.nan], ['Mr', np.nan], ['Ms', 28.1]],  columns=['Title', 'Age'])
    test_titanic_df = replace_missing_age_values(test_titanic_df)
    #assert test_titanic_df.isna()