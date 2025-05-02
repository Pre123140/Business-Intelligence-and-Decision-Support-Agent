# src/chart_generator.py

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import io

def plot_chart_from_question(df, query):
    query_lower = query.lower()

    # Ensure 'Date' column is in datetime format
    if "Date" in df.columns and not pd.api.types.is_datetime64_any_dtype(df["Date"]):
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

    # Helper: Check column presence
    def has_cols(*cols):
        return all(col in df.columns for col in cols)

    # Chart type inference
    if "line" in query_lower:
        chart_type = "line"
    elif "pie" in query_lower:
        chart_type = "pie"
    else:
        chart_type = "bar"

    # Mapping rules
    if has_cols("Region", "Revenue") and "revenue" in query_lower and "region" in query_lower:
        result = df.groupby("Region")["Revenue"].sum()
        _plot_and_download(result, chart_type, "Revenue by Region", x_label="Region")

    elif has_cols("Product") and "product distribution" in query_lower:
        result = df["Product"].value_counts()
        _plot_and_download(result, chart_type, "Product Distribution", x_label="Product")

    elif has_cols("Product", "Units Sold") and "units sold" in query_lower and "product" in query_lower:
        result = df.groupby("Product")["Units Sold"].sum()
        _plot_and_download(result, chart_type, "Units Sold by Product", x_label="Product")

    elif has_cols("Date", "Revenue") and "revenue over time" in query_lower:
        df_sorted = df.sort_values("Date")
        result = df_sorted.groupby("Date")["Revenue"].sum()
        _plot_and_download(result, chart_type, "Revenue Over Time", x_label="Date")

    elif has_cols("Date", "Units Sold") and "units sold over time" in query_lower:
        df_sorted = df.sort_values("Date")
        result = df_sorted.groupby("Date")["Units Sold"].sum()
        _plot_and_download(result, chart_type, "Units Sold Over Time", x_label="Date")

    else:
        st.info("⚠️ No matching chart logic found for this query or required columns missing.")


def _plot_and_download(series, chart_type, title, x_label=""):
    fig, ax = plt.subplots()

    if chart_type == "bar":
        series.plot(kind="bar", ax=ax, color="green")
    elif chart_type == "line":
        series.plot(kind="line", ax=ax, marker='o', color="blue")
    elif chart_type == "pie":
        ax.pie(series, labels=series.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title(title)
        st.pyplot(fig)
        _add_download_button(fig, "chart.png")
        return

    ax.set_title(title)
    ax.set_ylabel(series.name if series.name else "")
    if x_label:
        ax.set_xlabel(x_label)

    st.pyplot(fig)
    _add_download_button(fig, "chart.png")


def _add_download_button(fig, filename):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    st.download_button(
        label="Download Chart as PNG",
        data=buf,
        file_name=filename,
        mime="image/png"
    )
