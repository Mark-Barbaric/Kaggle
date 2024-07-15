import pandas as pd
import numpy as np
from kaggle_lib.kaggle_helpers import pickle_to_dict
from kaggle_lib.titanic.preprocessing import replace_missing_age_values, label_columns, get_mean_age_pickle_dir


def test_get_mean_age_pickle_dir():
    dir = get_mean_age_pickle_dir()
    assert dir.find('titanic/mean_age_by_titles.pickle') != -1
    dict1 = pickle_to_dict(dir)
    assert dict1.get('Mrs', -1.0) != -1.0


def test_replace_missing_age_values():
    test_titanic_df = pd.DataFrame([['Mr', np.nan], ['Mr', np.nan], ['Ms', 28.1]],  columns=['Title', 'Age'])
    replace_missing_age_values(test_titanic_df)
    assert test_titanic_df.isna().values.all() == False


def test_label_columns():
    test_titanic_df = pd.DataFrame([['Male', 'S', 'Mr'], ['Female', 'C', 'Ms']], columns=['Sex', 'Embarked', 'Title'])
    label_columns(test_titanic_df)
    assert test_titanic_df['Sex'].dtype == 'int64'
    assert test_titanic_df['Embarked'].dtype == 'int64'
    assert test_titanic_df['Title'].dtype == 'int64'