#!/usr/bin/env python3
""" Create a reusable prompt template using LangChain """
from langchain import prompts


def create_prompt_template(template_str, input_variables):
    """
    Create a reusable prompt template with placeholders.
    Args:
        template_str (str): Prompt template containing placeholders.
        input_variables (list): List of variable names used in the template.
    Returns:
        PromptTemplate: An object for dynamically generating prompts.
    """
    template = prompts.PromptTemplate(
        template=template_str,
        input_variables=input_variables
    )
    return template
