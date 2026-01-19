from rag_chain import load_chain

def main():
    chain = load_chain()
    print("RAG chatbot ready. Type 'exit' to quit.")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break

        response = chain.invoke(query)
        print("\nBot:", response.content, "\n")

if __name__ == "__main__":
    main()
