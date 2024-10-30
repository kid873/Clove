import streamlit as st
import Home
import first
import second

def app():
    st.title("Home")
    st.write("Welcome to the Home page!")

page = st.sidebar.selectbox("Select a page", ["Home","first","second"])

if page == "어디봐?":
    Home.app()
elif page =="날 봐!":
    first.app()
elif page =="여기를 클릭하세요":
    second.app()

# st.title("메인 페이지")
# st.write("여기는 메인 페이지입니다.")
