from langgraph.graph import END, StateGraph

from src.poc_lang_graph.model.openai_model import get_model, get_model_functions
from src.poc_lang_graph.service.service import Service
from src.poc_lang_graph.state.agent_function_state import AgentFunctionState
from src.poc_lang_graph.state.agent_tool_state import AgentToolState
from src.poc_lang_graph.tools.custom_tools import get_tools


def workflow_tools():
    service = Service(
        model=get_model(),
        tools=get_tools()
    )
    workflow = StateGraph(AgentToolState)
    workflow.add_node("agent", service.run_agent)
    workflow.add_node("action", service.execute_tools)
    workflow.set_entry_point("agent")

    workflow.add_conditional_edges(
        "agent",
        Service.should_continue_tool,
        {
            "continue": "action",
            "end": END
        }
    )

    workflow.add_edge("action", "agent")
    return workflow.compile()


def workflow_functions():
    model = get_model_functions()
    tools = get_tools()
    service = Service(
        model=model,
        tools=tools
    )
    workflow = StateGraph(AgentFunctionState)

    workflow.add_node("agent", service.call_model)
    workflow.add_node("action", service.call_tool)
    workflow.set_entry_point("agent")

    workflow.add_conditional_edges(
        "agent",
        Service.should_continue_function,
        {
            "continue": "action",
            "end": END
        }
    )

    workflow.add_edge('action', 'agent')
    return workflow.compile()
