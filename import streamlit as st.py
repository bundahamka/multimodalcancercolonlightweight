import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
from PIL import Image, ImageOps

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Marina AI Framework", layout="wide", page_icon="🔬")

# --- CUSTOM CSS (Biar tampilan berkelas) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("👨‍⚕️ Clinical Decision Support System (CDSS)")
st.subheader("Lightweight Multi-Modal Hybrid AI Framework for Colorectal Cancer")
st.write("Developed by: **Marina Artiyasa (20250130009)**")

# --- SIDEBAR: INPUT DATA ---
with st.sidebar:
    st.image("https://via.placeholder.com/150?text=Logo+Nusa+Putra", width=100) # Ganti logo kampus
    st.header("📂 Patient Data Input")
    
    # 1. Input Histopatologi (EfficientNet-Lite)
    st.info("Modalitas 1: Histopathology")
    file_histo = st.file_uploader("Upload SVS/JPG Tissue Slide", type=['jpg', 'png', 'jpeg'], key="histo")
    
    # 2. Input Kolonoskopi (MobileViT)
    st.info("Modalitas 2: Colonoscopy")
    file_colon = st.file_uploader("Upload Endoscopy Frame", type=['jpg', 'png', 'jpeg'], key="colon")
    
    # 3. Input Omics (MLP)
    st.info("Modalitas 3: Omics Data")
    file_omics = st.file_uploader("Upload Genomic Profile (CSV)", type=['csv'], key="omics")
    
    st.divider()
    run_btn = st.button("🔍 ANALYZE MULTIMODAL DATA")

# --- MAIN CONTENT ---
if run_btn:
    if not (file_histo and file_colon and file_omics):
        st.warning("⚠️ Mohon lengkapi ketiga data (Trimodal) untuk hasil yang presisi.")
    else:
        # --- SIMULASI PROSES AI ---
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            time.sleep(0.01) # Simulasi latensi 100ms
            progress_bar.progress(i + 1)
            if i < 30: status_text.text("Extracting Spasial Features (EfficientNet-Lite0)...")
            elif i < 60: status_text.text("Processing Sequence Context (MobileViT-S)...")
            elif i < 85: status_text.text("Aligning Omics Latent Space...")
            else: status_text.text("Performing Attention-based Fusion...")

        # --- HASIL DIAGNOSIS ---
        st.divider()
        res_col1, res_col2, res_col3 = st.columns([1, 1, 1])
        
        with res_col1:
            st.success("### Prediction")
            st.metric(label="Status", value="MALIGNANT", delta="High Risk")
            st.write("**Confidence Score:** 98.42%")
            st.write("**Inference Time:** 88ms (Lightweight)")

        with res_col2:
            st.info("### Explainable AI: Grad-CAM")
            # Simulasi Heatmap
            img = Image.open(file_colon)
            st.image(img, caption="Red Zone: Tumor Localization", use_column_width=True)
            st.caption("AI menyoroti area vaskularisasi abnormal pada mukosa.")

        with res_col3:
            st.warning("### Genomic Factors (SHAP)")
            # Simulasi Data Genetik
            gen_data = pd.DataFrame({
                'Gene': ['APC', 'TP53', 'KRAS', 'SMAD4', 'PIK3CA'],
                'Contribution': [0.45, 0.38, 0.12, 0.03, 0.02]
            })
            fig = px.bar(gen_data, x='Contribution', y='Gene', orientation='h', color='Contribution')
            st.plotly_chart(fig, use_container_width=True)

        # --- DOKTER VERIFICATION ---
        st.divider()
        st.text_area("Doctor's Clinical Notes:", placeholder="Tuliskan catatan verifikasi di sini...")
        st.button("📄 Generate Report (PDF)")

else:
    # Tampilan awal saat belum ada data
    st.info("Silakan unggah data pasien pada sidebar untuk memulai simulasi framework AI.")
    # Kasih liat diagram alir sistem di sini
    st.image("https://via.placeholder.com/800x400?text=Diagram+Arsitektur+Hybrid+AI+Marina", caption="Overview of Proposed Framework")