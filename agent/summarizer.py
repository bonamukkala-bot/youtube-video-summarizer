from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama

def summarize_text(text):

    llm = Ollama(
        model="gemma:2b",
        temperature=0
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )

    docs = splitter.split_text(text)

    summaries = []

    for chunk in docs:
        prompt = f"""
        Summarize this YouTube transcript clearly and concisely:

        {chunk}
        """
        response = llm.invoke(prompt)
        summaries.append(response)

    final_summary = "\n".join(summaries)

    return final_summary