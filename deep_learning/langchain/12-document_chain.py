#!/usr/bin/env python3
""" Create a document answer chain with chat history support """
from langchain_core import prompts
from langchain.chains import combine_documents


def document_answer_chain(llm, system_message, human_message):
    """
    Create a document-based QA chain that leverages chat history.
    Args:
        llm: Language model instance.
        system_message: Instructions for the assistant.
        human_message: User input template.
    Returns:
        A ChatPromptTemplate.
        A document chain for generating answers.
    """

    # Create chat prompt with correct message order
    prompt = prompts.ChatPromptTemplate.from_messages([
        ("system", system_message),
        prompts.MessagesPlaceholder(variable_name="chat_history"),
        ("human", human_message),
    ])

    # Create a document chain that stuffs documents into context
    document_chain = combine_documents.create_stuff_documents_chain(
        llm=llm,
        prompt=prompt
    )

    return prompt, document_chain
