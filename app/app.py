"""
=========================================
AI Diet Recommendation System
Main Application
=========================================
"""

import os

from image_predictor import ImagePredictor
from services import DietService
from utils import check_file_exists, print_heading


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    PROJECT_PATH,
    "models",
    "food_classifier_final.keras"
)


# ==========================================================
# Food Classes
# ==========================================================

CLASS_NAMES = [

    "bacon",
    "banana",
    "bread",
    "broccoli",
    "butter",
    "carrots",
    "cheese",
    "chicken",
    "cucumber",
    "eggs",
    "fish",
    "lettuce",
    "milk",
    "onions",
    "peppers",
    "potatoes",
    "sausages",
    "spinach",
    "tomato",
    "yogurt"

]


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    print_heading("AI Diet Recommendation System")

    predictor = ImagePredictor(
        MODEL_PATH,
        CLASS_NAMES
    )

    service = DietService()

    image_path = input("\nEnter Image Path : ").strip().strip('"')

    check_file_exists(image_path)

    prediction = predictor.predict(image_path)

    report = service.get_complete_report(
        prediction["food"]
    )

    print("\n")
    print("=" * 60)
    print("🍽 AI DIET RECOMMENDATION REPORT")
    print("=" * 60)

    print(f"\n📷 Food : {prediction['food'].title()}")
    print(f"🎯 Confidence : {prediction['confidence']*100:.2f}%")

    print("\n🥗 Nutrition")

    for key, value in report["nutrition"].items():

        print(f"{key:15}: {value}")

    print("\n🍽 Top Recipes")

    recipes = report["recipes"]

    for i, (_, row) in enumerate(recipes.head(5).iterrows(), start=1):

        print(f"\n{i}. {row['name'].title()}")
        print(f"⏱ Time : {row['minutes']} min")
        print(f"🥗 Ingredients : {row['n_ingredients']}")

    advice = report["recommendation"]

    print("\n❤️ Recommendation")

    print(f"Best Time : {advice['best_time']}")
    print(f"Benefit   : {advice['benefit']}")
    print(f"Water     : {advice['water']}")
    print(f"Pair With : {advice['pair_with']}")

    print("\n" + "=" * 60)