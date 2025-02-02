import operator
from typing import Union, Annotated, TypedDict

from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.messages import BaseMessage


class AgentToolState(TypedDict):
    input: str
    chat_history: list[BaseMessage]
    agent_outcome: Union[AgentAction, AgentFinish, None]
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]
