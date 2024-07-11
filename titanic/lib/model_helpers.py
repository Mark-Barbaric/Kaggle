import pickle
from sklearn.linear_model import LogisticRegressionCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV


def grid_search_and_best_params(X_train, y_train, model, param_grid):
    fit_params = {
        'early_stopping_rounds': 0
    }
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        n_jobs=-1,
        scoring='f1',
        cv=5
    )
    grid_search.fit(X_train, y_train)
    return grid_search.best_params_, grid_search.best_estimator_


def grid_search_xgb(X_train, y_train, random_state):
    param_grid = {
        'n_estimators': range(8, 22, 2),
        'learning_rate': [0.5, 0.1, 0.05],
        'max_depth': range(2, 6, 2),
        'subsample': [0.25, 0.5, 0.75]
    }
    model = XGBClassifier(
        random_state=random_state,
        n_jobs=-1
    )
    return grid_search_and_best_params(X_train, y_train, model, param_grid)


def grid_search_bc(X_train, y_train, random_state):
    param_grid = {
        'n_estimators': [10, 12, 14, 16],
        'oob_score': [True, False]
    }
    model = BaggingClassifier(
        random_state=random_state,
        n_jobs=-1
    )
    return grid_search_and_best_params(X_train, y_train, model, param_grid)


def grid_search_rf(X_train, y_train, random_state):
    param_grid = {
        'n_estimators': [100, 125, 150, 200],
        'max_depth': [50, 75, 100],
        'min_samples_split': [2, 4, 6, 8],
        'max_features': ['sqrt', 'log2'],
        'oob_score': [True, False]
    }
    model = RandomForestClassifier(
        random_state=random_state,
        oob_score=True,
        n_jobs=-1
    )
    return grid_search_and_best_params(X_train, y_train, model, param_grid)


def grid_search_dt(X_train, y_train, random_state):
    param_grid = {
        'criterion': ['gini', 'entropy', 'log_loss'],
        'max_depth': [25, 50, 75, 100],
        'min_samples_split': [2, 4, 6, 8]
    }
    model = DecisionTreeClassifier(
        random_state=random_state
    )
    return grid_search_and_best_params(X_train, y_train, model, param_grid)


def grid_search_lr(X_train, y_train, random_state):
    param_grid = {
        'Cs': [6, 8, 10, 12],
        'penalty': ['l1', 'l2'],
        'cv': [4, 6, 8]
    }
    model = LogisticRegressionCV(
        random_state=random_state,
        solver='liblinear',
        n_jobs=-1
        
    )
    return grid_search_and_best_params(X_train, y_train, model, param_grid)


def save_model(model, model_name: str):
    
    with open(model_name, 'wb') as f:
        pickle.dump(model, f)


def open_model(model_name: str):
    
    with open(model_name, 'rb') as f:
        model = pickle.load(f)
    
    return model