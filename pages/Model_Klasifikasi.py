import streamlit as st
from PIL import Image

st.header(''' 
Demo Model Klasifikasi
''')

uploaded_files = st.file_uploader("Upload Gambar", accept_multiple_files=False, type=["Jpg", "Jpeg", "PNG"])

if uploaded_files is not None:
    st.success("File Sukses diupload")
    image_upload = Image.open(uploaded_files)
    st.image(image_upload,caption='Gambar yang diunggah', use_column_width=True, width=200)

if st.button("Prediksi", type="primary"):
    st.write('Prediksi Sukses')
