from shiny import App, render, ui
from shiny import App, reactive, render, req, ui
from shinyswatch import theme
from parser import problemsDataFrame 


alunos_default = """Euler
Gauss
Riemann"""

problemas_default= "1, 3-6, 7[a-f]"

explain = """
Insira os problemas que deseja distribuir aleatóriamente da seguinte forma:
    
    - Números dos problemas (e.g. 1)
    
    - Intervalo dos problemas (e.g. 3-6)
    
    - Itens específicos nos problemas (e.g. 7[a-f])

De forma que uma lista da forma  1, 3-6, 7[a-f] significa

    - Problema número 1, 

    - Problemas do 3 ao 6 (isto é, 3, 4, 5 ou 6)

    - Itens **a** a **f** do problema 7.


Ao colocar os itens em linhas diferentes é sorteado um problema de cada linha.
Por exemplo, a entrada

    1, 3-6

    7[a-f]

sorteia dois problemas para cada aluno, um na primeira lista (1 ou 3 a 6) e 
um da segunda lista (itens **a** a **f** do problema 7). Se desejar mais
de um problema da mesma lista, basta repetir a lista diversas vezes (cuidado,
evitamos repetições, mas as vezes pode ser impossível se, por exemplo, 
uma lista com dois problemas for repetida 3 vezes.)

"""

app_ui = ui.page_fluid(
    ui.layout_columns(
        ui.card(
            ui.input_text_area(
                "listaProblemas",
                "Problemas:",
                problemas_default,
                height = '15vh',
                width = '100vw',
            ),
            ui.input_text_area(
                "listaAlunos",
                "Alunos:",
                alunos_default,
                height = '100vh',
                width = '100vw',
            ),
        ),
        ui.card(
            ui.input_action_button("generate", "Distribuir problemas"),
            ui.accordion(
                ui.accordion_panel("Tutorial", ui.markdown(explain)),
                open = False,
            )
        ), 
        ui.output_data_frame("problemas"),
        col_widths=[3, 6, 3]
    ), 
    theme = theme.darkly
)


def server(input, output, session):
    @render.text
    def txt():
        return f"n*2 is asd "

    @render.data_frame
    @reactive.event(input.generate)
    def problemas():
        return problemsDataFrame(
                input.listaAlunos(),
                input.listaProblemas()) 

app = App(app_ui, server)
