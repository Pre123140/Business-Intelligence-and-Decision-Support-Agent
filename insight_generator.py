# src/insight_generator.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_revenue_by_region(df):
    if "Region" in df.columns and "Revenue" in df.columns:
        revenue_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
        fig, ax = plt.subplots()
        revenue_by_region.plot(kind="bar", ax=ax, color="teal")
        ax.set_title("Total Revenue by Region")
        ax.set_ylabel("Revenue")
        st.pyplot(fig)
    else:
        st.warning("Columns 'Revenue' or 'Region' not found.")

def plot_top_products(df):
    if "Product" in df.columns and "Units Sold" in df.columns:
        product_sales = df.groupby("Product")["Units Sold"].sum().sort_values(ascending=False)
        fig, ax = plt.subplots()
        product_sales.plot(kind="barh", ax=ax, color="skyblue")
        ax.set_title("Top Products by Units Sold")
        st.pyplot(fig)
    else:
        st.warning("Columns 'Product' or 'Units Sold' not found.")

def plot_time_series(df):
    if "Date" in df.columns and "Revenue" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        time_series = df.groupby("Date")["Revenue"].sum()
        fig, ax = plt.subplots()
        time_series.plot(ax=ax, color="purple")
        ax.set_title("Revenue Over Time")
        ax.set_ylabel("Revenue")
        st.pyplot(fig)
    else:
        st.warning("Columns 'Date' or 'Revenue' not found.")

def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include='number')
    if numeric_df.shape[1] > 1:
        corr = numeric_df.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Heatmap")
        st.pyplot(fig)
    else:
        st.warning("Not enough numeric columns for correlation heatmap.")

def plot_revenue_by_product_region(df):
    if "Region" in df.columns and "Product" in df.columns and "Revenue" in df.columns:
        grouped = df.groupby(["Region", "Product"])["Revenue"].sum().unstack()
        fig, ax = plt.subplots()
        grouped.plot(kind='bar', ax=ax)
        ax.set_title("Revenue by Product in Each Region")
        ax.set_ylabel("Revenue")
        st.pyplot(fig)
    else:
        st.warning("Required columns for grouped revenue plot not found.")

def plot_units_over_time(df):
    if "Date" in df.columns and "Units Sold" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        time_series = df.groupby("Date")["Units Sold"].sum()
        fig, ax = plt.subplots()
        time_series.plot(ax=ax, color="orange")
        ax.set_title("Units Sold Over Time")
        ax.set_ylabel("Units Sold")
        st.pyplot(fig)
    else:
        st.warning("Columns 'Date' or 'Units Sold' not found.")
