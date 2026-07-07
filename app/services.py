"""
=========================================
Services
AI Diet Recommendation System
=========================================
"""

import os
import pandas as pd

from food_mapping import find_best_food
from nutrition_engine import NutritionEngine
from recipe_engine import RecipeEngine
from recommendation_engine import RecommendationEngine


class DietService:

    def __init__(self):

        # ==========================================
        # Project Paths
        # ==========================================

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        nutrition_path = os.path.join(BASE_DIR, "datasets", "nutrition")
        recipe_path = os.path.join(BASE_DIR, "datasets", "recipes")

        # ==========================================
        # Load Nutrition Dataset
        # ==========================================

        print("Loading Nutrition Dataset...")

        self.food_df = pd.read_csv(
            os.path.join(nutrition_path, "food.csv"),
            low_memory=False
        )

        self.food_nutrient_df = pd.read_csv(
            os.path.join(nutrition_path, "food_nutrient.csv"),
            low_memory=False
        )

        print("✅ Nutrition Dataset Loaded")

        # ==========================================
        # Load Recipe Dataset
        # ==========================================

        print("Loading Recipe Dataset...")

        recipe_file = os.path.join(recipe_path, "RAW_recipes.csv")

        print("Recipe File :", recipe_file)

        self.recipe_df = pd.read_csv(
            recipe_file,
            low_memory=False
        )

        print("Recipe Shape :", self.recipe_df.shape)

        print("Recipe Columns :")

        print(self.recipe_df.columns.tolist())

        # ==========================================
        # Create Engines
        # ==========================================

        self.nutrition_engine = NutritionEngine(
            self.food_df,
            self.food_nutrient_df
        )

        self.recipe_engine = RecipeEngine(
            self.recipe_df
        )

        self.recommendation_engine = RecommendationEngine()

        print("✅ Diet Service Ready!")

    # ==========================================================
    # Complete AI Report
    # ==========================================================

    def get_complete_report(self, food_name):

        # Find Food
        best_food = find_best_food(
            food_name,
            self.food_df,
            self.food_nutrient_df
        )

        if best_food is None:
            return None

        food_id = best_food["fdc_id"]
        print("=" *50)
        print("Food Name:", food_name)
        print("Food ID:", food_id)
        print("Description:", best_food["description"])
        print("=" * 50)

        # Nutrition
        nutrition = self.nutrition_engine.get_nutrition(
            food_id
        )
        print("=" *50)
        print("Food Name:", food_name)
        print("Food ID:", food_id)
        print("Nutrition:", nutrition)
        print("=" * 50)

        # Recipes
        recipes = self.recipe_engine.search_recipes(
            food_name
        )

        # Recommendation
        recommendation = self.recommendation_engine.get_recommendation(
            food_name
        )
        print("Nutrition Dictionary")
        
        print(nutrition)
        return {

            "food": food_name,

            "nutrition": nutrition,

            "recipes": recipes,

            "recommendation": recommendation

        }