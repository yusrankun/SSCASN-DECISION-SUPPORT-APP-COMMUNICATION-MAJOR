import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Rekomendasi CPNS", layout="wide")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("raw_cpns_ilmu_komunikasi.csv")
    return df

df = load_data()

# =========================
# PREPROCESSING
# =========================
df['gaji_min'] = pd.to_numeric(df['gaji_min'], errors='coerce')
df['gaji_max'] = pd.to_numeric(df['gaji_max'], errors='coerce')

df['gaji_avg'] = (df['gaji_min'] + df['gaji_max']) / 2

df['jumlah_formasi'] = pd.to_numeric(df['jumlah_formasi'], errors='coerce')
df['jumlah_ms'] = pd.to_numeric(df['jumlah_ms'], errors='coerce')

df['rasio_ketat'] = df['jumlah_ms'] / df['jumlah_formasi']
df['rasio_ketat'] = df['rasio_ketat'].replace([np.inf, -np.inf], np.nan)

# Extract provinsi (simple)
df['provinsi'] = df['lokasi_nm'].astype(str).apply(lambda x: x.split("|")[0])

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.title("🔎 Filter")

selected_provinsi = st.sidebar.multiselect(
    "Pilih Provinsi",
    options=sorted(df['provinsi'].dropna().unique())
)

min_gaji = st.sidebar.slider(
    "Minimal Gaji",
    int(df['gaji_min'].min()),
    int(df['gaji_max'].max()),
    int(df['gaji_min'].min())
)

selected_instansi = st.sidebar.multiselect(
    "Instansi (opsional)",
    options=sorted(df['ins_nm'].dropna().unique())
)

# =========================
# FILTERING
# =========================
df_filtered = df.copy()

if selected_provinsi:
    df_filtered = df_filtered[df_filtered['provinsi'].isin(selected_provinsi)]

df_filtered = df_filtered[df_filtered['gaji_min'] >= min_gaji]

if selected_instansi:
    df_filtered = df_filtered[df_filtered['ins_nm'].isin(selected_instansi)]

# =========================
# SCORING SYSTEM
# =========================
df_filtered['score'] = df_filtered['gaji_avg'] / (df_filtered['rasio_ketat'] + 1)

df_filtered = df_filtered.sort_values(by='score', ascending=False)

# =========================
# UI
# =========================
st.title("🎯 Rekomendasi Formasi CPNS - Ilmu Komunikasi")

st.markdown("""
Sistem ini membantu kamu menemukan formasi CPNS berdasarkan:
- 💰 Gaji
- 📍 Lokasi
- 🏢 Instansi
- ⚔️ Tingkat persaingan
""")

# =========================
# METRICS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Total Data", len(df_filtered))
col2.metric("Rata-rata Gaji", int(df_filtered['gaji_avg'].mean() or 0))
col3.metric("Rata-rata Rasio", round(df_filtered['rasio_ketat'].mean() or 0, 2))

# =========================
# TOP REKOMENDASI
# =========================
st.subheader("🔥 Top Rekomendasi")

top_n = st.slider("Jumlah rekomendasi", 5, 50, 10)

st.dataframe(
    df_filtered.head(top_n)[[
        'ins_nm',
        'jabatan_nm',
        'provinsi',
        'gaji_min',
        'gaji_max',
        'jumlah_formasi',
        'jumlah_ms',
        'rasio_ketat',
        'score'
    ]],
    use_container_width=True
)

# =========================
# EXPLORATION
# =========================
st.subheader("📊 Data Lengkap")

st.dataframe(df_filtered, use_container_width=True)

# =========================
# DOWNLOAD
# =========================
csv = df_filtered.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download hasil filter",
    data=csv,
    file_name='hasil_filter_cpns.csv',
    mime='text/csv'
)