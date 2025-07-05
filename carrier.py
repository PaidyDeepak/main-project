import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import os
import json
from datetime import datetime

# Main function to run the career guidance app
def show_carrier():
    if "history" not in st.session_state:
        st.session_state.history = {}

    # Load environment variables and configure API
    load_dotenv()
    api = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api)

    # Initialize history dictionary
    st.set_page_config(page_title="Career Guidance Assistant", layout="centered")
    if st.session_state.get("logged_in", False):
        st.write(f"Welcome, **{st.session_state.username}**! You are now logged in.")
        tab1, tab2, tab3 = st.tabs(["Home", "ChatBot", "Hisory"])
        with tab1:
            # Check for API key
            if not api:
                st.error("Google API Key not found. Please set GOOGLE_API_KEY in your .env file.")
                st.info("Get your API key from: https://aistudio.google.com/app/apikey")
                st.stop()
            # Page setup
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
            # Layout columns
            col1, col2 = st.columns([5, 1])
            s1, s2 = st.columns([1, 1])
            r1, r2 = st.columns([5, 1])
            c1, c2 = st.columns([5, 1])
            co1, co2 = st.columns([5, 1])
            
            
            # Function to generate career guidance response
            def get_carrier_guidence(prompt):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(prompt)
                    st.subheader("Response is generated:")
                    return response.text
                except Exception as e:
                    return f"Error: {e}"

            # Sidebar: Profile and History
            with col1:
                st.subheader("👤 Your Profile")
                with s1:
                    interests = st.text_input("Interests", placeholder="Generative AI, Full Stack")
                    skills = st.text_input("Skills", placeholder="Python, C++")
                with s2:
                    education = st.text_input("Highest Education Received", placeholder="B.Tech")
                    exp = st.text_input("Experience", placeholder="5 years")
                with s1:
                    if st.button("Save", type="primary"):
                        if interests and skills and education and exp:
                            st.subheader(":green-background[Saved Successfully!!]")
                        else:
                            st.error("Please fill your details in profile !!!!")
            
            # Suggested Questions
            with r1:
                st.markdown("Suggested Questions:")
                sample_tags = [
                    "How can I become a cloud Engineer with my background and skills?",
                    "With my profile, what should I do to be successful in my career?",
                    "Can I become a cloud engineer with my skills and education?",
                    "What are the highest paying jobs I can get with my profile?",
                ]
                with st.expander("Click to expand"):
                    for tag in sample_tags:
                        if st.button(tag):
                            st.session_state["tags"] = st.session_state.get("tags", "") + f"{tag}, "

            # Question input
            with c1:
                question = st.text_input(
                    "Chat with our Bot for your doubts:",
                    placeholder="With my profile what should I do?",
                    key="tags"
                )

            # Footer
            with co1:
                st.markdown("----")
                st.subheader("Created by Deepak")
                st.markdown("Built using Streamlit and Gemini")

            # Submit button
            with c2:
                if st.button("Submit"):
                    with c1:
                        if not (interests and skills and education and exp):
                            st.error("Please fill your details in profile !!!!")
                        elif question:
                            prompt = (
                                f"My interests are {interests}. My skills are {skills}. "
                                f"My educational background is {education}. My experience is {exp}. "
                                f"Here is my question: {question}."
                            )
                            with st.spinner("Generating response..."):
                                result = get_carrier_guidence(prompt)
                            st.markdown(result)
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            username = st.session_state.username 
                            st.session_state.history[question] = {
                                "user": username,
                                "time": timestamp,
                                "answer": result
                            }


        with tab3:
            # Function to display history
            def show_history():
                if not st.session_state.history:
                    st.error("History is Empty")
                else:
                    for q, a in st.session_state.history.items():
                        st.markdown("----")
                        st.markdown(f"**Question:** {q}  \n→ **Answer:** {a}")
                    if st.button("Save History"):
                        h = pd.DataFrame([
                            {
                                "question": q,
                                "answer": a["answer"],
                                "user": a["user"],
                                "time": a["time"]
                            }
                            for q, a in st.session_state.history.items()
                        ])
                        h.to_json("history.json", orient="records", indent=2)
                        st.success("History saved successfully.")


                st.markdown("----")
                st.subheader("Created by Deepak")
                st.markdown("Built using Streamlit and Gemini")
            
            show_history()
    else:
        st.warning("You must log in first.")
    
