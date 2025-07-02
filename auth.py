import streamlit as st
import sqlite3

DB_PATH = 'users.db'

def check_credentials(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def create_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login():
    st.title("🔐 Welcome to Health Assistant")

    tab1, tab2 = st.tabs(["🔓 Login", "📝 Sign Up"])

    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            if check_credentials(username, password):
                st.success("Login successful!")
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with tab2:
        new_user = st.text_input("Choose a Username", key="signup_user")
        new_pass = st.text_input("Choose a Password", type="password", key="signup_pass")
        confirm = st.text_input("Confirm Password", type="password", key="signup_confirm")

        if st.button("Register"):
            if new_pass != confirm:
                st.error("Passwords do not match.")
            elif new_user.strip() == "":
                st.warning("Username cannot be empty.")
            elif create_user(new_user, new_pass):
                st.success("Registration successful! Please log in.")
            else:
                st.error("Username already exists.")
