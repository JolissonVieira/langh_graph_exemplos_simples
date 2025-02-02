import uuid

from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain_openai import AzureChatOpenAI

from src.poc_lang_graph.config import API_KEY, BASE_URL
from src.poc_lang_graph.tools.custom_functions import get_functions
from src.poc_lang_graph.tools.custom_tools import get_tools

execution_id = uuid.uuid4()


def get_model():
    prompt = hub.pull("hwchase17/openai-functions-agent")

    llm = AzureChatOpenAI(
        azure_endpoint=BASE_URL,
        azure_deployment="gpt-4o",
        api_version="2024-02-15-preview",
        api_key=API_KEY,
        openai_api_type="azure",
        temperature=0,
        default_headers={
            "usuario": "",
            "desenvol": "true",
            "execution_id": str(execution_id),
        },
    )
    return create_openai_functions_agent(llm, get_tools(), prompt)


def get_model_functions():
    llm = AzureChatOpenAI(
            azure_endpoint=BASE_URL,
            azure_deployment="gpt-4o",
            api_version="2024-02-15-preview",
            api_key=API_KEY,
            openai_api_type="azure",
            temperature=0,
            default_headers={
                "usuario": "",
                "desenvol": "true",
                "execution_id": str(execution_id),
            },
        ).bind_functions(functions=get_functions())
    return llm
