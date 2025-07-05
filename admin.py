import streamlit as st
import pandas as pd

st.set_page_config(page_title="Admin Page",layout="centered")
def show_admin():
    st.title("Admin page")
    # Load the CSV file
    df = pd.read_csv("users.csv")  # Replace with your actual file path

    # Display all users
    st.write("All Registered Users:")
    st.dataframe(df)

    # Optionally, access specific columns
    usernames = df["username"].tolist()
    emails = df["email"].tolist()
    passwords = df["password"].tolist()

