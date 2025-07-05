import streamlit as st
from login import show_login
from home import show_home
from carrier import show_carrier
from signup import show_signup
from admin import show_admin
# Navigation
page = st.sidebar.radio("Navigate", ["SignUp","Login", "Home","Career Guidence Chatbot","Admin"])

if page=="SignUp":
    show_signup()
elif page == "Login":
    show_login()
elif page == "Home":
    show_home()
elif page == "Career Guidence Chatbot":
    show_carrier()
elif page=="Admin":
    if st.session_state.get("logged_in", False):
        user=st.session_state.username
        if user=="Admin":
            show_admin()
        else:
            st.sidebar.error("You are not a Admin")
    else:
        st.sidebar.info("Please Login")

if st.session_state.get("logged_in", False):
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()


