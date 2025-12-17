# C:\Users\Ayush Yadav\ticketboard\frontend\app.py

import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

# === CONFIGURATION ===
# Replace with your EC2 public IP
BACKEND_URL = "http://16.171.114.116:8080"
USERNAME = "admin"
PASSWORD = "securepassword"

# === STREAMLIT UI ===
st.set_page_config(page_title="TicketBoard", layout="wide")
st.title("🎫 TicketBoard - MicroService")
st.markdown("A CI/CD-deployed microservice for managing technical tickets.")

# === FETCH TICKETS ===
def get_tickets():
    try:
        response = requests.get(
            f"{BACKEND_URL}/tickets",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"⚠️ Backend returned: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Failed to connect to backend: {str(e)}")
        return []

# === CREATE TICKET ===
def create_ticket(title, desc, priority, status):
    payload = {
        "title": title,
        "description": desc,
        "priority": priority,
        "status": status
    }
    try:
        response = requests.post(
            f"{BACKEND_URL}/tickets",
            json=payload,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )
        return response.status_code == 200
    except Exception as e:
        st.error(f"❌ Create failed: {str(e)}")
        return False

# === UI: CREATE FORM ===
st.subheader("➕ Create New Ticket")
with st.form("create_ticket"):
    title = st.text_input("Title", placeholder="e.g., Login not working")
    desc = st.text_area("Description", placeholder="Steps to reproduce...")
    priority = st.selectbox("Priority", ["LOW", "MEDIUM", "HIGH"])
    status = st.selectbox("Status", ["OPEN", "IN_PROGRESS", "RESOLVED"])
    submitted = st.form_submit_button("Submit Ticket")
    
    if submitted:
        if title.strip():
            if create_ticket(title, desc, priority, status):
                st.success("✅ Ticket created successfully!")
                st.rerun()  # Refresh list
            else:
                st.error("❌ Failed to create ticket")
        else:
            st.warning("⚠️ Title cannot be empty")

# === UI: DISPLAY TICKETS ===
st.subheader("📋 All Tickets")
tickets = get_tickets()

if tickets:
    for t in tickets:
        with st.expander(f"**{t.get('title', 'No Title')}** | {t.get('priority')} | {t.get('status')}"):
            st.write(f"**Created:** {t.get('createdAt', 'N/A')}")
            st.write(t.get('description', ''))
else:
    st.info("📭 No tickets yet. Create one above!")