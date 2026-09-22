import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Import preprocessing
from nlp.preprocessing import preprocess_text

def train_and_save_model():
    dataset_path = 'data/meal_dataset.csv'
    
    print("Loading dataset...")
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}. Please run 'python scripts/generate_data.py' first.")
        return
        
    df = pd.read_csv(dataset_path)
    
    if 'text' not in df.columns or 'category' not in df.columns:
        print("Error: Dataset must contain 'text' and 'category' columns.")
        return
        
    print("Preprocessing text data...")
    # Apply preprocessing
    df['processed_text'] = df['text'].apply(preprocess_text)
    
    # Remove rows that became empty after preprocessing
    df = df[df['processed_text'].str.strip() != '']
    
    X = df['processed_text']
    y = df['category']
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Vectorizing text using TF-IDF...")
    vectorizer = TfidfVectorizer(max_features=1000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    print("Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_tfidf, y_train)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    
    print("\n" + "="*50)
    print(f"MODEL TRAINING COMPLETED")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("="*50)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    print("\nSaving model and vectorizer...")
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/meal_classifier.pkl')
    joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
    
    print("Success! Model and vectorizer saved to 'models/' directory.")

if __name__ == "__main__":
    train_and_save_model()
