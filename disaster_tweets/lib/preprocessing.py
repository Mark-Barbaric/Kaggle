import re

def preprocess_text(x : str)->str:
    x = x.lower()
    x = re.sub(r'http\S+', '', x)
    x = re.sub(r'@\S+', '', x)
    x = x.strip(' ')
    x = re.sub(r'[^a-zA-Z0-9 ]+', '', x)
    return x


def is_valid_token(x : str)->bool:

    return x

def sentences_to_strings(sentences:list[str])->list[list[int,str]]:
    ...
