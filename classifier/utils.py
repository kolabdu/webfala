import pickle

# def clean_url(url):
#     prefixes = ['http://www.', 'https://www.', 'http://', 'https://', 'www.']
#     for prefix in prefixes:
#         if url.startswith(prefix):
#             url = url.replace(prefix, '', 1)
#             break
#     return url

def tokenize(cleaned_url):
    tkns_BySlash = cleaned_url.split('/')
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = i.split('-')
        tkns_ByDot = []
        for token in tokens:
            temp_Tokens = token.split('.')
            tkns_ByDot.extend(temp_Tokens)
        total_Tokens.extend(tokens + tkns_ByDot)
    total_Tokens = list(set(total_Tokens))
    if 'com' in total_Tokens:
        total_Tokens.remove('com')
    return cleaned_url

def load_model_and_vectorizer():
    with open('classifier/logit_model.pkl', 'rb') as file:
        model = pickle.load(file)

    with open('classifier/vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
        
    return model, vectorizer

def predict_url_category(cleaned_url, model, vectorizer):
    X = vectorizer.transform(cleaned_url)
    prediction = model.predict(X)[0]
    return prediction
