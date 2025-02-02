from langchain_core.utils.function_calling import convert_to_openai_function

from src.poc_lang_graph.tools.custom_tools import get_tools


def get_functions():
    return [convert_to_openai_function(t) for t in get_tools()]
