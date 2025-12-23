#!/usr/bin/env python3
"""Load documents from a folder using LangChain document loaders."""
from langchain_community import document_loaders


def load_documents(folder_path, file_pattern):
    """
    Load documents from a folder using a glob pattern.
    Args:
        folder_path (str): Path to the folder containing documents.
        file_pattern (str): Glob pattern to match files (e.g., '**/*.md').
    Returns:
        list: A list of LangChain Document objects.
    """
    loader = document_loaders.DirectoryLoader(
        path=folder_path,
        glob=file_pattern,
        loader_cls=document_loaders.TextLoader,
        silent_errors=True,
        show_progress=False
    )

    documents = loader.load()
    return documents
