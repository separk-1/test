import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px

# 페이지 이름
st.set_page_config(
    page_icon = "⚖️",
    page_title = "bidding game",
    layout = "wide",
)

def split_line(n):
    for i in range(n):
        st.write("\n")
    return

# text 색상
def text_64(text):
    st.markdown(f'<p style="color:#000000;font-size:64px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

def text_32(text):
    st.markdown(f'<p style="color:#000000;font-size:32px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

def text_24(text):
    st.markdown(f'<p style="color:#000000;font-size:24px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

def text_18(text):
    st.markdown(f'<p style="color:#000000;font-size:18px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

def text_32_highlight(text):
    st.markdown(f'<p style="color:#476600;font-size:32px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

# 포맷 깔끔하게
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# header
text_64("bidding game\n")
split_line(2)

#############
