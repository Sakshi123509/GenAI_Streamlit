import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit!")
st.write("Welcome to your first :streamlit: app.")
st.text("This is a simple example to get you started with Streamlit.")

name=st.text_input("Enter name: ")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

    df=pd.DataFrame(np.random.randn(10,2),columns=["A","B"])
    st.line_chart(df)
    st.bar_chart(df)

    st.sidebar.title("Sidebar")
    st.image("https://www.shutterstock.com/image-photo/sun-sets-behind-mountain-ranges-600nw-2479236003.jpg", caption="Beautiful Sunset")
    st.sidebar.text("This is the sidebar where you can add additional controls and information.")
    st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")

    upload_file=st.file_uploader("Upload a file", type='csv')
    if upload_file is not None:
        df=pd.read_csv(upload_file)
        st.dataframe(df)

    st.title("abc Text and Markdown Demo")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")
    st.code("for i in range(5): print(i)", language="python")
    
    st.text_input("What's your name?")
    st.text_area("Write something...")
    st.number_input("Pick a number", min_value=0, max_value=100)
    st.slider("Choose a range", 0, 100)
    st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
    st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
    st.radio("Pick one", ["Option A", "Option B"])
    st.checkbox("I agree to the terms")

    if st.checkbox("Show Details"):
        st.info("Here are more details...")



    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        st.success(f"Welcome, {username}!")
