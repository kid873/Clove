import streamlit as st
import Home
import first
import second

def app():Home")
    st.write("Welcome to Homepage")

page = st.sidebar.selectbox("Select a page", ["Home","first","second"])

if page == "Home":
    Home.app()
elif page =="first":
    first.app()
elif page =="second":
    second.app()

# st.title("메인 페이지")
# st.write("여기는 메인 페이지입니다.")
