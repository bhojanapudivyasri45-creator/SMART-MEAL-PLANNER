import random

def get_meal_plan(category, days=1):
    """
    Returns a meal plan based on the NLP detected category.
    Generates a daily plan for the specified number of days.
    """
    
    # Store multiple options for each meal to allow generating multiple days
    data = {
        "diabetes": {
            "title": "Diabetes-Friendly Meal Pattern",
            "breakfasts": [
                "Oatmeal with berries and a sprinkle of nuts.",
                "Scrambled eggs with spinach and whole-grain toast.",
                "Greek yogurt with chia seeds and sliced almonds."
            ],
            "mid_morning_snacks": ["A small apple with almond butter.", "Handful of walnuts.", "Carrot sticks with hummus."],
            "lunches": [
                "Grilled chicken or tofu salad with mixed greens and vinaigrette.",
                "Quinoa bowl with black beans, corn, and avocado.",
                "Lentil soup with a side salad."
            ],
            "evening_snacks": ["Unsalted almonds.", "Celery with peanut butter.", "Roasted chickpeas."],
            "dinners": [
                "Baked salmon with roasted broccoli and a small portion of quinoa.",
                "Grilled turkey burger (no bun) with side salad.",
                "Tofu stir-fry with mixed non-starchy vegetables."
            ],
            "foods_to_consider": "Whole grains, leafy greens, lean proteins, beans, lentils, and healthy fats (avocados, nuts).",
            "foods_to_limit": "STRICTLY AVOID: Sugary beverages, refined carbohydrates (white bread, pasta), processed meats, and foods high in added sugars."
        },
        "hypertension": {
            "title": "Hypertension / Low-Sodium Meal Pattern",
            "breakfasts": ["Greek yogurt with sliced bananas.", "Oatmeal with fresh fruit.", "Whole wheat toast with mashed avocado."],
            "mid_morning_snacks": ["Unsalted rice cakes with hummus.", "Fresh fruit like a pear.", "Unsalted mixed nuts."],
            "lunches": [
                "Turkey wrap on whole-wheat tortilla with plenty of fresh veggies (no added salt).",
                "Large green salad with grilled chicken and lemon-olive oil dressing.",
                "Low-sodium vegetable soup with a side salad."
            ],
            "evening_snacks": ["Fresh orange.", "Apple slices.", "Carrot sticks."],
            "dinners": [
                "Grilled fish with steamed vegetables seasoned with herbs (no salt).",
                "Baked chicken breast with brown rice and asparagus.",
                "Lentil and vegetable stew."
            ],
            "foods_to_consider": "Fruits, vegetables, whole grains, low-fat dairy, and lean proteins (DASH diet principles).",
            "foods_to_limit": "STRICTLY AVOID: High-sodium processed foods, canned soups, salty snacks, pickles, and processed meats."
        },
        "weight_management": {
            "title": "Weight Management / Calorie-Conscious Plan",
            "breakfasts": ["Protein smoothie with spinach.", "Egg white omelet with vegetables.", "Greek yogurt with berries."],
            "mid_morning_snacks": ["Carrot and celery sticks with hummus.", "Small apple.", "Handful of almonds."],
            "lunches": [
                "Large mixed salad with lean protein.",
                "Zucchini noodles with turkey meatballs.",
                "Quinoa salad with mixed veggies."
            ],
            "evening_snacks": ["Air-popped popcorn.", "Cucumber slices.", "Edamame."],
            "dinners": [
                "Grilled chicken with roasted Brussels sprouts.",
                "Baked cod with a side salad.",
                "Tofu and broccoli stir-fry."
            ],
            "foods_to_consider": "High-volume, low-calorie foods like leafy greens, lean proteins, and fiber-rich vegetables.",
            "foods_to_limit": "STRICTLY AVOID: High-calorie sugary drinks, deep-fried foods, heavy sauces, and excessive portions of calorie-dense snacks."
        },
        "vegetarian": {
            "title": "Vegetarian Meal Plan",
            "breakfasts": ["Avocado toast with hemp seeds.", "Oatmeal with nuts and fruits.", "Smoothie bowl."],
            "mid_morning_snacks": ["Greek yogurt with mixed berries.", "Apple with peanut butter.", "Handful of walnuts."],
            "lunches": ["Lentil soup with side salad.", "Chickpea salad sandwich.", "Quinoa and black bean bowl."],
            "evening_snacks": ["Roasted chickpeas.", "Carrot sticks with hummus.", "Fruit salad."],
            "dinners": ["Vegetable and tofu stir-fry with brown rice.", "Eggplant parmesan with side salad.", "Stuffed bell peppers with quinoa and beans."],
            "foods_to_consider": "Lentils, beans, tofu, tempeh, eggs, dairy, nuts, seeds, and plenty of vegetables.",
            "foods_to_limit": "Meat, poultry, and fish."
        },
        "vegan": {
            "title": "Vegan Plant-Based Meal Plan",
            "breakfasts": ["Chia seed pudding with almond milk.", "Vegan protein smoothie.", "Oatmeal with berries."],
            "mid_morning_snacks": ["Edamame.", "Apple with almond butter.", "Mixed nuts."],
            "lunches": ["Quinoa bowl with black beans and avocado.", "Lentil soup.", "Vegan wrap with hummus and veggies."],
            "evening_snacks": ["Mixed nuts and seeds.", "Roasted chickpeas.", "Fruit."],
            "dinners": ["Lentil Shepherd's Pie.", "Hearty chickpea curry with brown rice.", "Tofu stir-fry."],
            "foods_to_consider": "Legumes, tofu, tempeh, seitan, nuts, seeds, fruits, vegetables, and whole grains.",
            "foods_to_limit": "STRICTLY AVOID: All animal products including meat, dairy, eggs, and honey."
        },
        "high_protein": {
            "title": "High-Protein Meal Plan",
            "breakfasts": ["Three-egg omelet with spinach and cheese.", "Protein shake.", "Cottage cheese with fruit."],
            "mid_morning_snacks": ["Cottage cheese with pineapple.", "Handful of almonds.", "Hard-boiled eggs."],
            "lunches": ["Grilled chicken breast with quinoa.", "Tofu salad.", "Tuna salad on whole wheat."],
            "evening_snacks": ["Greek yogurt.", "Protein bar.", "Edamame."],
            "dinners": ["Lean steak or salmon with roasted sweet potatoes.", "Chicken breast with asparagus.", "Lentil stew."],
            "foods_to_consider": "Lean meats, poultry, fish, eggs, dairy, legumes, and soy products.",
            "foods_to_limit": "Empty calories from sugary snacks and heavily processed foods."
        },
        "low_sodium": {
            "title": "Low-Sodium Meal Plan",
            "breakfasts": ["Oatmeal with berries (no added salt).", "Fresh fruit smoothie.", "Unsalted scrambled eggs."],
            "mid_morning_snacks": ["Fresh fruit salad.", "Unsalted nuts.", "Carrot sticks."],
            "lunches": ["Unsalted vegetable soup.", "Low-sodium turkey sandwich.", "Large green salad."],
            "evening_snacks": ["Unsalted mixed nuts.", "Apple slices.", "Cucumber sticks."],
            "dinners": ["Baked chicken with fresh herbs.", "Grilled fish with lemon.", "Vegetable stir-fry (no soy sauce)."],
            "foods_to_consider": "Fresh fruits and vegetables, fresh meats, whole grains, and salt-free seasoning blends.",
            "foods_to_limit": "STRICTLY AVOID: Canned foods, processed meats, soy sauce, and salty snack foods."
        },
        "heart_healthy": {
            "title": "Heart-Healthy Meal Plan",
            "breakfasts": ["Whole-grain cereal with low-fat milk.", "Oatmeal with walnuts.", "Avocado toast."],
            "mid_morning_snacks": ["Small handful of walnuts.", "Fresh fruit.", "Celery with almond butter."],
            "lunches": ["Spinach salad with grilled salmon.", "Turkey and avocado wrap.", "Lentil soup."],
            "evening_snacks": ["Celery sticks with almond butter.", "Apple slices.", "Handful of almonds."],
            "dinners": ["Baked cod or grilled chicken with roasted Brussels sprouts.", "Salmon with quinoa.", "Vegetable stew."],
            "foods_to_consider": "Fatty fish (rich in Omega-3s), nuts, olive oil, oats, and lots of vegetables.",
            "foods_to_limit": "STRICTLY AVOID: Saturated fats, trans fats, high-sodium foods, and red meat."
        },
        "jaundice": {
            "title": "Jaundice Recovery Diet",
            "breakfasts": ["Oatmeal with honey and banana.", "Porridge made with water or skim milk.", "Poha (flattened rice) with very little oil."],
            "mid_morning_snacks": ["Fresh sugarcane juice (highly recommended).", "Papaya slices.", "Coconut water."],
            "lunches": [
                "Soft boiled rice with boiled dal (lentils) and spinach.",
                "Khichdi (rice and lentil porridge) with mild spices.",
                "Vegetable clear soup with soft boiled rice."
            ],
            "evening_snacks": ["Sweet lime (mosambi) juice.", "Boiled potato chaat (no spices).", "A small bowl of curd/yogurt."],
            "dinners": [
                "Light vegetable soup and a small portion of soft rice.",
                "Mashed boiled vegetables (carrots, beans) with soft chapatis.",
                "Dal water (lentil broth) with plain rice."
            ],
            "foods_to_consider": "Carbohydrate-rich foods, sugarcane juice, coconut water, papaya, clear soups, boiled vegetables, and plenty of fluids.",
            "foods_to_limit": "STRICTLY AVOID: Non-vegetarian food (meat, fish, poultry), eggs, spicy foods, oily/fried foods, butter, ghee, heavy dairy, alcohol, and caffeine. The liver needs to rest and process very light food."
        },
        "typhoid": {
            "title": "Typhoid Fever Recovery Diet",
            "breakfasts": ["Soft boiled eggs (if tolerated) or mashed banana with milk.", "Thin porridge or gruel.", "White bread toast with a little jam."],
            "mid_morning_snacks": ["Strained fruit juice (apple or grape).", "Coconut water.", "Fruit custard."],
            "lunches": [
                "Overcooked soft rice with well-mashed dal.",
                "Vegetable soup with thoroughly boiled vegetables.",
                "Sago (sabudana) khichdi or plain curd rice."
            ],
            "evening_snacks": ["Baked apple or applesauce.", "Clear vegetable broth.", "Boiled potato."],
            "dinners": [
                "Light soup with soft bread.",
                "Moong dal khichdi (very soft).",
                "Mashed pumpkin or bottle gourd with soft rice."
            ],
            "foods_to_consider": "High-calorie, high-carbohydrate, low-fiber, and soft foods. Drink boiled/purified water, clear soups, fruit juices, and coconut water.",
            "foods_to_limit": "STRICTLY AVOID: Non-vegetarian food (meat, heavy fish, chicken), raw vegetables, high-fiber foods (like whole grains, raw fruits with skin), spicy foods, and heavily fried foods. The digestive system is very weak during typhoid."
        },
        "balanced_diet": {
            "title": "General Balanced Meal Plan",
            "breakfasts": ["Whole-wheat toast with mashed avocado and a boiled egg.", "Oatmeal with fruit.", "Greek yogurt."],
            "mid_morning_snacks": ["Piece of seasonal fruit.", "Handful of nuts.", "Carrot sticks."],
            "lunches": ["Whole grain wrap with lean turkey and hummus.", "Mixed salad with chicken.", "Quinoa bowl."],
            "evening_snacks": ["Small handful of trail mix.", "Apple slices.", "Yogurt."],
            "dinners": ["Grilled chicken breast with steamed green beans.", "Baked fish with sweet potato.", "Tofu stir-fry."],
            "foods_to_consider": "A colorful variety of fruits, vegetables, whole grains, and lean proteins.",
            "foods_to_limit": "Highly processed foods, excessive added sugars, and fried foods."
        },
        "general_health": {
            "title": "General Wellness Meal Plan",
            "breakfasts": ["Smoothie bowl with spinach.", "Oatmeal with berries.", "Eggs with toast."],
            "mid_morning_snacks": ["Sliced bell peppers with guacamole.", "Fruit.", "Nuts."],
            "lunches": ["Quinoa salad with mixed vegetables.", "Chicken salad.", "Soup and salad."],
            "evening_snacks": ["Apple slices with cinnamon.", "Yogurt.", "Popcorn."],
            "dinners": ["Baked white fish with mixed greens.", "Chicken with roasted vegetables.", "Lentil stew."],
            "foods_to_consider": "Whole, unprocessed foods.",
            "foods_to_limit": "Refined sugars and artificial additives."
        }
    }
    
    # Default to balanced diet if category not found
    category_data = data.get(category, data["balanced_diet"])
    
    # Generate daily plans
    daily_plans = []
    for day_num in range(1, days + 1):
        # Pick a random meal or rotate through options
        daily_plans.append({
            "day": day_num,
            "breakfast": random.choice(category_data["breakfasts"]),
            "mid_morning_snack": random.choice(category_data["mid_morning_snacks"]),
            "lunch": random.choice(category_data["lunches"]),
            "evening_snack": random.choice(category_data["evening_snacks"]),
            "dinner": random.choice(category_data["dinners"])
        })
    
    plan = {
        "title": category_data["title"],
        "daily_plans": daily_plans,
        "foods_to_consider": category_data["foods_to_consider"],
        "foods_to_limit": category_data["foods_to_limit"],
        "nutrition_tips": category_data.get("nutrition_tips", "Follow general healthy eating guidelines.")
    }
    
    return plan
