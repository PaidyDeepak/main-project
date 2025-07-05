import streamlit as st
import pandas as pd
import bcrypt
import os

def show_login():
    USER_FILE = "users.csv"
    # Ensure CSV exists
    if not os.path.exists(USER_FILE):
        df = pd.DataFrame(columns=["username", "email", "password"])
        df.to_csv(USER_FILE, index=False)

    # Helper functions
    def check_password(password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    def load_users():
        return pd.read_csv(USER_FILE)

    # Session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""

    # Login Form
    st.header("🔐 Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            users = load_users()
            user_row = users[users["username"] == username]

            if not user_row.empty and check_password(password, user_row.iloc[0]["password"]):
                st.success(f"Welcome, {username}!")
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("Invalid username or password.")

