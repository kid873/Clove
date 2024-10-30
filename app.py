import streamlit as st
import 어서와
import 날봐
import 여기를클릭하세요

def app():
    st.title("어서와!")
    st.write("이런 곳은 처음이지?ㅋㅋ")

page = st.sidebar.selectbox("Select a page", ["어서와!","날 봐!","여기를 클릭하세요"])

if page == "어서와!":
    Home.app()
elif page =="날 봐!":
    first.app()
elif page =="여기를 클릭하세요":
    second.app()

# st.title("메인 페이지")
# st.write("여기는 메인 페이지입니다.")
