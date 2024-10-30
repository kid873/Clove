import streamlit as st
import Home
import first
import second

def app():
    st.title("Home")
    st.write("Welcome to the Home page!")

page = st.sidebar.selectbox("Select a page", ["Hey","Look at me!","Hurry up"])

if page == "Hey":
    Home.app()
elif page =="Look at me!":
    first.app()
elif page =="Hurry up":
    second.app()

# st.title("메인 페이지")
# st.write("여기는 메인 페이지입니다.")
