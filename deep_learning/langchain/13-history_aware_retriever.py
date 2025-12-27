#!/usr/bin/env python3
"""Build a history-aware retriever using LangChain"""
from langchain_core import prompts
from langchain import chains


def build_history_aware_retriever(llm, retriever, human_message):
    """
    Build a history-aware retriever that reformulates the search query
    using conversation history before performing retrieval.
    Args:
        llm: Language model used to generate the search query.
        retriever: A LangChain retriever (e.g., FAISS retriever).
        human_message: Template string for the human input.
    Returns:
        ChatPromptTemplate: Prompt used to generate the search query.
        Runnable: A history-aware retriever.
    """

    # Prompt: chat_history -> human input
    prompt_search_query = prompts.ChatPromptTemplate.from_messages([
        prompts.MessagesPlaceholder(variable_name="chat_history"),
        prompts.HumanMessagePromptTemplate.from_template(human_message),
    ])

    # Create history-aware retriever
    history_aware_retriever = chains.create_history_aware_retriever(
        llm,
        retriever,
        prompt_search_query
    )

    return prompt_search_query, history_aware_retriever
