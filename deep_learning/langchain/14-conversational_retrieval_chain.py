#!/usr/bin/env python3
""" Create a conversational retrieval chain using LangChain """
from langchain import chains


def create_conversational_retrieval_chain(history_aware_retriever,
                                          document_chain):
    """
    Builds a conversational retrieval chain that retrieves documents using
    conversation-aware queries and generates answers from those documents.
    Args:
        history_aware_retriever: A retriever that leverages chat history.
        document_chain: A chain that generates answers from retrieved
        documents.
    Returns:
        A retrieval chain ready to handle conversational queries.
    """
    return chains.create_retrieval_chain(
        history_aware_retriever,
        document_chain
    )
