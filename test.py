from retrieve import retrieve
from agent2 import generate_report

queries = [
    "What is the policy on international travel?",
    "Is travel insurance required?",
    "When should employees submit expense reports?",
    "What is the work from home policy?"
]

for question in queries:

    print("=" * 60)
    print("Question:", question)

    snippets = retrieve(question) #agent 1

    print("\n[Agent 1] Data Retriever")

    if snippets:
        print(f"Found {len(snippets)} relevant snippet(s).")

        for i, snippet in enumerate(snippets, start=1):
            print(f"\nSnippet {i}:")
            print(snippet)

        context = "\n\n".join(snippets)

    else:
        print("No relevant information found.")
        context = ""

    print("\n[Agent 2] Report Generator")

    answer = generate_report(question, context) #agent 2

    print("\nFinal Answer:")
    print(answer)