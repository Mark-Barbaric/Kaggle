
import preprocessor as tweet_preprocessor
import string


def preprocess_text(text, stopwords):
    """_summary_

    Args:
        df (_type_): _description_
        column_name (_type_): _description_
        stopwords (_type_): _description_
    """
    def remove_punctuations(text: str):
        for punctuation in string.punctuation:
            text = text.replace(punctuation, '')
        return text

    text = text.lower()
    text = remove_punctuations(text)
    text = text.replace('\s\s+', ' ')
    text = tweet_preprocessor.clean(text)
    text = ' '.join([w for w in text.split(' ') if w not in stopwords])
    return text