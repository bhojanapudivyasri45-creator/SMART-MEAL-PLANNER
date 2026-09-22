import joblib
import os
from .preprocessing import preprocess_text, explain_nlp_pipeline

class MealPlanClassifier:
    def __init__(self, model_path='models/meal_classifier.pkl', vectorizer_path='models/tfidf_vectorizer.pkl'):
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.model = None
        self.vectorizer = None
        self._load_models()
        
    def _load_models(self):
        if os.path.exists(self.model_path) and os.path.exists(self.vectorizer_path):
            self.model = joblib.load(self.model_path)
            self.vectorizer = joblib.load(self.vectorizer_path)
        else:
            self.model = None
            self.vectorizer = None
            
    def is_ready(self):
        return self.model is not None and self.vectorizer is not None

    def predict(self, text):
        if not self.is_ready():
            raise Exception("Model or Vectorizer not found. Please run 'python train_model.py' first.")
            
        # Preprocess the input text
        processed_text = preprocess_text(text)
        
        if not processed_text.strip():
            # If text is empty after preprocessing (e.g., only stopwords)
            return {
                "category": "balanced_diet",
                "confidence": 0.0,
                "processed_text": processed_text,
                "nlp_steps": explain_nlp_pipeline(text)
            }
            
        # Vectorize
        features = self.vectorizer.transform([processed_text])
        
        # Predict
        prediction = self.model.predict(features)[0]
        
        # Get probability/confidence
        probabilities = self.model.predict_proba(features)[0]
        confidence = max(probabilities) * 100
        
        return {
            "category": prediction,
            "confidence": round(confidence, 2),
            "processed_text": processed_text,
            "nlp_steps": explain_nlp_pipeline(text)
        }
