import streamlit as st
import plotly.express as px
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Analysis Dashboard")

# ----------------------------
# Sample Dataset
# ----------------------------
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [20000, 25000, 30000, 28000, 35000, 40000],
    "Customers": [150, 180, 210, 190, 230, 260],
    "Region": ["North", "South", "East", "West", "North", "South"]
})

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("Filter Options")

selected_region = st.sidebar.selectbox(
    "Select Region",
    options=df["Region"].unique()
)

filtered_df = df[df["Region"] == selected_region]

# ----------------------------
# Layout Columns
# ----------------------------
col1, col2 = st.columns(2)

# Line Chart
with col1:
    st.subheader("Monthly Sales Trend")
    fig1 = px.line(
        filtered_df,
        x="Month",
        y="Sales",
        markers=True,
        title="Sales Trend"
    )
    st.plotly_chart(fig1, use_container_width=True)

# Bar Chart
with col2:
    st.subheader("Customer Count")
    fig2 = px.bar(
        filtered_df,
        x="Month",
        y="Customers",
        title="Customers per Month"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Pie Chart
# ----------------------------
st.subheader("Sales Distribution by Region")

fig3 = px.pie(
    df,
    names="Region",
    values="Sales",
    title="Regional Sales Contribution"
)

st.plotly_chart(fig3, use_container_width=True)
