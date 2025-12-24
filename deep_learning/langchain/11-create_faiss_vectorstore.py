#!/usr/bin/env python3
""" Creates a FAISS vector store and retriever using LangChain """
from langchain_community import vectorstores


def create_faiss_vectorstore(docs, embedding_model, k,
                             search_type="similarity"):
    """
    Builds a FAISS vector store from documents and returns the vector store
    along with a configured retriever.
    Args:
        docs (list): List of LangChain Document objects.
        embedding_model: LangChain embeddings model.
        k (int): Number of documents to retrieve per query.
        search_type (str): Type of search (default: "similarity").
    Returns:
        tuple: (vectorstore, retriever)
    """
    # Create FAISS vector store from documents
    vectorstore = vectorstores.FAISS.from_documents(
        docs,
        embedding_model
    )

    # Create retriever from vector store
    retriever = vectorstore.as_retriever(
        search_type=search_type,
        search_kwargs={"k": k}
    )

    return vectorstore, retriever
