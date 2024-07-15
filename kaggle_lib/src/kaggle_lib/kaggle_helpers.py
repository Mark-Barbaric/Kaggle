import pickle


def pickle_to_dict(pickle_dir: str) -> dict:
    """Helper function used to load dict from .pickle file

    Args:
        pickle_dir (str): _description_

    Returns:
        dict: _description_
    """
    with open(pickle_dir, 'rb') as handle:
        dict = pickle.load(handle)
    
    return dict