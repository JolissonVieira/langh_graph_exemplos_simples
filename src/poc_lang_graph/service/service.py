import json

from langchain_core.agents import AgentFinish
from langchain_core.messages import FunctionMessage
from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import ToolExecutor, ToolInvocation


class Service:

    def __init__(self, model: AzureChatOpenAI, tools):
        self.model = model
        self.tools = tools

    def run_agent(self, data):
        agent_runnable = self.model
        agent_outcome = agent_runnable.invoke(data)
        return {"agent_outcome": agent_outcome}

    def execute_tools(self, data):
        tool_executor = ToolExecutor(self.tools)
        agent_action = data["agent_outcome"]
        output = tool_executor.invoke(agent_action)
        print(f"The agent action is: {agent_action}")
        print(f"The tool result is: {output}")
        return {"intermediate_steps": [(agent_action, str(output))]}

    def call_model(self, state):
        messages = state['messages']
        response = self.model.invoke(messages)
        return {"messages": [response]}

    def call_tool(self, state):
        tool_executor = ToolExecutor(self.tools)
        messages = state['messages']
        last_message = messages[-1]
        action = ToolInvocation(
            tool=last_message.additional_kwargs["function_call"]["name"],
            tool_input=json.loads(last_message.additional_kwargs["function_call"]["arguments"]),
        )
        print(f"The agent action is {action}")

        response = tool_executor.invoke(action)
        print(f"The tool result is: {response}")

        function_message = FunctionMessage(content=str(response), name=action.tool)
        return {"messages": [function_message]}

    @staticmethod
    def should_continue_tool(data):
        if isinstance(data["agent_outcome"], AgentFinish):
            return "end"
        else:
            return "continue"

    @staticmethod
    def should_continue_function(state):
        messages = state['messages']
        last_message = messages[-1]
        if "function_call" not in last_message.additional_kwargs:
            return "end"
        else:
            return "continue"
