import streamlit as st 
import pandas as panda
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="dark")
sidebar_bg_color = '#0c1e3c'
text_color = '#b3cde3'
highlight_color = '#ffcc00'


st.markdown(
    f"""
    <style>
        /* Center sidebar content */
        .sidebar .sidebar-content {{
            background-color: {sidebar_bg_color};
            color: {text_color};
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}
        /* Style for text elements in the sidebar */
        .sidebar h2, .sidebar p {{
            text-align: center;
            color: {text_color};
        }}
        /* Main background and text styling */
        .main .block-container {{
            background-color: #1b2638;
            color: {text_color};
        }}
        .main h1 {{
            color: {highlight_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(f"<h2>Proyek Analisis Data</h2>", unsafe_allow_html=True)
st.sidebar.markdown(f"<p>Nama: Kevin Junus Ketti</p>", unsafe_allow_html=True)
st.sidebar.markdown(f"<p>Email: kevinketti218@gmail.com</p>", unsafe_allow_html=True)
st.sidebar.markdown(f"<p>ID Dicoding: kevinjunusketti</p>", unsafe_allow_html=True)

st.title("Analisis Data E-Commerce Public Dataset")
st.markdown(f"<p style='color:{highlight_color};'>Pilih tipe analisis di sidebar untuk memulai.</p>", unsafe_allow_html=True)







st.markdown("---")
st.markdown("Dikembangkan oleh Kevin Junus Ketti | Email: kevinketti218@gmail.com")