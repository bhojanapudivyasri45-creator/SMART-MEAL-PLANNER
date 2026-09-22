import pandas as pd
import random
import os

def generate_dataset():
    data = []
    
    # Categories to predict
    categories = [
        "diabetes", "hypertension", "weight_management", 
        "general_health", "vegetarian", "vegan", 
        "high_protein", "low_sodium", "heart_healthy", "balanced_diet",
        "jaundice", "typhoid"
    ]
    
    # Base templates for generating sentences
    templates = {
        "diabetes": [
            "I have diabetes and need a {meal} plan",
            "What should I eat if I have diabetes?",
            "Healthy food for diabetic patients",
            "I am diabetic and want to plan my diet",
            "Looking for sugar-free {meal} options for diabetes",
            "I need a low glycemic index diet",
            "Diabetic friendly meal suggestions please",
            "Can you suggest a healthy meal plan for someone with diabetes?"
        ],
        "hypertension": [
            "I have high blood pressure and want a {meal} plan",
            "Diet plan for hypertension",
            "What to eat to lower blood pressure?",
            "I suffer from high BP and need healthy food",
            "Meals for hypertension control",
            "Low sodium food for high blood pressure",
            "I want a diet plan for my hypertension",
            "Blood pressure friendly {meal} ideas"
        ],
        "weight_management": [
            "I want to lose weight, give me a {meal} plan",
            "Diet plan for weight loss",
            "I am trying to manage my weight with healthy food",
            "Low calorie {meal} options",
            "Meals for weight management and fat loss",
            "I need a calorie deficit diet plan",
            "Healthy diet for maintaining my weight",
            "Weight reduction friendly {meal} suggestions"
        ],
        "general_health": [
            "I just want a healthy {meal} plan",
            "Healthy diet for maintaining my current lifestyle",
            "General wellness meal suggestions",
            "I need a nutritious daily diet",
            "Simple and healthy food plan",
            "Give me a general healthy diet",
            "I want to eat clean and stay fit",
            "Basic health focused {meal} ideas"
        ],
        "vegetarian": [
            "I am a vegetarian and want a {meal} plan",
            "Vegetarian diet plan for the week",
            "Healthy veg food only",
            "Plant based but not vegan meals",
            "I don't eat meat, need a pure vegetarian diet",
            "Vegetarian options for a healthy lifestyle",
            "I need a vegetarian {meal} plan without eggs",
            "Veg food recommendations please"
        ],
        "vegan": [
            "I am vegan and need a plant-based {meal} plan",
            "Vegan diet plan for the whole week",
            "No animal products, healthy vegan food",
            "Strictly vegan meal suggestions",
            "I need a dairy-free and meat-free vegan diet",
            "Plant based vegan meals only",
            "Vegan {meal} options for healthy living",
            "Pure vegan diet plan"
        ],
        "high_protein": [
            "I want a high protein {meal} plan for muscle gain",
            "High protein diet plan",
            "Protein rich foods for my workout",
            "I need more protein in my diet",
            "Meals with lots of protein",
            "Suggest a high protein {meal} option",
            "Diet for bodybuilding with high protein",
            "Protein heavy food recommendations"
        ],
        "low_sodium": [
            "I want a low sodium {meal} plan",
            "Low salt diet plan",
            "Meals with very little salt",
            "I need a sodium restricted diet",
            "Suggest low sodium {meal} options",
            "Healthy low salt food",
            "Diet with minimum sodium content",
            "Salt free or low sodium meals"
        ],
        "heart_healthy": [
            "I want a heart healthy {meal} plan",
            "Diet for good cardiovascular health",
            "Heart friendly meals",
            "I need food that is good for my heart",
            "Suggest heart healthy {meal} options",
            "Low cholesterol heart healthy diet",
            "Cardio friendly diet plan",
            "Meals for maintaining a healthy heart"
        ],
        "balanced_diet": [
            "I need a perfectly balanced {meal} plan",
            "Balanced diet with all nutrients",
            "I want a mix of carbs, proteins, and fats",
            "Healthy and balanced daily meals",
            "Well rounded balanced diet",
            "Suggest a balanced {meal} option",
            "Complete balanced nutrition plan",
            "A balanced diet for everyday living"
        ],
        "jaundice": [
            "I have jaundice and need a diet plan",
            "What should I eat during jaundice recovery?",
            "Jaundice friendly {meal} suggestions",
            "I am suffering from jaundice, give me healthy food options",
            "Diet for liver recovery from jaundice",
            "Foods to eat when you have jaundice",
            "I need a {meal} plan for jaundice patient",
            "Best diet to cure jaundice quickly"
        ],
        "typhoid": [
            "I have typhoid fever and need a {meal} plan",
            "Diet plan for typhoid patient",
            "What to eat during typhoid?",
            "I am recovering from typhoid fever",
            "Soft foods for typhoid recovery",
            "Best {meal} options when suffering from typhoid",
            "Typhoid friendly diet recommendations",
            "I need a highly nutritious diet for typhoid"
        ]
    }
    
    meals = ["breakfast", "lunch", "dinner", "snack", "daily", "weekly"]
    
    # Generate varied data (aiming for ~600 rows)
    for category in categories:
        for _ in range(60): # 60 per category = 600 total
            template = random.choice(templates[category])
            meal = random.choice(meals)
            text = template.format(meal=meal)
            
            # Add some random noise/variation
            if random.random() > 0.7:
                text = "Hi, " + text
            if random.random() > 0.7:
                text = text + " Please help."
            if random.random() > 0.8:
                text = text.lower()
                
            data.append({
                "text": text,
                "category": category
            })
            
    df = pd.DataFrame(data)
    
    # Shuffle the dataset
    df = df.sample(frac=1).reset_index(drop=True)
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    df.to_csv('data/meal_dataset.csv', index=False)
    print(f"Dataset generated successfully with {len(df)} rows at 'data/meal_dataset.csv'")

if __name__ == "__main__":
    generate_dataset()
