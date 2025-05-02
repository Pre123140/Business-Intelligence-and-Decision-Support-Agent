# src/ui.py (Custom Guided UI for Business Intelligence Agent)

import streamlit as st
import pandas as pd
from data_processor import load_data, summarize_data
from insight_generator import (
    plot_revenue_by_region,
    plot_top_products,
    plot_time_series,
    plot_correlation_heatmap,
    plot_revenue_by_product_region,
    plot_units_over_time
)
from llm_agent import load_llm, df_to_documents, create_vectorstore, ask_question
from chart_generator import plot_chart_from_question

st.set_page_config(page_title="AI BI Agent", layout="wide")
st.title("📊 AI Business Intelligence & Decision Support Agent")

# === Session State ===
if "df" not in st.session_state:
    st.session_state.df = None

# === Tabs ===
tabs = st.tabs(["📁 Upload & Overview", "📊 Auto Visual Insights", "💬 Ask AI Questions", "📈 Chart Generator", "📘 How to Use"])

# === Tab 1: Upload & Overview ===
with tabs[0]:
    st.header("Upload Your Business Dataset")
    st.markdown("You can upload any CSV file with business metrics (e.g., Sales, Revenue, Units, Product, Date, Region).")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        df = load_data(uploaded_file)
        if df is not None:
            st.session_state.df = df
            st.success("✅ File loaded successfully")

            st.subheader("📋 Data Preview")
            st.dataframe(df.head())

            st.subheader("📌 Dataset Summary")
            st.dataframe(summarize_data(df))
        else:
            st.error("❌ Failed to read data. Try another file.")

# === Tab 2: Auto Visual Insights ===
with tabs[1]:
    st.header("📊 Automated Visual Analysis")
    if st.session_state.df is not None:
        df = st.session_state.df
        plot_revenue_by_region(df)
        plot_top_products(df)
        plot_time_series(df)
        plot_correlation_heatmap(df)
        plot_revenue_by_product_region(df)
        plot_units_over_time(df)
    else:
        st.warning("⚠️ Please upload a dataset first from the Upload tab.")

# === Tab 3: Ask Questions ===
with tabs[2]:
    st.header("💬 Ask AI-Powered Business Questions")
    st.markdown("Ask in natural language, e.g.:")
    st.code("What is the total revenue by region?\nWhich product sold the most in January?")

    if st.session_state.df is not None:
        query = st.text_input("Enter your question:")
        if query:
            with st.spinner("Generating answer..."):
                llm = load_llm()
                docs = df_to_documents(st.session_state.df)
                vs = create_vectorstore(docs)
                answer = ask_question(llm, vs, query, st.session_state.df)
                st.success("Answer:")
                st.write(answer)
    else:
        st.warning("⚠️ Upload data first from the Upload tab.")

# === Tab 4: Chart Generator ===
with tabs[3]:
    st.header("📈 Generate Visual Chart from Query")
    st.markdown("Ask for a chart like:")
    st.code("Line chart of revenue by region\nPie chart of product distribution")

    if st.session_state.df is not None:
        chart_query = st.text_input("Describe the chart you want to generate")
        if chart_query:
            plot_chart_from_question(st.session_state.df, chart_query)
    else:
        st.warning("⚠️ Please upload your CSV first.")

# === Tab 5: How to Use ===
with tabs[4]:
    st.header("📘 Guide to Using the BI Agent")
    st.markdown("""
    **Step 1**: Go to the **Upload & Overview** tab and upload your business dataset (CSV only).

    **Step 2**: Explore key stats and a summary of your data.

    **Step 3**: Navigate to **Auto Visual Insights** to view charts like revenue trends, top products, etc.

    **Step 4**: In the **Ask AI Questions** tab, type your business question to get natural language insights.

    **Step 5**: Use the **Chart Generator** to describe a chart (e.g., "bar chart of top products by revenue").

    This app supports real-time, local processing of any structured CSV — with or without specific column names like Product, Region, Revenue, Units, etc.
    """)
