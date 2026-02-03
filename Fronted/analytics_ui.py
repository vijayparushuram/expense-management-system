import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_tab():
    st.subheader("Expense Analytics")

    # Start and End dates side by side
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        try:
            response = requests.post(f"{API_URL}/analytics/", json=payload)
            response_data = response.json()
        except requests.exceptions.RequestException:
            st.error("Failed to fetch analytics")
            return

        if not response_data:
            st.warning("No data available for the selected date range.")
            return

        data = {
            "Category": list(response_data.keys()),
            "Total": [response_data[c]["total"] for c in response_data],
            "Percentage": [response_data[c]["percentage"] for c in response_data]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.markdown("### Expense Breakdown By Category")
        st.bar_chart(
            data=df_sorted.set_index("Category")["Percentage"],
            use_container_width=True
        )

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)
