# 🧠 AI-Powered Business Intelligence & Decision Support Agent

An interactive AI agent that helps users **analyze uploaded business data, generate insights, visualize trends, and support real-time decisions** — powered by `Mistral-7B`, LangChain, RAG (Retrieval Augmented Generation), and Streamlit. Users can upload CSVs and get instant responses from an LLM-powered chatbot trained on their data.

---

## 🎯 Project Objective
To create a dataset-agnostic GenAI agent that:
- Understands business data dynamically upon upload
- Provides summary insights, trends, and patterns
- Answers real-time queries using RAG and LLMs
- Generates visual charts and downloadable reports

---

## 🚀 Key Features
- **LLM-Powered Chatbot** – Interact directly with your uploaded CSV
- **Insight Generator** – Get trends, summaries, stats in plain English
- **Dynamic Charts** – Auto-generate visuals like bar, line, and pie charts
- **Download Options** – Export PNG charts or PDF reports
- **RAG Pipeline** – Combine FAISS + LangChain for accurate answers
- **100% Local Execution** – No OpenAI API needed (Mistral-7B offline)

---

## 🧠 Conceptual Study
Want to explore how GenAI augments BI?
👉 [Read the Full Conceptual Study →](https://github.com/Pre123140/Business-Intelligence-and-Decision-Support-Agent/blob/main/BUSINESS%20INTELLIGENCE%20AND%20DECISION%20SUPPORT%20AGENT%20(1).pdf)

---

## 🛠️ Tech Stack
- `mistral-7b-openorca.Q4_K_M.gguf` via GPT4All
- `LangChain` (Agents + FAISS)
- `Streamlit` for the frontend UI
- `Pandas`, `Matplotlib`, `Plotly` for charting
- `fpdf` and `PIL` for PDF/PNG export

---

## 📁 Folder Structure
```
bi_decision_support_agent/
├── data/                        # Uploaded CSVs
├── models/                     # LLM models (Mistral-7B GGUF)
├── src/
│   ├── ui.py                   # Streamlit UI for file upload and user input
│   ├── data_processor.py       # Preprocessing of uploaded data
│   ├── insight_generator.py    # Stats, summaries, key KPIs
│   ├── chart_generator.py      # Dynamic visualizations
│   ├── llm_agent.py            # RAG + LLM querying agent
│   └── utils.py                # Helper functions for formatting, paths
└── requirements.txt
```

---

## ⚙️ How to Run the Project

### 1. 📂 Clone the Repository
```bash
git clone https://github.com/yourname/bi_decision_support_agent
cd bi_decision_support_agent
```

### 2. ✨ Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. ⚖️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🤖 Add Your LLM Model
Place `mistral-7b-openorca.Q4_K_M.gguf` in the `/models/` directory.

### 5. 🚀 Run the App
```bash
streamlit run src/ui.py
```

Then upload any `.csv` file and start chatting or exploring!

---

---

## ✨ Project Highlights
- **No Fixed Schema**: Works with any CSV, auto-detects columns
- **Business-Ready**: Summarizes sales, profits, trends, and more
- **Chat + Visuals**: Both conversational and chart-based output
- **Offline-First**: Ideal for internal orgs with sensitive data

---

## 📜 License

This project is open for educational use only. For commercial deployment, contact the author.

---

## 📬 Contact
If you'd like to learn more or collaborate on projects or other initiatives, feel free to connect on [LinkedIn](https://www.linkedin.com/in/prerna-burande-99678a1bb/) or check out my [portfolio site](https://youtheleader.com/).

