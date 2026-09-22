import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK data is downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except Exception:
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
        
    import os
    if os.environ.get('VERCEL'):
        nltk_dir = '/tmp/nltk_data'
        os.makedirs(nltk_dir, exist_ok=True)
        nltk.data.path.append(nltk_dir)
    else:
        nltk_dir = None
        
    nltk.download('punkt', download_dir=nltk_dir, quiet=True)
    nltk.download('stopwords', download_dir=nltk_dir, quiet=True)
    nltk.download('wordnet', download_dir=nltk_dir, quiet=True)
    
# For newer NLTK versions, punkt_tab might be needed
try:
    nltk.data.find('tokenizers/punkt_tab')
except Exception:
    import os
    nltk_dir = '/tmp/nltk_data' if os.environ.get('VERCEL') else None
    nltk.download('punkt_tab', download_dir=nltk_dir, quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """
    Cleans and preprocesses natural language text.
    - Lowercases
    - Removes punctuation
    - Tokenizes
    - Removes stopwords
    - Lemmatizes
    """
    if not isinstance(text, str):
        return ""
        
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # 3. Tokenization
    tokens = word_tokenize(text)
    
    # 4. Remove stopwords and 5. Lemmatization
    cleaned_tokens = [
        lemmatizer.lemmatize(word) 
        for word in tokens 
        if word not in stop_words
    ]
    
    # Rejoin tokens into a single string
    return " ".join(cleaned_tokens)

def explain_nlp_pipeline(text):
    """
    Returns a dictionary breaking down the NLP preprocessing steps 
    so they can be displayed in the UI for educational demonstration.
    """
    if not isinstance(text, str):
        return {}
        
    original = text
    lowercased = text.lower()
    no_punct = re.sub(r'[^\w\s]', '', lowercased)
    tokens = word_tokenize(no_punct)
    
    no_stopwords = [word for word in tokens if word not in stop_words]
    lemmatized = [lemmatizer.lemmatize(word) for word in no_stopwords]
    
    return {
        "original": original,
        "lowercased": lowercased,
        "no_punctuation": no_punct,
        "tokens": tokens,
        "no_stopwords": no_stopwords,
        "lemmatized": lemmatized,
        "final_text": " ".join(lemmatized)
    }
