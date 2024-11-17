from fasthtml.common import fast_app, serve, Titled, RedirectResponse 
from componentes import  gerar_formulario, gerar_lista_tarefas

app, routes = fast_app()

lista_tarefa = []

@routes("/") 
def homepage():
    formulario = gerar_formulario()
    elemento_lista_tarefas = gerar_lista_tarefas(lista_tarefa)
    return Titled("Lista de Tarefas", formulario, elemento_lista_tarefas)

@routes("/adicionar_tarefa", methods=["post"])
def adicionar_tarefa(tarefa: str):
    if tarefa:
        lista_tarefa.append(tarefa)
    return gerar_lista_tarefas(lista_tarefa)

@routes("/deletar/{posicao}")
def deletar(posicao: int):
    if len(lista_tarefa) > posicao:
        lista_tarefa.pop(posicao)
    return gerar_lista_tarefas(lista_tarefa)



       
serve()
