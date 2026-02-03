import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab

st.set_page_config(page_title="Expense Tracking System", layout="wide")
st.title("Expense Tracking System 💰")

tab1, tab2 = st.tabs(["➕ Add / Update", "📊 Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()
