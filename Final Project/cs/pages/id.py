import streamlit as st
from PIL import Image
import os

st.title("💀 Internship Profile 💀")
st.markdown("---")

# Load profile photo
image_path = "assets/face.png"  # or use "assets/chandan.jpg" if it's in a folder
if os.path.exists(image_path):
    img = Image.open(image_path)
    st.image(img, width=200, caption="Chandan Suthar")
else:
    st.warning("⚠️ Profile photo not found. Please add '.jpg' in your assets directory.")

st.header("Name")
st.write("**Chandan Suthar**")

st.header("Basic Details")
st.markdown("""
- **Student ID:** CT_CSI_DS_5312  
- **Start Date:** 28/05/2025  
- **Domain:** Data Science  
- **Stream:** B.Tech  
- **Passing Out Year:** 2026  
- **College Name:** Poornima Institute of Engineering and Technology  
- **Batch:** Batch 2  
""")

st.header("🔗 Social Links")

st.markdown("""
- [Portfolio](https://darkling.pythonanywhere.com/)
- [LinkedIn](https://www.linkedin.com/in/chandansuthar007)
- [GitHub](https://github.com/ChandanSuthar/)
""")

gif_path = "assets/CoffeeCat.gif"
st.image(gif_path)