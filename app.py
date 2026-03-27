import streamlit as st
import sqlite3
from datetime import datetime
from PIL import Image

# ✅ MUST BE FIRST
st.set_page_config(page_title="Aligna", layout="centered")

# -------------------------
# LOGO (centered)
# -------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("logo.png", width=140)

# spacing
st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# TITLE
# -------------------------
st.markdown(
    "<h1 style='text-align: center;'>Aligna</h1>",
    unsafe_allow_html=True
)


conn = sqlite3.connect("waitlist.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS waitlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    name TEXT,
    email TEXT,
    user_type TEXT
)
""")
conn.commit()

def save_signup(name: str, email: str, user_type: str):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    cur.execute(
        "INSERT INTO waitlist (timestamp, name, email, user_type) VALUES (?, ?, ?, ?)",
        (timestamp, name, email, user_type),
    )
    conn.commit()

st.markdown(
    """
    <h1 style='text-align: center;'> Aligna</h1>
    <h3 style='text-align: center;'>No swiping. Just real alignment.</h3>
    <p style='text-align: center; color: gray;'>
    A dating app for ambitious people who want meaningful, aligned relationships — powered by AI.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.subheader("Why Aligna is different")

col1, col2 = st.columns(2)

with col1:
    st.markdown("✅ AI-curated daily matches")
    st.markdown("✅ No endless swiping")
    st.markdown("✅ Intent-based dating")

with col2:
    st.markdown("✅ Built for ambitious people")
    st.markdown("✅ Higher-quality matches")
    st.markdown("✅ Less time wasted")

st.markdown("---")

st.subheader("Join the waitlist")

name = st.text_input("Your name")
email = st.text_input("Email")
user_type = st.selectbox(
    "What best describes you?",
    ["Entrepreneur", "Professional", "Student", "Other"]
)

if st.button("🚀 Join Waitlist"):
    if not name.strip() or not email.strip():
        st.error("Please fill all fields.")
    else:
        try:
            save_signup(name.strip(), email.strip(), user_type)
            st.success("You're on the list 🚀")
        except Exception as e:
            st.error("Signup failed.")
            st.exception(e)

st.warning("🔥 Only first 100 users get early access")

st.markdown("---")
st.caption("Aligna © 2026")
