from preprocessing import preprocess_text

def test_preprocesing_basic_preprocessing():
    text="Abdas"
    ans=preprocess_text(text)
    assert ans == "abdas"
    text="Aba! £as"
    ans=preprocess_text(text)
    assert ans == "aba as"
    text="https://asdadd.com This is the way to go!"
    ans=preprocess_text(text)
    assert ans == "this is the way to go"


def test_preprocesing_http_preprocessing():
    text="https://asdadd.com This is the way to go!"
    ans=preprocess_text(text)
    assert ans == "this is the way to go"
    
    text="[tag]http://asdadd.com This is the way to go!"
    ans=preprocess_text(text)
    assert ans == "tag this is the way to go"
