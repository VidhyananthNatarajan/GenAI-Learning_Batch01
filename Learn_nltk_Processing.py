import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# input text
text ="This is an sample text for NLP DATA pre-processing and running. This is to Clean the data and Tokenize it."

# Function for Data pre-processing
def preprocess_text(text):
    text = text.lower()
 # Removal of puncutations and special chars
    text = re.sub(r'[^\w\s]','',text)
    
 # Tokenize the text
    tokens = word_tokenize(text)

 # stopwords
    stop_words = set(stopwords.words('english'))  
    tokens =[word for word in tokens if word not in stop_words]

 # Lemmization
    lemmatizer=WordNetLemmatizer()
    lem_tokens= [lemmatizer.lemmatize(word) for word in tokens]
    return text,tokens,lem_tokens
    









processed_text = preprocess_text(text)
print("Procesed text is:",processed_text)

