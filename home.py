import streamlit as st
import os
from admin import show_admin

def show_home():
    if st.session_state.get("logged_in", False):
        st.title("Home Page")
        st.write(f"Welcome, **{st.session_state.username}**! You are now logged in.")
        st.subheader("We Have following ChatBots:")
        tab1, tab2, tab3 = st.tabs(["Career Guidence ChatBot", "Document Explainer ChatBot", "Url loader"])
        with tab1:
            st.title("🎓 Generative AI-Powered Career Guidance Assistant")
            st.markdown("""
                Welcome to your personalized career advisor.
                You are an advanced AI-powered career guidance chatbot designed to assist students and professionals in choosing the best career path based on their aptitude, aspirations, skills, and work experience. 
                Your goal is to provide highly personalized and data-driven career recommendations.
            """)
            st.markdown("Fill out your background information and ask career-related questions in ChatBot.")
            st.markdown("----")
            st.subheader("Created by Deepak")
            st.markdown("Built using Streamlit and Gemini")
        with tab2:
            st.markdown("Document Explainer Chatbot")
        with tab3:
            st.markdown("Url loader Chatbot")

    else:
        st.warning("You must log in first.")
show_home()

