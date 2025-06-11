import os
os.environ["STREAMLIT_HOME"] = os.getcwd()  # Ensure Streamlit writes config to a writable path

import streamlit as st

st.set_page_config(page_title="🌾 AgriBot - Smart Farming Assistant", page_icon="🌾")

# --- Helper Data ---
SOIL_TYPES = ["Sandy", "Clay", "Loamy", "Peaty", "Saline", "Silty", "Red"]
IRRIGATION_METHODS = ["Drip", "Sprinkler", "Flood", "Manual"]
CROPS = ["Wheat", "Rice", "Maize", "Sugarcane", "Potato", "Cotton", "Soybean", "Groundnut"]

MOCK_WEATHER = {
    "Delhi": "Sunny, 36°C, Humidity: 22%",
    "Mumbai": "Cloudy, 30°C, Humidity: 78%",
    "Bengaluru": "Rainy, 24°C, Humidity: 88%",
    "Chennai": "Sunny, 34°C, Humidity: 62%"
}

PEST_TIPS = {
    "Wheat": "Watch for aphids and rust disease. Use neem oil and crop rotation.",
    "Rice": "Stem borers and leaf folders are common. Maintain field hygiene and use pheromone traps.",
    "Maize": "Armyworms and shoot fly are major pests. Early sowing and seed treatment recommended.",
    "Sugarcane": "Monitor for borers. Remove infested canes and use biocontrol agents.",
    "Potato": "Late blight is a risk. Avoid overhead irrigation and use certified seeds.",
    "Cotton": "Bollworms and whiteflies are common. Use resistant varieties and trap crops.",
    "Soybean": "Look out for leaf-eating caterpillars. Practice crop rotation.",
    "Groundnut": "Termites and leaf miners attack. Drench soil and use organic mulches."
}

CROP_RULES = {
    ("Sandy", "Drip"): ["Groundnut", "Cotton"],
    ("Clay", "Flood"): ["Rice", "Sugarcane"],
    ("Loamy", "Sprinkler"): ["Wheat", "Potato", "Maize"],
    ("Peaty", "Manual"): ["Potato", "Wheat"],
    ("Silty", "Sprinkler"): ["Maize", "Soybean"],
    ("Saline", "Drip"): ["Cotton", "Barley"]
}

# --- Sidebar Inputs ---
st.sidebar.header("Farm Details")
location = st.sidebar.selectbox("Location", list(MOCK_WEATHER.keys()), index=0)
soil_type = st.sidebar.selectbox("Soil Type", SOIL_TYPES)
irrigation = st.sidebar.selectbox("Irrigation Method", IRRIGATION_METHODS)
interested_crops = st.sidebar.multiselect("Interested Crops", CROPS, default=["Wheat"])

st.sidebar.markdown("---")
if st.sidebar.button("Show Weather Forecast"):
    st.sidebar.info(f"Weather in {location}: {MOCK_WEATHER[location]}")

# --- Main UI ---
st.title("🌾 AgriBot - Smart Farming Assistant")
st.write("Personalized crop recommendations, weather updates, pest tips, and Q&A for smart farming decisions.")

st.header("1️⃣ Personalized Crop Recommendations")
def recommend_crops(soil, irrigation, interests):
    # Rule-based matching
    recs = []
    for (soil_rule, irrig_rule), crops in CROP_RULES.items():
        if soil == soil_rule and irrigation == irrig_rule:
            recs.extend([c for c in crops if c in interests])
    if not recs:
        # Fallback: suggest from interests
        recs = interests
    return recs

recommended_crops = recommend_crops(soil_type, irrigation, interested_crops)
if recommended_crops:
    st.success(f"Recommended Crops for your field: {', '.join(recommended_crops)}")
else:
    st.warning("No matching crops found. Try changing your selections.")

st.header("2️⃣ Pest Control Tips")
for crop in interested_crops:
    if crop in PEST_TIPS:
        st.markdown(f"**{crop}:** {PEST_TIPS[crop]}")

st.header("3️⃣ Ask AgriBot (Q&A) 👩‍🌾")
user_query = st.text_input("Ask me anything about crops, soil, weather, or pests:")

def basic_qa(query):
    q = query.lower()
    if "red soil" in q:
        return ("Red soil is typically sandy to loamy in texture, rich in iron (which gives it the red color), "
                "usually acidic, low in nitrogen, humus, and phosphorus, and best suited for crops like groundnut, "
                "millets, potato, and cotton. It has good drainage but needs fertilization for high productivity.")
    if "winter" in q and "crop" in q:
        return "Best winter crops include Wheat, Mustard, and Barley."
    if "fertilizer" in q and "rice" in q:
        return "For rice, use NPK fertilizers in a 2:1:1 ratio along with organic manure."
    if "irrigation" in q and "wheat" in q:
        return "Wheat prefers sprinkler or surface irrigation, especially at the crown root initiation stage."
    if "best soil" in q and "potato" in q:
        return "Loamy and sandy soils with good drainage are best for potatoes."
    if "weather" in q:
        return f"Weather in {location}: {MOCK_WEATHER[location]}"
    return "Sorry, I don't know the answer yet. Try asking about crops, soil, weather, or pests!"

if user_query:
    st.info(f"AgriBot: {basic_qa(user_query)}")

st.caption("👨‍🌾 Powered by Streamlit | Ready for OpenAI / Hugging Face integration!")
