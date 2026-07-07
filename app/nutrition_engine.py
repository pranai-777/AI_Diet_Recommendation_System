"""
=========================================
Nutrition Engine
AI Diet Recommendation System
=========================================
"""

import pandas as pd


class NutritionEngine:

    def __init__(self, food_df, food_nutrient_df):

        self.food_df = food_df

        self.food_nutrient_df = food_nutrient_df

        self.IMPORTANT_NUTRIENTS = {

            1008: "Calories",
            1003: "Protein",
            1004: "Fat",
            1005: "Carbohydrates"

        }

    def get_nutrition(self, food_id):

        nutrients = self.food_nutrient_df[

            self.food_nutrient_df["fdc_id"] == food_id

        ]
        print("Rows Found:", len(nutrients))
        print(nutrients.head())

        nutrients = nutrients[

            nutrients["nutrient_id"].isin(

                self.IMPORTANT_NUTRIENTS.keys()

            )

        ].copy()

        nutrients["Nutrient"] = nutrients["nutrient_id"].map(

            self.IMPORTANT_NUTRIENTS

        )

        nutrition = {}

        for _, row in nutrients.iterrows():

            nutrition[row["Nutrient"]] = row["amount"]

        return nutrition