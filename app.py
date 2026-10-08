import streamlit as st

st.set_page_config(
    page_title="Coffee Shop Transaction Analysis",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Coffee Shop Transaction Analysis")

pages = [
    st.Page(
        "pages/executive_dashboard.py",
        title="Executive Dashboard",
        icon="📊",
        default=True
    ),
    st.Page(
        "pages/revenue_analysis.py",
        title="Revenue Analysis",
        icon="💰"
    ),
    st.Page(
        "pages/transaction_analysis.py",
        title="Transaction Analysis",
        icon="🧾"
    ),
    st.Page(
        "pages/product_analysis.py",
        title="Product Analysis",
        icon="☕"
    ),
    st.Page(
        "pages/time_analysis.py",
        title="Time Analysis",
        icon="⏰"
    )
]

pg = st.navigation(pages, position="sidebar")

pg.run()
