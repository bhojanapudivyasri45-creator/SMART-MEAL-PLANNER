import os
from flask import Flask, render_template, request, jsonify

from nlp.preprocessing import explain_nlp_pipeline
from nlp.classifier import MealPlanClassifier
from meal_planner.planner import get_meal_plan
from database.database import init_db, save_query, get_recent_history

app = Flask(__name__)

# Initialize database
init_db()

# Initialize Local NLP Classifier (Scikit-Learn)
classifier = MealPlanClassifier()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.get('user_input', '').strip()
    diet_pref = request.form.get('diet_pref', '').strip()
    
    try:
        days = int(request.form.get('days', 1))
    except ValueError:
        days = 1
    
    if not user_input:
        return render_template('index.html', error="Please enter your meal planning needs.")
        
    try:
        # 1. Local NLP Prediction using Scikit-Learn (INSTANT)
        prediction_result = classifier.predict(user_input)
        category = prediction_result['category']
        confidence = prediction_result['confidence']
        
        nlp_steps = prediction_result.get('nlp_steps', {})
        
        # Override with diet preference if explicitly chosen and confident in default
        if diet_pref and diet_pref != "none" and category in ["general_health", "balanced_diet"]:
            category = diet_pref
            
        # 2. Generate Multi-Day Meal Plan (API/INSTANT)
        meal_plan = get_meal_plan(category, days=days, user_input=user_input, diet_pref=diet_pref)
        
        # 3. Save to Database
        save_query(user_input, category, diet_pref)
        
        return render_template('result.html', 
                               user_input=user_input,
                               category=category,
                               confidence=confidence,
                               meal_plan=meal_plan,
                               nlp_steps=nlp_steps)
                               
    except Exception as e:
        print(f"Error: {str(e)}")
        # Fallback for errors
        fallback_plan = get_meal_plan("balanced_diet", days=days)
        return render_template('result.html', 
                               user_input=user_input,
                               category="General Balanced Diet",
                               confidence="N/A",
                               meal_plan=fallback_plan,
                               error_msg=f"Model error: {str(e)}. Showing balanced plan.",
                               nlp_steps={})

@app.route('/health')
def health_check():
    return jsonify({"status": "running"})

@app.route('/history')
def history():
    recent_queries = get_recent_history()
    return jsonify(recent_queries)

if __name__ == '__main__':
    app.run(debug=True)
