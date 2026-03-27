import streamlit as st
import sqlite3
from datetime import datetime
from PIL import Image

# -------------------------
# PAGE CONFIG (MUST BE FIRST)
# -------------------------
st.set_page_config(page_title="Aligna", layout="centered")

# -------------------------
# DATABASE
# -------------------------
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

# -------------------------
# FUNCTIONS
# -------------------------
def save_signup(name, email, user_type):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(
        "INSERT INTO waitlist (timestamp, name, email, user_type) VALUES (?, ?, ?, ?)",
        (timestamp, name, email, user_type)
    )
    conn.commit()

def get_signups():
    return cur.execute("SELECT * FROM waitlist").fetchall()

def email_exists(email):
    result = cur.execute(
        "SELECT * FROM waitlist WHERE email = ?", (email,)
    ).fetchone()
    return result is not None

# -------------------------
# LOGO (CENTERED)
# -------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", width=140)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown(
    "<h1 style='text-align: center;'>Aligna</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>No swiping. Just real alignment.</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: gray;'>A dating app for ambitious people who want meaningful, aligned relationships — powered by AI.</p>",
    unsafe_allow_html=True
)

# -------------------------
# SOCIAL PROOF 🔥
# -------------------------
rows = get_signups()
st.markdown(f"<h4 style='text-align: center;'>🔥 {len(rows)} people already joined</h4>", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# FEATURES
# -------------------------
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

# -------------------------
# FORM
# -------------------------
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
    elif email_exists(email.strip()):
        st.warning("This email is already on the waitlist.")
    else:
        save_signup(name.strip(), email.strip(), user_type)
        st.success("You're in 🚀 We'll notify you when we launch.")

# urgency
st.warning("🔥 Only first 100 users get early access")

st.markdown("---")

# -------------------------
# ADMIN PANEL (HIDDEN)
# -------------------------
with st.expander("🔒 Admin Access"):
    password = st.text_input("Enter admin password", type="password")

    if password == "aligna_admin_2026":
        rows = get_signups()
        st.success(f"Total signups: {len(rows)}")
        st.dataframe(rows)

# -------------------------
# FOOTER
# -------------------------
st.caption("Aligna © 2026")
