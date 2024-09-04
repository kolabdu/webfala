import pickle
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('webfala.log')
formatter = logging.Formatter('%(name)s %(levelname)s %(asctime)-15s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.propagate = False

from sklearn.feature_extraction.text import TfidfVectorizer
#from . import vectorizer_rename as vector

def clean_url(url):
    prefixes = ['http://www.', 'https://www.', 'www.']
    for prefix in prefixes:
        if url.startswith(prefix):
            url = url.replace(prefix, '')
            break
    return url


# Define the makeTokens function
def tokenize(url):
    tkns_BySlash = url.split('/')
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
    return url




def load_model_and_vectorizer():
    with open('classifier/logit_model.pkl', 'rb') as file:
        model = pickle.load(file)

    with open('classifier/vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
        
    return model, vectorizer

def predict_url_category(url, model,vectorizer):
       
    prediction = model.predict(vectorizer.transform(url))
    proba = model.predict_proba(vectorizer.transform(url))
    logger.debug(f'{prediction} url:{url}')
    if prediction == 'good':
        return f'The URL is safe with {proba.max().round(2)*100} % confidence'
        logger.debug('the url is safe')
    else:
        return f"URL APPEARS TO BE MALICIOUS with {proba.max().round(2)*100} % confidence"
        logger.debug('the url is malicious')
