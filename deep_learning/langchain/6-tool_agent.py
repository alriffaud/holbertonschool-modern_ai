#!/usr/bin/env python3
""" Load a multi-tool LangChain agent executor """
from langchain import agents
from langchain_community.agent_toolkits import load_tools


def load_agent_with_toolkit(llm, toolkit_names, prompt):
    """
    Create an agent executor capable of using multiple tools.
    Args:
        llm: A LangChain LLM instance.
        toolkit_names (list[str]): Names of toolkits to load.
        prompt: A ChatPromptTemplate instance.
    Returns:
        AgentExecutor: Configured agent executor with tool-calling capability.
    """
    tools = load_tools.load_tools(toolkit_names)

    agent = agents.create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = agents.AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )

    return agent_executor
