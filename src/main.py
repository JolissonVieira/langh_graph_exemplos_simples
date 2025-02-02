from langchain_core.messages import SystemMessage, HumanMessage

from src.poc_lang_graph.work_flow.flow import workflow_tools, workflow_functions


def executar_fluxo_com_tools():
    inputs = {"input": "gere um numero aleatório e escreva por extenso em minusculas", "chat_history": []}
    app = workflow_tools()
    for s in app.stream(inputs):
        print(list(s.values())[0])
        print("-------------------")


def executar__fluxo_com_functions():
    system_message = SystemMessage(content="você é um assistente útil")
    user_01 = HumanMessage(content="gere um número aleatório e escreva por extenso em minúsculas e liste o nomes de mulheres.")
    inputs = {"messages": [system_message, user_01]}
    app = workflow_functions()
    app.invoke(inputs)


if __name__ == "__main__":
    # executar_fluxo_com_tools()
    executar__fluxo_com_functions()

