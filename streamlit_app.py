"""
==========================================================
AI Diet Recommendation System
Premium Streamlit Dashboard — Enhanced Edition
==========================================================
"""

import os
import sys
import tempfile
from datetime import datetime

import streamlit as st
from pdf_generator import create_pdf

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
APP_PATH = os.path.join(PROJECT_PATH, "app")
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
    initial_sidebar_state="expanded",
)

# ==========================================================
# Premium CSS — glassmorphism, gradients, motion
# ==========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }

/* App background — soft animated gradient mesh */
.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(37,99,235,0.10) 0%, transparent 45%),
        radial-gradient(circle at 85% 10%, rgba(16,185,129,0.10) 0%, transparent 45%),
        radial-gradient(circle at 50% 90%, rgba(139,92,246,0.08) 0%, transparent 45%),
        #f4f7fb;
}

.block-container {
    padding-top: 1.2rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* ---------------- Hero ---------------- */
.hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(120deg, #1d4ed8 0%, #2563eb 45%, #0ea5e9 100%);
    padding: 48px 40px;
    border-radius: 28px;
    text-align: center;
    color: white;
    box-shadow: 0 20px 45px rgba(29,78,216,0.28);
    margin-bottom: 34px;
}
.hero::before {
    content: "";
    position: absolute;
    top: -60%; left: -20%;
    width: 140%; height: 220%;
    background: radial-gradient(circle, rgba(255,255,255,0.14) 0%, transparent 60%);
    transform: rotate(12deg);
}
.hero h1 {
    font-size: 2.4rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-bottom: 6px;
    position: relative;
}
.hero h4 {
    font-weight: 500;
    opacity: 0.92;
    position: relative;
}
.hero .badge-row {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 18px;
    flex-wrap: wrap;
    position: relative;
}
.hero .pill {
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.3);
    backdrop-filter: blur(6px);
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 600;
}

/* ---------------- Sidebar ---------------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
}
section[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
section[data-testid="stSidebar"] .stAlert {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px;
}

/* ---------------- Generic cards ---------------- */
.card, .recipe-card, .nutrition-card {
    color: #111827 !important;
}
.card h1, .card h2, .card h3, .card h4,
.recipe-card h1, .recipe-card h2, .recipe-card h3,
.nutrition-card h1, .nutrition-card h2, .nutrition-card h3 {
    color: #111827 !important;
}
.card p, .recipe-card p, .nutrition-card p { color: #4b5563 !important; }

.gradient-card, .gradient-card h1, .gradient-card h2,
.gradient-card h3, .gradient-card p { color: white !important; }

body, p { color: #374151; }
h1, h2, h3, h4, h5, h6 { color: #111827; }

/* Section labels */
.section-title {
    font-size: 1.4rem;
    font-weight: 800;
    color: #111827;
    margin: 6px 0 18px 0;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-title .accent {
    width: 6px;
    height: 22px;
    border-radius: 4px;
    background: linear-gradient(180deg, #2563eb, #10b981);
    display: inline-block;
}

/* Metric containers */
div[data-testid="metric-container"] {
    background: white;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 8px 24px rgba(15,23,42,0.06);
    border: 1px solid rgba(15,23,42,0.04);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
div[data-testid="metric-container"]:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 32px rgba(15,23,42,0.12);
}

/* Uploader */
section[data-testid="stFileUploader"] {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border: 1.5px dashed #93c5fd;
    box-shadow: 0 8px 24px rgba(15,23,42,0.05);
}

/* Nutrition stat tiles */
.stat-tile {
    padding: 24px 20px;
    border-radius: 20px;
    color: white;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.16);
    transition: transform 0.25s ease;
}
.stat-tile:hover { transform: translateY(-5px) scale(1.02); }
.stat-tile h3 { font-size: 0.95rem; font-weight: 600; opacity: 0.9; margin-bottom: 4px; }
.stat-tile h1 { font-size: 2.1rem; font-weight: 800; margin: 4px 0; }
.stat-tile p { font-size: 0.78rem; opacity: 0.85; margin: 0; }

/* Recipe cards */
.recipe-item {
    background: white;
    border-radius: 22px;
    padding: 22px 26px;
    margin-bottom: 16px;
    box-shadow: 0 8px 22px rgba(15,23,42,0.06);
    border: 1px solid rgba(15,23,42,0.04);
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.recipe-item:hover {
    transform: translateX(4px);
    box-shadow: 0 12px 28px rgba(15,23,42,0.10);
}
.recipe-badge {
    background: linear-gradient(135deg, #10b981, #34d399);
    padding: 8px 18px;
    border-radius: 30px;
    color: white;
    font-weight: 700;
    font-size: 0.82rem;
    white-space: nowrap;
}

/* Recommendation cards */
.rec-card {
    padding: 28px;
    border-radius: 24px;
    color: white;
    box-shadow: 0 14px 32px rgba(0,0,0,0.18);
}
.rec-card h2 { font-size: 1.1rem; font-weight: 700; opacity: 0.9; }
.rec-card h3 { font-size: 1.5rem; font-weight: 800; margin-top: -6px; }
.rec-card hr { border-color: rgba(255,255,255,0.3); margin: 16px 0; }

/* Confidence gauge */
.gauge-wrap { display: flex; justify-content: center; margin: 10px 0; }
.gauge {
    width: 190px; height: 190px;
    border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    font-size: 34px; font-weight: 800;
    box-shadow: 0 10px 26px rgba(0,0,0,0.14);
    background: white;
}

/* Buttons */
.stButton>button, .stDownloadButton>button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 26px;
    font-weight: 700;
    box-shadow: 0 8px 20px rgba(37,99,235,0.3);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 26px rgba(37,99,235,0.4);
}

.footer-note {
    text-align: center;
    color: #94a3b8;
    font-size: 0.8rem;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# Hero Banner
# ==========================================================

st.markdown(f"""
<div class="hero">
    <h1>🥗 AI Diet Recommendation System</h1>
    <h4>Deep Learning Powered Food Recognition &amp; Nutrition Analysis</h4>
    <div class="badge-row">
        <span class="pill">🧠 Computer Vision</span>
        <span class="pill">📊 Real-time Nutrition</span>
        <span class="pill">🍽 Recipe Engine</span>
        <span class="pill">📄 PDF Reports</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.markdown("## 🥗 AI Diet")
st.sidebar.caption(f"Session · {datetime.now().strftime('%b %d, %Y')}")
st.sidebar.markdown("---")

st.sidebar.markdown("#### Capabilities")
st.sidebar.success("✔ Food Detection")
st.sidebar.success("✔ Nutrition Analysis")
st.sidebar.success("✔ Healthy Recipes")
st.sidebar.success("✔ Diet Recommendation")

st.sidebar.markdown("---")
st.sidebar.info(
    """
**How it works**

1. Upload a food photo
2. AI detects the food item
3. View nutrition facts
4. Get recipes & diet advice
5. Download a PDF report
    """
)
st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit · TensorFlow · Keras")

# ==========================================================
# Model
# ==========================================================

MODEL_PATH = os.path.join(PROJECT_PATH, "models", "food_classifier.keras")

CLASS_NAMES = [
    "bacon", "banana", "bread", "broccoli", "butter", "carrots",
    "cheese", "chicken", "cucumber", "eggs", "fish", "lettuce",
    "milk", "onions", "peppers", "potatoes", "sausages",
    "spinach", "tomato", "yogurt",
]

# ==========================================================
# Load Model Only Once
# ==========================================================

@st.cache_resource
def load_system():
    predictor = ImagePredictor(MODEL_PATH, CLASS_NAMES)
    service = DietService()
    return predictor, service


predictor, service = load_system()

# ==========================================================
# Upload Image
# ==========================================================

st.markdown('<div class="section-title"><span class="accent"></span>Upload Your Food Photo</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Drag & drop or browse an image (JPG, JPEG, PNG)",
    type=["jpg", "jpeg", "png"],
)

# ==========================================================
# AI Prediction Dashboard
# ==========================================================

if uploaded_file is not None:

    file_bytes = uploaded_file.getvalue()

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    temp_file.write(file_bytes)
    temp_file.close()

    with st.spinner("🔍 Analyzing your food image..."):
        prediction = predictor.predict(temp_file.name)
        report = service.get_complete_report(prediction["food"])

    st.divider()

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<div class="section-title"><span class="accent"></span>Uploaded Food</div>', unsafe_allow_html=True)
        st.image(file_bytes, use_container_width=True)

    with right:
        st.markdown('<div class="section-title"><span class="accent"></span>AI Prediction</div>', unsafe_allow_html=True)

        confidence = prediction["confidence"] * 100

        m1, m2 = st.columns(2)
        with m1:
            st.metric("Detected Food", prediction["food"].title())
        with m2:
            st.metric("Confidence", f"{confidence:.2f}%")

        gauge_color = "#10B981"
        if confidence < 80:
            gauge_color = "#F59E0B"
        if confidence < 60:
            gauge_color = "#EF4444"

        st.markdown(
            f"""
            <div class="gauge-wrap">
                <div class="gauge" style="border:14px solid {gauge_color}; color:{gauge_color};">
                    {confidence:.0f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.progress(prediction["confidence"])
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

    st.markdown('<div class="section-title"><span class="accent"></span>Nutrition Information</div>', unsafe_allow_html=True)

    nutrition = report["nutrition"]

    tiles = [
        ("🔥", "Calories", nutrition.get("Calories", "N/A"), "kcal", "#F97316", "#FB923C"),
        ("🥩", "Protein", nutrition.get("Protein", "N/A"), "grams", "#2563EB", "#3B82F6"),
        ("🥑", "Fat", nutrition.get("Fat", "N/A"), "grams", "#10B981", "#34D399"),
        ("🍞", "Carbohydrates", nutrition.get("Carbohydrates", "N/A"), "grams", "#8B5CF6", "#A855F7"),
    ]

    cols = st.columns(4)
    for col, (icon, label, value, unit, c1, c2) in zip(cols, tiles):
        with col:
            st.markdown(f"""
            <div class="stat-tile" style="background:linear-gradient(135deg,{c1},{c2});">
                <h3>{icon} {label}</h3>
                <h1>{value}</h1>
                <p>{unit}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ==========================================================
    # 🍽 Recipe Cards
    # ==========================================================

    st.markdown('<div class="section-title"><span class="accent"></span>Healthy Recipe Suggestions</div>', unsafe_allow_html=True)

    recipes = report["recipes"]

    if recipes.empty:
        st.warning("No healthy recipes found.")
    else:
        recipe_list = recipes.head(5)

        for _, row in recipe_list.iterrows():
            st.markdown(f"""
            <div class="recipe-item">
                <div>
                    <h3 style="margin-bottom:4px;">🍽 {row['name'].title()}</h3>
                    <p style="margin:2px 0;">⏱ <b>Cooking Time:</b> {row['minutes']} minutes</p>
                    <p style="margin:2px 0;">🥗 <b>Ingredients:</b> {row['n_ingredients']}</p>
                </div>
                <span class="recipe-badge">Healthy</span>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ==========================================================
    # ❤️ Diet Recommendation
    # ==========================================================

    st.markdown('<div class="section-title"><span class="accent"></span>AI Diet Recommendation</div>', unsafe_allow_html=True)

    recommendation = report["recommendation"]

    card1, card2 = st.columns(2, gap="large")

    with card1:
        st.markdown(f"""
        <div class="rec-card" style="background:linear-gradient(135deg,#2563EB,#3B82F6);">
            <h2>🕒 Best Time</h2>
            <h3>{recommendation["best_time"]}</h3>
            <hr>
            <h2>💧 Water Intake</h2>
            <h3>{recommendation["water"]}</h3>
        </div>
        """, unsafe_allow_html=True)

    with card2:
        st.markdown(f"""
        <div class="rec-card" style="background:linear-gradient(135deg,#10B981,#34D399);">
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

    pdf_path = create_pdf(report, prediction)

    dl_col, _ = st.columns([1, 3])
    with dl_col:
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download AI Diet Report",
                data=pdf_file,
                file_name="AI_Diet_Report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    st.markdown('<p class="footer-note">Generated by AI Diet Recommendation System · For informational purposes only, not medical advice.</p>', unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align:center; padding:60px 20px; color:#94a3b8;">
        <h3>👆 Upload a food photo above to get started</h3>
        <p>Your personalized nutrition analysis and diet plan will appear here.</p>
    </div>
    """, unsafe_allow_html=True)
