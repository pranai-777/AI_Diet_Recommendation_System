"""
==========================================================
AI Diet Recommendation System
Professional Streamlit Dashboard
==========================================================
"""

import os
import sys
import tempfile

import streamlit as st
from pdf_generator import create_pdf
# ==========================================================
# Project Paths
# ==========================================================

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

APP_PATH = os.path.join(
    PROJECT_PATH,
    "app"
)

sys.path.append(APP_PATH)

# ==========================================================
# Import Project Modules
# ==========================================================

from image_predictor import ImagePredictor
from services import DietService

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(

    page_title="AI Diet Recommendation System",

    page_icon="🥗",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# Professional CSS
# ==========================================================

st.markdown("""

<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{

background:#eef3f8;

}

.block-container{

padding-top:1rem;
padding-left:2rem;
padding-right:2rem;
padding-bottom:2rem;
max-width:1450px;

}

/* Header */

.hero{

background:linear-gradient(90deg,#2563eb,#1d4ed8);

padding:35px;

border-radius:20px;

text-align:center;

color:white;

box-shadow:0 8px 25px rgba(0,0,0,.18);

margin-bottom:30px;

}

/* Cards */

div[data-testid="metric-container"]{

background:white;

border-radius:18px;

padding:20px;

box-shadow:0 5px 18px rgba(0,0,0,.08);

transition:0.3s;

}

div[data-testid="metric-container"]:hover{

transform:translateY(-6px);

}

/* Expander */

.streamlit-expanderHeader{

font-size:18px;

font-weight:bold;

}

/* Upload */

section[data-testid="stFileUploader"]{

background:white;

padding:20px;

border-radius:18px;

box-shadow:0 5px 15px rgba(0,0,0,.08);

}

</style>

""", unsafe_allow_html=True)

# ==========================================================
# Hero Banner
# ==========================================================

st.markdown("""

<div class="hero">

<h1>🥗 AI Diet Recommendation System</h1>

<h4>Deep Learning Powered Food Recognition & Nutrition Analysis</h4>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("🥗 AI Diet")

st.sidebar.success("✔ Food Detection")

st.sidebar.success("✔ Nutrition Analysis")

st.sidebar.success("✔ Healthy Recipes")

st.sidebar.success("✔ Diet Recommendation")

st.sidebar.markdown("---")

st.sidebar.info(

"""
Upload a food image and the AI will:

• Detect the food

• Show nutrition facts

• Recommend healthy recipes

• Provide diet advice

"""
)

# ==========================================================
# Model
# ==========================================================

MODEL_PATH = os.path.join(

PROJECT_PATH,

"models",

"food_classifier.keras"

)

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
# Load Model Only Once
# ==========================================================

@st.cache_resource

def load_system():

    predictor = ImagePredictor(

        MODEL_PATH,

        CLASS_NAMES

    )

    service = DietService()

    return predictor, service


predictor, service = load_system()

# ==========================================================
# Upload Image
# ==========================================================

uploaded_file = st.file_uploader(

"📷 Upload Food Image",

type=["jpg","jpeg","png"]

)
# ==========================================================
# AI Prediction Dashboard
# ==========================================================

if uploaded_file is not None:

    # Save uploaded image temporarily
    file_bytes = uploaded_file.getvalue()

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    temp_file.write(file_bytes)
    temp_file.close()

    # AI Prediction
    prediction = predictor.predict(temp_file.name)

    # Get Nutrition, Recipes and Recommendation
    report = service.get_complete_report(
        prediction["food"]
    )

    # ======================================================
    # Dashboard Layout
    # ======================================================

    left, right = st.columns([1, 1])

    # ======================================================
    # Uploaded Image
    # ======================================================

    with left:

        st.subheader("📷 Uploaded Food")

        st.image(
            file_bytes,
            use_container_width=True
        )

    # ======================================================
    # Prediction Result
    # ======================================================

    with right:

        st.subheader("🤖 AI Prediction")

        confidence = prediction["confidence"] * 100

        st.metric(
            "Detected Food",
            prediction["food"].title()
        )

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        # Circular Gauge using HTML
        gauge_color = "#10B981"

        if confidence < 80:
            gauge_color = "#F59E0B"

        if confidence < 60:
            gauge_color = "#EF4444"

        st.markdown(
            f"""
            <div style="
                width:180px;
                height:180px;
                border-radius:50%;
                border:14px solid {gauge_color};
                display:flex;
                justify-content:center;
                align-items:center;
                margin:auto;
                font-size:32px;
                font-weight:bold;
                color:{gauge_color};
                box-shadow:0 6px 20px rgba(0,0,0,.15);
            ">
            {confidence:.0f}%
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(
            prediction["confidence"]
        )

        st.write("")

        if confidence >= 90:

            st.success("🟢 Excellent Prediction")

        elif confidence >= 80:

            st.success("🟢 Very Good Prediction")

        elif confidence >= 70:

            st.info("🟡 Good Prediction")

        elif confidence >= 60:

            st.warning("🟠 Fair Prediction")

        else:

            st.error("🔴 Low Confidence")

    st.divider()
    # ==========================================================
    # 🥗 Nutrition Dashboard
    # ==========================================================

    st.markdown("## 🥗 Nutrition Information")

    nutrition = report["nutrition"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#F97316,#FB923C);
        padding:20px;
        border-radius:18px;
        color:white;
        text-align:center;
        box-shadow:0 5px 18px rgba(0,0,0,.18);
        ">
            <h3>🔥 Calories</h3>
            <h1>{nutrition.get("Calories","N/A")}</h1>
            <p>kcal</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#2563EB,#3B82F6);
        padding:20px;
        border-radius:18px;
        color:white;
        text-align:center;
        box-shadow:0 5px 18px rgba(0,0,0,.18);
        ">
            <h3>🥩 Protein</h3>
            <h1>{nutrition.get("Protein","N/A")}</h1>
            <p>grams</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#10B981,#34D399);
        padding:20px;
        border-radius:18px;
        color:white;
        text-align:center;
        box-shadow:0 5px 18px rgba(0,0,0,.18);
        ">
            <h3>🥑 Fat</h3>
            <h1>{nutrition.get("Fat","N/A")}</h1>
            <p>grams</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#8B5CF6,#A855F7);
        padding:20px;
        border-radius:18px;
        color:white;
        text-align:center;
        box-shadow:0 5px 18px rgba(0,0,0,.18);
        ">
            <h3>🍞 Carbohydrates</h3>
            <h1>{nutrition.get("Carbohydrates","N/A")}</h1>
            <p>grams</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ==========================================================
    # 🍽 Premium Recipe Cards
    # ==========================================================

    st.markdown("## 🍽 Healthy Recipe Suggestions")

    recipes = report["recipes"]

    if recipes.empty:

        st.warning("No healthy recipes found.")

    else:

        recipe_list = recipes.head(5)

        for i, (_, row) in enumerate(recipe_list.iterrows(), start=1):

            st.markdown(f"""
<div style="
background:white;
border-radius:20px;
padding:20px;
margin-bottom:18px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<h3>🍽 {row['name'].title()}</h3>

<p>⏱ <b>Cooking Time:</b> {row['minutes']} minutes</p>

<p>🥗 <b>Ingredients:</b> {row['n_ingredients']}</p>

</div>

<div>

<span style="
background:#10B981;
padding:8px 18px;
border-radius:30px;
color:white;
font-weight:bold;
">

Healthy

</span>

</div>

</div>

</div>
""", unsafe_allow_html=True)

    st.divider()

    # ==========================================================
    # ❤️ Premium Diet Recommendation
    # ==========================================================

    st.markdown("## ❤️ AI Diet Recommendation")

    recommendation = report["recommendation"]

    card1, card2 = st.columns(2)

    with card1:

        st.markdown(f"""
<div style="
background:linear-gradient(135deg,#2563EB,#3B82F6);
padding:25px;
border-radius:22px;
color:white;
box-shadow:0 8px 25px rgba(0,0,0,.18);
">

<h2>🕒 Best Time</h2>

<h3>{recommendation["best_time"]}</h3>

<hr>

<h2>💧 Water Intake</h2>

<h3>{recommendation["water"]}</h3>

</div>
""", unsafe_allow_html=True)

    with card2:

        st.markdown(f"""
<div style="
background:linear-gradient(135deg,#10B981,#34D399);
padding:25px;
border-radius:22px;
color:white;
box-shadow:0 8px 25px rgba(0,0,0,.18);
">

<h2>💪 Health Benefit</h2>

<h3>{recommendation["benefit"]}</h3>

<hr>

<h2>🥣 Best Combination</h2>

<h3>{recommendation["pair_with"]}</h3>

</div>
""", unsafe_allow_html=True)

    st.divider()

# ==========================================================
# Download Report
# ==========================================================

    pdf_path = create_pdf(
      report,
      prediction
     )

    with open(pdf_path, "rb") as pdf_file:

         st.download_button(

              label="📄 Download AI Diet Report",

            data=pdf_file,

            file_name="AI_Diet_Report.pdf",

            mime="application/pdf"

    )
