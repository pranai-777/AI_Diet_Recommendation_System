# 🥗 AI Diet Recommendation System

An AI-powered web application that detects food items from images and provides nutrition facts, healthy recipes, and personalized diet recommendations using Deep Learning and Streamlit.

---

# 📌 Overview

The AI Diet Recommendation System uses an EfficientNetB0 deep learning model to classify food images into 20 food categories. After prediction, the application retrieves nutrition information from the USDA FoodData Central dataset, recommends healthy recipes, and provides personalized diet advice through an interactive Streamlit dashboard.

---

# 🚀 Features

- 📷 Food Image Classification
- 🤖 Deep Learning using EfficientNetB0
- 🥗 Nutrition Information
- 🍽 Healthy Recipe Recommendations
- ❤️ AI Diet Recommendations
- 📄 Download Diet Report (PDF)
- 💻 Interactive Streamlit Dashboard

---

# 🧠 Model

- Architecture: EfficientNetB0
- Framework: TensorFlow / Keras
- Number of Classes: 20
- Input Size: 224 × 224

Supported Food Classes:

- Bacon
- Banana
- Bread
- Broccoli
- Butter
- Carrots
- Cheese
- Chicken
- Cucumber
- Eggs
- Fish
- Lettuce
- Milk
- Onions
- Peppers
- Potatoes
- Sausages
- Spinach
- Tomato
- Yogurt

---

# 🛠 Technologies Used

- Python
- TensorFlow
- Streamlit
- Pandas
- NumPy
- OpenCV
- Pillow
- ReportLab
- Scikit-learn

---

# 📂 Project Structure

```
AI_Diet_Recommendation_System
│
├── app/
│   ├── image_predictor.py
│   ├── services.py
│   ├── nutrition_engine.py
│   ├── recipe_engine.py
│   ├── recommendation_engine.py
│   └── food_mapping.py
│
├── datasets/
│   ├── nutrition/
│   └── recipes/
│
├── models/
│   └── food_classifier_final.keras
│
├── streamlit_app.py
├── pdf_generator.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Workflow

1. Upload a food image.
2. The EfficientNetB0 model predicts the food item.
3. Nutrition information is retrieved from the USDA FoodData Central dataset.
4. Healthy recipes are recommended.
5. Personalized diet advice is displayed.
6. Users can download the diet report as a PDF.

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Diet-Recommendation-System.git
```

Move into the project directory:

```bash
cd AI-Diet-Recommendation-System
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

# 📷 Application Screenshots

You can add screenshots here after uploading them to GitHub.

Example:

```
screenshots/home.png
screenshots/prediction.png
screenshots/nutrition.png
```

---

# 📚 Dataset

- USDA FoodData Central
- RAW Recipes Dataset

---

# 🎯 Future Enhancements

- Multi-food detection
- Meal planning
- Calorie tracking
- User authentication
- Mobile application
- Barcode scanning
- Cloud deployment

---

# 👨‍💻 Developer

**Pranai Teja Sabbe**

Master's in Data Science

University of Europe for Applied Sciences

---

# 📄 License

This project is intended for educational and research purposes only.
