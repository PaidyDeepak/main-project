import streamlit as st
import pandas as pd
import bcrypt
import os

def show_signup():
    USER_FILE = "users.csv"

    # Ensure CSV exists
    if not os.path.exists(USER_FILE):
        df = pd.DataFrame(columns=["username", "email", "password"])
        df.to_csv(USER_FILE, index=False)

    # Helper functions
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def save_user(username, email, hashed_pw):
        df = pd.read_csv(USER_FILE)
        new_user = pd.DataFrame([[username, email, hashed_pw]], columns=["username", "email", "password"])
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(USER_FILE, index=False)

    # SignUp Form
    st.header("📝 Sign Up")

    with st.form("signup_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Register")

        if submit:
            if not username or not email or not password or not confirm_password:
                st.error("Please fill in all fields.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            else:
                hashed_pw = hash_password(password)
                save_user(username, email, hashed_pw)
                st.success("User registered successfully!")

