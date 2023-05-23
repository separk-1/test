import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import plotly.express as px

from trubrics.integrations.streamlit import FeedbackCollector

# page
st.set_page_config(
    page_icon = "⚖️",
    page_title = "bidding game",
    layout = "wide",
)

def split_line(n):
    for i in range(n):
        st.write("\n")
    return

# text
def text_32(text):
    st.markdown(f'<p style="color:#000000;font-size:32px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)

def text_18(text):
    st.markdown(f'<p style="color:#000000;font-size:18px;border-radius:2%;">{text}</p>', unsafe_allow_html=True) 

# format
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# header
text_18("bidding game\n")
split_line(2)

#############
collector = FeedbackCollector()
collector.st_feedback(feedback_type="issue")

feedback = collector.st_feedback(
	feedback_type="thumbs",
	path="thumbs_feedback.json"
)

# print out the feedback object as a dictionary in your app
feedback.dict() if feedback else None
