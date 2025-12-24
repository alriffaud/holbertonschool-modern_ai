#!/usr/bin/env python3
"""Create and load a HuggingFace embedding model using LangChain."""
from langchain_huggingface import HuggingFaceEmbeddings


def create_embeddings(model_name):
    """
    Load a HuggingFace embedding model for generating vector representations
    of text documents.
    Args:
        model_name (str): Name of the HuggingFace model to use.
    Returns:
        HuggingFaceEmbeddings: An embeddings model instance.
    """
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings
