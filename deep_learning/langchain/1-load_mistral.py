#!/usr/bin/env python3
""" Load a Mistral language model using LangChain """
import langchain_mistralai


def load_mistral(model_name, temperature):
    """
    Initialize a Mistral LLM using LangChain's ChatMistralAI.
    Args:
        model_name (str): Name of the Mistral model to load.
        temperature (float): Controls randomness in the model's output.
    Returns:
        ChatMistralAI: Configured LLM instance ready to be invoked.
    """
    llm = langchain_mistralai.ChatMistralAI(
        model=model_name,
        temperature=temperature
    )
    return llm
