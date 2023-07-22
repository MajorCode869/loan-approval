import streamlit as st
import sys
sys.path.append('C:\celebal\lap\src')

from prediction_page import show_predict_page



page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_predict_page()

    