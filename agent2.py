from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key="..."
)

prompt = ChatPromptTemplate.from_template("""
You are a Report Generator.

Answer ONLY using the retrieved context.

Rules:
- Do not use outside knowledge.
- Remove duplicate information.
- Organize the answer clearly.
- If the context is insufficient, say so.
- Do not mention "Based on the provided context". Answer directly.

Question:
{question}

Context:
{context}
""")

chain = prompt | llm


def generate_report(question, context):
    response = chain.invoke({
        "question": question,
        "context": context
    })
    if isinstance(response.content, str):
        return response.content

    return "\n".join(
        block["text"]
        for block in response.content
        if block.get("type") == "text"
    )