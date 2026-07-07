"""
=========================================
Recommendation Engine
AI Diet Recommendation System
=========================================
"""


class RecommendationEngine:

    def __init__(self):

        self.DIET_ADVICE = {

            "banana": {
                "best_time": "Breakfast",
                "benefit": "Rich in potassium and natural energy.",
                "water": "Drink one glass of water.",
                "pair_with": "Oats or yogurt."
            },

            "milk": {
                "best_time": "Morning",
                "benefit": "Excellent source of calcium.",
                "water": "Drink water throughout the day.",
                "pair_with": "Oats or cereal."
            },

            "eggs": {
                "best_time": "Breakfast",
                "benefit": "High-quality protein.",
                "water": "Drink one glass of water.",
                "pair_with": "Whole wheat bread."
            },

            "chicken": {
                "best_time": "Lunch",
                "benefit": "Rich in lean protein.",
                "water": "Drink two glasses of water.",
                "pair_with": "Brown rice and vegetables."
            },

            "fish": {
                "best_time": "Lunch or Dinner",
                "benefit": "Rich in Omega-3 fatty acids.",
                "water": "Stay hydrated throughout the day.",
                "pair_with": "Steamed vegetables."
            }

        }

    def get_recommendation(self, food_name):

        food_name = food_name.lower()

        if food_name in self.DIET_ADVICE:

            return self.DIET_ADVICE[food_name]

        return {

            "best_time": "Any Time",

            "benefit": "Healthy food choice.",

            "water": "Stay hydrated.",

            "pair_with": "Fresh vegetables."

        }