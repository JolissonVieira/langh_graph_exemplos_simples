from typing import Annotated

from langgraph.graph import add_messages, StateGraph
from typing_extensions import TypedDict


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)
