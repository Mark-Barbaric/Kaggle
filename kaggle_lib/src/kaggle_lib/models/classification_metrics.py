from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def get_classification_metrics(y_true, y_pred, name) -> dict:
    """_summary_

    Args:
        y_true (_type_): _description_
        y_pred (_type_): _description_
        name (_type_): _description_

    Returns:
        dict: _description_
    """
    return {
        'name': name,
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred),
        'recall': recall_score(y_true, y_pred),
        'f1_score': f1_score(y_true, y_pred)
    }