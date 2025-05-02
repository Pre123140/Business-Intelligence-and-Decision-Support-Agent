# src/llm_agent.py

from langchain.llms import GPT4All
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

import pandas as pd
import os

MODEL_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "models", "mistral-7b-v0.1.Q4_K_M.gguf")
)

# Load local LLM
def load_llm():
    return GPT4All(model=MODEL_PATH, backend='llama', verbose=True)

# Convert dataframe to document format
def df_to_documents(df):
    text = df.to_csv(index=False)
    return [Document(page_content=text)]

# Create vectorstore from dataframe
def create_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore

# Ask LLM with context
def ask_question(llm, vectorstore, query, df):
    docs = vectorstore.similarity_search(query)
    query_lower = query.lower()

    # Safe datetime conversion
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

    # 1. Total revenue by region
    if "total revenue by region" in query_lower and "Region" in df.columns and "Revenue" in df.columns:
        result = df.groupby("Region")["Revenue"].sum()
        return result.to_string()

    # 2. Top 2 regions by sales
    elif "top 2 regions" in query_lower and "sales" in query_lower and "Region" in df.columns and "Revenue" in df.columns:
        result = df.groupby("Region")["Revenue"].sum().nlargest(2)
        return result.to_string()

    # 3. Product with highest total units sold
    elif "highest total units sold" in query_lower and "Product" in df.columns and "Units Sold" in df.columns:
        result = df.groupby("Product")["Units Sold"].sum()
        top_product = result.idxmax()
        return f"{top_product} has the highest total units sold:\n{result.to_string()}"

    # 4. Average unit price of Widget A in North
    elif "average unit price of widget a" in query_lower and "north" in query_lower and all(col in df.columns for col in ["Product", "Region", "Unit Price"]):
        filtered = df[(df["Product"] == "Widget A") & (df["Region"] == "North")]
        avg_price = filtered["Unit Price"].mean()
        return f"Average unit price of Widget A in North: {avg_price:.2f}"

    # 5. Units of Widget A sold in East
    elif all(sub in query_lower for sub in ["widget a", "east", "units"]) and all(col in df.columns for col in ["Product", "Region", "Units Sold"]):
        filtered = df[(df["Product"] == "Widget A") & (df["Region"] == "East")]
        total_units = filtered["Units Sold"].sum()
        return f"Units of Widget A sold in East: {total_units}"

    # 6. Region with highest Widget C sales
    elif all(sub in query_lower for sub in ["widget c", "region", "highest"]) and all(col in df.columns for col in ["Product", "Region", "Units Sold"]):
        filtered = df[df["Product"] == "Widget C"]
        result = filtered.groupby("Region")["Units Sold"].sum()
        top_region = result.idxmax()
        return f"{top_region} had the highest Widget C sales:\n{result.to_string()}"

    # 7. Total revenue for Widget B in January
    elif all(sub in query_lower for sub in ["widget b", "total revenue", "january"]) and all(col in df.columns for col in ["Product", "Date", "Revenue"]):
        filtered = df[(df["Product"] == "Widget B") & (df["Date"].dt.month == 1)]
        total = filtered["Revenue"].sum()
        return f"Total revenue for Widget B in January: {total}"

    # 8. Total revenue in January
    elif "total revenue" in query_lower and "january" in query_lower and "Date" in df.columns and "Revenue" in df.columns:
        jan_data = df[df["Date"].dt.month == 1]
        total = jan_data["Revenue"].sum()
        return f"Total revenue for all products in January: {total}"

    # 9. Region that sold most Widget A units
    elif all(sub in query_lower for sub in ["widget a", "region", "sold the most"]) and all(col in df.columns for col in ["Product", "Region", "Units Sold"]):
        filtered = df[df["Product"] == "Widget A"]
        result = filtered.groupby("Region")["Units Sold"].sum()
        top_region = result.idxmax()
        return f"{top_region} sold the most Widget A units:\n{result.to_string()}"

    # 10. Highest average unit price for Widget B in January
    elif all(sub in query_lower for sub in ["widget b", "average unit price", "january"]) and all(col in df.columns for col in ["Product", "Region", "Unit Price", "Date"]):
        filtered = df[(df["Product"] == "Widget B") & (df["Date"].dt.month == 1)]
        result = filtered.groupby("Region")["Unit Price"].mean()
        top_region = result.idxmax()
        return f"{top_region} had the highest average unit price for Widget B:\n{result.to_string()}"

    # Fallback
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain.run(input_documents=docs, question=query)
