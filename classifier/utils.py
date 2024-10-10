
import pickle
import logging

# Setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('webfala.log')
formatter = logging.Formatter('%(name)s %(levelname)s %(asctime)-15s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.propagate = False

from sklearn.feature_extraction.text import TfidfVectorizer

# Function to clean the URL (removes common prefixes)
def clean_url(url):
    prefixes = ['http://www.', 'https://www.', 'www.']
    for prefix in prefixes:
        if url.startswith(prefix):
            url = url.replace(prefix, '')
            break
    return url

# Function to tokenize the URL into different components
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
    return total_Tokens  # Return tokens for further processing

# Function to load the pre-trained model and vectorizer
def load_model_and_vectorizer():
    try:
        with open('classifier/logit_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        with open('classifier/vectorizer.pkl', 'rb') as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)
        logger.info('Model and vectorizer successfully loaded.')
        return model, vectorizer
    except Exception as e:
        logger.error(f"Error loading model or vectorizer: {e}")
        raise e

# Function to predict if the URL is malicious or safe
def predict_url_category(url, model, vectorizer):
    try:
        # Transform the cleaned URL using the vectorizer
        transformed_url = vectorizer.transform([url])
        
        # Predict the category and get the confidence probability
        prediction = model.predict(transformed_url)[0]
        proba = model.predict_proba(transformed_url).max().round(2) * 100
        
        logger.debug(f"Prediction: {prediction} | URL: {url} | Confidence: {proba}%")
        
        if prediction == 'good':
            logger.debug('The URL is safe.')
            return f'The URL is safe with {proba}% confidence', True
        else:
            logger.debug('The URL appears to be malicious.')
            return f'The URL appears to be malicious with {proba}% confidence', False
    except Exception as e:
        logger.error(f"Error predicting URL category: {e}")
        raise e
