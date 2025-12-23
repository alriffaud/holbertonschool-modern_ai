#!/usr/bin/env python3
""" Split documents into chunks using LangChain """
from langchain import text_splitter


def split_into_chunks(docs, chunk_size, chunk_overlap):
    """
    Split a list of LangChain Document objects into smaller chunks.
    Args:
        docs (list): List of LangChain Document objects.
        chunk_size (int): Maximum number of characters per chunk.
        chunk_overlap (int): Number of overlapping characters between chunks.
    Returns:
        list: List of LangChain Document objects representing chunks.
    """
    splitter = text_splitter.RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    split_docs = splitter.split_documents(docs)
    return split_docs
