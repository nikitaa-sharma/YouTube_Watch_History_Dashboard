import streamlit as st
from analyze import load_data
import visualizations as vz
import matplotlib.pyplot as plt

st.set_page_config(page_title="YouTube Watch History Dashboard", layout="wide")
st.title("📊 YouTube Watch History Dashboard")

uploaded_file = st.file_uploader("Upload your watch-history.json", type="json")

if uploaded_file:
    df = load_data(uploaded_file)

    st.success("File loaded successfully!")
    
    # Top Channels
    st.subheader("🎥 Top Watched Channels")
    st.plotly_chart(vz.top_channels_chart(df), use_container_width=True)

    # Activity by Hour
    st.subheader("⏰ Watching Activity by Hour")
    st.plotly_chart(vz.activity_by_hour(df), use_container_width=True)

    # Weekday Activity
    st.subheader("📅 Watching by Day of Week")
    st.plotly_chart(vz.day_of_week_chart(df), use_container_width=True)

    # Wordcloud
    st.subheader("🔠 Word Cloud of Watched Titles")
    wc = vz.generate_wordcloud(df)
    fig = vz.generate_wordcloud(df)
    st.pyplot(fig)
