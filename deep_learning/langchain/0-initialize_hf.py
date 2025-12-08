#!/usr/bin/env python3
""" Initialize a Hugging Face text-to-text LLM using LangChain """
from langchain_community import llms


def initialize_hf_llm(model_name, max_tokens):
    """
    Initialize a Hugging Face text-to-text generation LLM using LangChain's
    HuggingFacePipeline.
    Args:
        model_name (str): Name of the Hugging Face model to load.
        max_tokens (int): Maximum number of tokens to generate.
    Returns:
        HuggingFacePipeline: Configured LLM instance ready for invocation.
    """
    llm = llms.HuggingFacePipeline.from_model_id(
        model_id=model_name,
        task="text2text-generation",
        pipeline_kwargs={"max_new_tokens": max_tokens}
    )
    return llm
