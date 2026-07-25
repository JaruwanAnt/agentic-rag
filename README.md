# Agentic AI Programming Test

## Overview

This project implements a simple **two-agent Retrieval-Augmented Generation (RAG)** system using **LangChain** and **Google Gemini**.

The system consists of:

* **Agent 1 – Data Retriever**

  * Searches a local knowledge base (`knowledge_base.txt`)
  * Retrieves the most relevant information using keyword matching

* **Agent 2 – Report Generator**

  * Receives the retrieved context from Agent 1
  * Uses Google Gemini to generate a final answer based only on the retrieved information

---

## Project Structure

```text
agentic-rag/
│
├── knowledge_base.txt      # Knowledge base
├── retrieve.py             # Agent 1 (Retriever)
├── agent2.py               # Agent 2 (Report Generator)
├── test.py                 # Main program
├── requirements.txt
├── README.md
└── .env                    # Google API Key
```

---

## Architecture

```
User Question
      │
      ▼
Agent 1: Data Retriever
      │
      ▼
Retrieved Context
      │
      ▼
Agent 2: Report Generator (Gemini)
      │
      ▼
Final Answer
```

---

## Technologies

* Python 3
* LangChain
* Google Gemini API
* python-dotenv

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GOOGLE_API_KEY=your_api_key_here
```

---

## Run

```bash
python test.py
```

---

## Example Questions

* What is the policy on international travel?
* Is travel insurance required?
* When should employees submit expense reports?
* What is the work from home policy?

---

## Retrieval Method

The Retriever Agent performs a simple keyword-based search over the local knowledge base.

The process is:

1. Split the knowledge base into paragraphs.
2. Remove common stop words from the user query.
3. Score each paragraph by keyword overlap.
4. Return the highest-scoring paragraphs.
5. If no relevant paragraph is found, the Report Generator returns that the information is insufficient.

---

## Example Output

```
Question:
What is the policy on international travel?

[Agent 1] Data Retriever
Found 1 relevant snippet.

[Agent 2] Report Generator

Final Answer:
Employees traveling internationally must obtain manager approval at least two weeks before departure. The company covers airfare, hotel, and daily allowances according to the travel policy.
```

---

## Notes

* This project demonstrates a simple multi-agent RAG workflow.
* Agent 1 is responsible for retrieval only.
* Agent 2 generates responses using the retrieved context.
* If the knowledge base does not contain sufficient information, the system explicitly reports that instead of generating unsupported answers.
