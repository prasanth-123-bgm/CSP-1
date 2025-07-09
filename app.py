
import streamlit as st
import pandas as pd
import pickle
from gtts import gTTS
from io import BytesIO
from weather import get_weather, get_weather_telugu, get_weather_hindi

# Safe model loading
try:
    with open("crop_model.pkl", "rb") as f:
        crop_model = pickle.load(f)
except Exception as e:
    st.error(f"❌ crop_model.pkl loading failed: {e}")
    st.stop()

try:
    with open("label_encoder.pkl", "rb") as f:
        le = pickle.load(f)
except Exception as e:
    st.error(f"❌ label_encoder.pkl loading failed: {e}")
    st.stop()

def speak(text, lang='te'):
    try:
        tts = gTTS(text=text, lang=lang)
        fp = BytesIO()
        tts.write_to_fp(fp)
        st.audio(fp.getvalue(), format='audio/mp3')
    except Exception as e:
        st.warning(f"Voice output failed: {e}")

st.set_page_config(page_title="Agri Voice Assistant", layout="centered")
st.title("🌿 Agri Voice Assistant (Weather + Crop)")
lang = st.radio("Language", ["English", "తెలుగు", "हिन्दी"])

st.header("🌤️ Weather Forecast")
city = st.text_input("Enter City Name")
if st.button("Get Weather"):
    if city:
        if lang == "తెలుగు":
            report = get_weather_telugu(city)
            speak(report, 'te')
        elif lang == "हिन्दी":
            report = get_weather_hindi(city)
            speak(report, 'hi')
        else:
            report = get_weather(city)
            speak(report, 'en')
        st.text_area("Weather Info", report, height=150)

st.header("🌱 Crop Recommendation")
n = st.number_input("Nitrogen (N)", 0, 200)
p = st.number_input("Phosphorus (P)", 0, 200)
k = st.number_input("Potassium (K)", 0, 200)
temp = st.number_input("Temperature (°C)", 10.0, 50.0)
hum = st.number_input("Humidity (%)", 10.0, 100.0)
ph = st.number_input("pH", 0.0, 14.0)
rain = st.number_input("Rainfall (mm)", 0.0, 500.0)

if st.button("Recommend Crop"):
    features = [[n, p, k, temp, hum, ph, rain]]
    prediction = crop_model.predict(features)[0]
    crop = le.inverse_transform([prediction])[0]
    output = f"సిఫారసు చేసిన పంట: {crop}" if lang == "తెలుగు" else f"अनुशंसित फसल: {crop}" if lang == "हिन्दी" else f"Recommended Crop: {crop}"
    st.success(output)
    speak(output, lang='te' if lang == "తెలుగు" else 'hi' if lang == "हिन्दी" else 'en')
