import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def display_confusion_matrix(y_true, y_pred):
    """Creates and displays confusion matrix for prediction and true values.

    Args:
        y_true (_type_): _description_
        y_pred (_type_): _description_
    """
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True)
    plt.show()
    

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