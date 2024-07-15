import pandas as pd
import numpy as np
from kaggle_lib.titanic.preprocessing import replace_missing_age_values


def test_titanic_preprocessing():
    test_titanic_df = pd.DataFrame([['Mr', np.nan], ['Mr', np.nan], 'Ms', 28.1],  columns=['Title', 'Age'])
    test_titanic_df = replace_missing_age_values(test_titanic_df)
    assert test_titanic_df.isna()