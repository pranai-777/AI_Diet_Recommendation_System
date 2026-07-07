"""
=========================================
Recipe Engine
AI Diet Recommendation System
=========================================
"""

import pandas as pd


class RecipeEngine:

    def __init__(self, recipe_df):

        self.recipe_df = recipe_df

        self.UNHEALTHY_WORDS = [

            "cake",
            "cookie",
            "candy",
            "pie",
            "brownie",
            "dessert",
            "ice cream",
            "chocolate",
            "cocktail"

        ]


    def search_recipes(self, food_name):

        recipes = self.recipe_df[

            self.recipe_df["name"].str.contains(
                food_name,
                case=False,
                na=False
            )

        ]

        recipes = recipes[

            (recipes["minutes"] >= 5) &
            (recipes["minutes"] <= 60)

        ]

        recipes = recipes[

            recipes["n_ingredients"] <= 10

        ]

        healthy = recipes.copy()

        for word in self.UNHEALTHY_WORDS:

            healthy = healthy[
                ~healthy["name"].str.contains(
                    word,
                    case=False,
                    na=False
                )
            ]

        healthy = healthy.sort_values(

            by=["minutes", "n_ingredients"]

        )

        return healthy.head(10)
    


# ==========================================================
# Display Recipes
# ==========================================================

def print_recipes(recipes):

    print("=" * 60)

    print("🥗 Recommended Recipes")

    print("=" * 60)

    for i, (_, row) in enumerate(recipes.iterrows(), start=1):

        print(f"\n{i}. {row['name'].title()}")

        print(f"⏱ Time : {row['minutes']} minutes")

        print(f"🥗 Ingredients : {row['n_ingredients']}")

    print("=" * 60)