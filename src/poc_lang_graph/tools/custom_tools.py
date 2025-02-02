from langchain.tools import tool
import random


@tool("lower_case", return_direct=True)
def to_lower_case(input:str) -> str:
    """Retorna a entrada em minúsculas"""
    return input.lower()


@tool("random_number", return_direct=True)
def random_number_maker() -> int:
    """Retorna um número entre 0 e 100, mostrando a palavra 'random'"""
    return random.randint(0, 100)


def get_tools():
    return [to_lower_case, random_number_maker]
