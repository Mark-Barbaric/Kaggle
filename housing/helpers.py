import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from constants import *


def output_preds(X_test: pd.DataFrame, preds_test: pd.DataFrame, version: str):
    output = pd.DataFrame({
        'Id': X_test.index,
        'SalePrice': preds_test
    })
    output.to_csv(f"submission_{version}.csv", index=False)


def create_categorical_cols(train: pd.DataFrame,
                            test: pd.DataFrame,
                            cols_to_ignore: list[str]) -> list[str]:
    """_summary_

    Args:
        df (pd.Dataframe): _description_
        cols_to_ignore (list[str]): _description_

    Returns:
        list[str]: _description_
    """
    return [cname for cname in train.columns
            if cname not in cols_to_ignore and
            train[cname].nunique() < MAX_CARDINALITY and
            train[cname].dtype == "object" and
            test[cname].nunique() < MAX_CARDINALITY and
            test[cname].dtype == "object"]


def create_numerical_cols(train: pd.DataFrame,
                          test: pd.DataFrame,
                          cols_to_ignore: list[str]) -> list[str]:
    """_summary_

    Args:
        train (pd.DataFrame): _description_
        test (pd.DataFrame): _description_
    
    Returns:
        list[str]: _description_
    """
    return [cname for cname in train.columns
            if cname not in cols_to_ignore and
            train[cname].dtype in ['int64', 'float64'] and
            test[cname].dtype in ['int64', 'float64']]


def y_and_train_test_split(df: pd.DataFrame, y_column: str, train_size: float):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        train_size (float): _description_
    """
    test_size = 1.0 - train_size
    X_final = df.drop(y_column, axis=1)
    y = df[y_column]
    return train_test_split(X_final, y,
                            train_size=train_size, test_size=test_size,
                            random_state=0)


def get_feature_names(pipeline: Pipeline) -> dict[str, float]:
    """_summary_

    Args:
        pipeline (Pipeline): _description_

    Returns:
        map[str, float]: _description_
    """
    column_transformer = pipeline['column_transformer']
    assert hasattr(column_transformer, 'get_feature_names_out')
    feature_names = column_transformer.get_feature_names_out()
    feature_selection = pipeline['feature_selection']
    output = {}
    
    for step in feature_selection:
        assert hasattr(step, 'get_support')
        feature_importances = step.get_support()
        feature_names = [cname for i, cname in enumerate(feature_names) if feature_importances[i]]

    return feature_names