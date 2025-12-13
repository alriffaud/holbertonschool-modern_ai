#!/usr/bin/env python3
""" Create a reusable chat-style prompt template using LangChain """
from langchain import prompts


def create_chat_prompt_template(system_message, human_message):
    """
    Create a chat-style prompt template with separate system and human
    messages.
    Args:
        system_message (str): Instructions defining the assistant's behavior.
        human_message (str): User input template containing placeholders.
    Returns:
        ChatPromptTemplate: A prompt template for chat-based LLMs.
    """
    chat_prompt = prompts.ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            ("human", human_message)
        ]
    )
    return chat_prompt
