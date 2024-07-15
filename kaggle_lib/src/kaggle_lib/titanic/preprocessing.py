from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import pickle


def pickle_to_dict(pickle_dir: str) -> dict:
    with open(pickle_dir, 'rb') as handle:
        dict = pickle.load(handle)
    
    return dict


def replace_missing_age_values(df):
    mean_age_by_titles = pickle_to_dict('mean_age_by_titles.pickle')
    missing_age_mask = (df['Age'].isna())
    df.loc[missing_age_mask, 'Age'] = df[missing_age_mask].apply(lambda x : mean_age_by_titles[x['Title']], axis=1).values


def replace_missing_fare_values(df):
    mean_fare = df['Fare'].mean()
    df['Fare'] = df['Fare'].fillna(mean_fare)


def create_titles_column(df):
    passenger_names = df['Name'].str.split(',')
    df['Title'] = [passenger_name[1].lstrip().split(' ')[0][:-1] for passenger_name in passenger_names]
    df.drop('Name', inplace=True, axis=1)


def create_group_size(df):
    df['GroupSize'] = df.groupby('Ticket')['Ticket'].transform('count')


def create_family_size_column(df):
    df['FamilySize'] = df['SibSp'] + df['Parch']
    df.drop(['SibSp', 'Parch'], inplace=True, axis=1)

 
def normalize_columns(df):
    #TODO: move to ColumnTransformer class
    min_max_scaler = MinMaxScaler()
    NUMERICAL_COLUMNS = ['Age', 'Fare']
    df[NUMERICAL_COLUMNS] = min_max_scaler.fit_transform(df[NUMERICAL_COLUMNS])


def label_columns(df, titles):
    #TODO: move to ColumnTransformer class
    label_encoder = LabelEncoder()
    df['Sex'] = label_encoder.fit_transform(df['Sex'])
    df['Embarked'] = label_encoder.fit_transform(df['Embarked'])
    label_encoder.fit(titles)
    df['Title'] = label_encoder.transform(df['Title'])


def drop_unnecessary_columns(df):
    COLUMNS_TO_DROP = ['PassengerId', 'Ticket', 'Cabin']
    df.drop(COLUMNS_TO_DROP, inplace=True, axis=1)


def preprocess_titanic_dataset(df, titles):
    """Class used to preprocess Titanic DataFrame in place.

    Args:
        df (_type_): _description_
    """
    create_titles_column(df)
    create_family_size_column(df)
    create_group_size(df)
    replace_missing_age_values(df)
    replace_missing_fare_values(df)
    label_columns(df, titles)
    normalize_columns(df)
    drop_unnecessary_columns(df)