"""
=========================================
Food Mapping Module
=========================================
"""

def find_best_food(food_name, food_df, food_nutrient_df=None):

    search_word = food_name.upper()

    matches = food_df[
        food_df["description"].str.contains(
            search_word,
            case=False,
            na=False
        )
    ]

    if len(matches) == 0:
        return None

    if food_nutrient_df is None:
        return matches.iloc[0]

    REQUIRED = [1008, 1003, 1004, 1005]

    for _, row in matches.iterrows():

        food_id = row["fdc_id"]

        nutrients = food_nutrient_df[
            food_nutrient_df["fdc_id"] == food_id
        ]

        nutrient_ids = nutrients["nutrient_id"].tolist()

        if all(x in nutrient_ids for x in REQUIRED):

            print("="*60)
            print("✅ PERFECT FOOD FOUND")
            print(row["description"])
            print("="*60)

            return row

    print("⚠ No complete nutrition found.")

    return matches.iloc[0]