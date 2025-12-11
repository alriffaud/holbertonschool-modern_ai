#!/usr/bin/env python3
""" Build a message sequence for LangChain LLMs """
from langchain_core import messages


def setup_message_sequence(system_msg, human_msgs):
    """
    Prepare a sequence of system and human messages for an LLM.
    Args:
        system_msg (str): The system instruction defining model behavior.
        human_msgs (list[str]): A list of human message strings.
    Returns:
        list: A list containing a SystemMessage followed by HumanMessage
        objects.
    """
    message = [messages.SystemMessage(content=system_msg)]

    for msg in human_msgs:
        message.append(messages.HumanMessage(content=msg))

    return message
