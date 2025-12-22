#!/usr/bin/env python3
""" Create a Pandas DataFrame Agent using LangChain """
from langchain_experimental.agents.agent_toolkits \
    import create_pandas_dataframe_agent


def create_dataframe_agent(llm, df):
    """
    Create a Pandas DataFrame Agent capable of answering questions
    about a pandas DataFrame using a LangChain LLM.
    The agent is configured to:
    - Allow execution of Python code on the DataFrame
    - Display detailed reasoning steps
    - Handle parsing errors gracefully
    Args:
        llm: A LangChain LLM instance.
        df: A pandas DataFrame to be queried by the agent.
    Returns:
        AgentExecutor: A configured Pandas DataFrame agent.
    """
    agent = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        allow_dangerous_code=True,
        verbose=True,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )

    return agent
