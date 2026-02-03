import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def add_update_tab():
    st.subheader("Add / Update Expenses")

    selected_date = st.date_input(
        "Enter Date",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )

    selected_date_str = selected_date.strftime("%Y-%m-%d")

    # Fetch existing expenses
    try:
        response = requests.get(f"{API_URL}/expenses/{selected_date_str}")
        existing_expenses = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        st.error("API server not reachable")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        col1.text("Amount")
        col2.text("Category")
        col3.text("Notes")

        expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)

            amount_input = col1.number_input(
                "Amount",
                min_value=0.0,
                step=1.0,
                value=amount,
                key=f"amount_{i}",
                label_visibility="collapsed"
            )

            category_input = col2.selectbox(
                "Category",
                categories,
                index=categories.index(category),
                key=f"category_{i}",
                label_visibility="collapsed"
            )

            notes_input = col3.text_input(
                "Notes",
                value=notes,
                key=f"notes_{i}",
                label_visibility="collapsed"
            )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submit_button = st.form_submit_button("Save Expenses")

        if submit_button:
            filtered_expenses = [e for e in expenses if e["amount"] > 0]

            if not filtered_expenses:
                st.warning("Please enter at least one expense.")
                return

            try:
                response = requests.post(
                    f"{API_URL}/expenses/{selected_date_str}",
                    json=filtered_expenses
                )
                if response.status_code == 200:
                    st.success("Expenses updated successfully!")
                else:
                    st.error("Failed to update expenses.")
            except requests.exceptions.RequestException:
                st.error("Failed to connect to API.")
