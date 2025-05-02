# 🧠 AI Business Intelligence & Decision Support Agent

This project is an interactive, no-code analytics tool powered by Large Language Models (LLMs), designed to help business users extract insights, generate visualizations, and ask natural language questions from their own CSV datasets — without writing code.

Built using Streamlit, LangChain, HuggingFace Embeddings, FAISS, and GPT4All (Mistral).

---

## 🚀 Features

- Upload any structured CSV dataset (sales, finance, marketing, etc.)
- View data preview, summary stats, and missing value analysis
- Generate automated insights: revenue trends, product performance, correlation heatmaps
- Ask plain English questions about your data (e.g., "Which region had the highest sales?")
- Get LLM-powered, context-aware answers with business relevance
- Auto-generate charts (bar, pie, line) based on your questions
- Download visualizations as PNG
- Works offline with local models (no cloud dependency)

---

## 📂 Folder Structure
AI_BUSINESS_INTELLIGENCE_AGENT
│
├── models/
│ └── mistral-7b-v0.1.Q4_K_M.gguf # Local LLM model
│
├── src/
│ ├── data_processor.py # CSV loading and summary
│ ├── insight_generator.py # Core visual analytics
│ ├── chart_generator.py # Auto-charting from user queries
│ ├── llm_agent.py # LLM + RAG + FAISS logic
│ └── ui.py # Streamlit-based app
│
│
├── requirements.txt # Dependencies
└── README.md # Project overview


---

## 📘 How It Works

1. User uploads a CSV file (sales report, customer data, etc.)
2. App parses the file, shows previews and summaries
3. Prebuilt charts display trends like revenue by region or product
4. User types a natural language question (e.g., “Top 2 products by sales?”)
5. The system uses FAISS + HuggingFace embeddings to retrieve relevant content
6. GPT4All (Mistral) answers based on retrieved context
7. Charts are optionally auto-generated and downloadable

---

## 🛠️ Tech Stack

- **Streamlit** – Web interface
- **pandas** – Data manipulation and analysis
- **matplotlib & seaborn** – Plotting
- **LangChain** – LLM orchestration and RAG setup
- **FAISS** – Local vector database
- **HuggingFace Embeddings** – Text embedding for vectorization
- **GPT4All / Mistral** – Local LLM (runs offline)

---

Set up a Python environment:
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt


Add Mistral GGUF model to models/ folder (download separately).


Launch the app:
streamlit run src/ui.py


💡 Example Questions
"Show revenue trends over time"

"What is the total sales by region?"

"Which product had the highest units sold?"

📚 Conceptual Study
Want to understand the logic behind vector search, RAG, or chart generation?
👉 View the full conceptual study (Link to be added when hosted)

🧭 Future Enhancements
Add memory/chat history

Support Excel uploads

Generate executive PDF reports

Integrate advanced models (GPT-4, Claude)

📄 License
MIT License.
For educational/demo purposes only. Commercial usage not permitted without written permission.


