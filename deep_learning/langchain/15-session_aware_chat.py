#!/usr/bin/env python3
"""
Wraps a conversational retrieval chain with session-aware message history
"""
from langchain_core import runnables


def create_session_aware_chat(retrieval_chain, get_session_history, input_key,
                              history_key, output_key,):
    """
    Wraps a conversational retrieval chain with session-aware message history.
    Args:
        retrieval_chain: Conversational retrieval chain.
        get_session_history: Function returning a BaseChatMessageHistory for a
        session.
        input_key: Key for user input.
        history_key: Key where chat history is injected.
        output_key: Key where the model output is stored.
    Returns:
        RunnableWithMessageHistory
    """
    return runnables.RunnableWithMessageHistory(
        retrieval_chain,
        get_session_history,
        input_messages_key=input_key,
        history_messages_key=history_key,
        output_messages_key=output_key,
    )
