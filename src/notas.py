import flet as ft
import config

# Classe Nota para representar cada aluno e suas notas
class Nota(ft.Row):
    def __init__(self, aluno, notas):
        super().__init__()
        self.checkbox = ft.Checkbox()
        self.nome_aluno_view = ft.Text(aluno)
        
        # Exibe todas as notas
        self.notas_view = ft.Text(f"{notas[0]} | {notas[1]} | {notas[2]}")
        self.notas_editar = ft.TextField(value=f"{notas[0]} | {notas[1]} | {notas[2]}", visible=False)
        
        # Calcula a média das notas
        media = (notas[0] + notas[1] + notas[2]) / 3
        self.media_view = ft.Text(f'Média: {media:.2f}')
        self.status_view = ft.Text("Aprovado" if media >= 7 else "Reprovado", color="green" if media >= 7 else "red")
        
        self.btn_editar = ft.IconButton(icon=ft.Icons.EDIT, on_click=self.editar)
        self.btn_salvar = ft.IconButton(visible=False, icon=ft.icons.SAVE_OUTLINED, on_click=self.salvar)

        self.controls = [
            self.checkbox,
            self.nome_aluno_view,
            self.notas_view,
            self.media_view,
            self.status_view,
            self.notas_editar,
            self.btn_editar,
            self.btn_salvar
        ]

    # Função para editar as notas do aluno
    def editar(self, e):
        self.btn_editar.visible = False
        self.btn_salvar.visible = True
        self.notas_view.visible = False
        self.notas_editar.visible = True
        self.update()

    # Função para salvar as novas notas do aluno
    def salvar(self, e):
        self.btn_editar.visible = True
        self.btn_salvar.visible = False
        self.notas_view.visible = True
        self.notas_editar.visible = False
        self.notas_view.value = self.notas_editar.value

        # Atualiza as notas e o status
        notas_str = self.notas_editar.value.split(" | ")
        notas = [float(nota) for nota in notas_str]
        
        # Calcula nova média e atualiza status
        media = sum(notas) / len(notas)
        self.media_view.value = f'Média: {media:.2f}'
        self.status_view.value = "Aprovado" if media >= 7 else "Reprovado"
        self.status_view.color = "green" if media >= 7 else "red"
        self.update()

def main(page: ft.Page):
    config.chamar(page)
    page.title = "Gerenciador de Notas"
    page.theme_mode = ft.ThemeMode.LIGHT

    lista_notas = []  # Lista para armazenar as notas dos alunos

    def adicionar_nota(e):
        if nome_aluno_field.value.strip() and nota_field_1.value.strip() and nota_field_2.value.strip() and nota_field_3.value.strip():
            # Adiciona as 3 notas do aluno
            notas = [
                float(nota_field_1.value),
                float(nota_field_2.value),
                float(nota_field_3.value)
            ]
            novo_aluno = Nota(aluno=nome_aluno_field.value, notas=notas)
            lista_notas.append(novo_aluno)
            lista_notas_view.controls.append(novo_aluno)

            # Limpa os campos
            nome_aluno_field.value = ""
            nota_field_1.value = ""
            nota_field_2.value = ""
            nota_field_3.value = ""

            page.update()

    # Remover notas selecionadas
    def remover_notas(e):
        for nota in lista_notas[:]:
            if nota.checkbox.value:
                lista_notas_view.controls.remove(nota)
                lista_notas.remove(nota)
        page.update()

    nome_aluno_field = ft.TextField(label='Nome do Aluno')
    
    # Três campos para inserir as notas
    nota_field_1 = ft.TextField(label='Nota 1')
    nota_field_2 = ft.TextField(label='Nota 2')
    nota_field_3 = ft.TextField(label='Nota 3')
    
    mensagem_erro = ft.Text(value="", color="red", size=14)

    # Botões para adicionar e remover notas
    btn_adicionar_nota = ft.ElevatedButton('Adicionar Nota', on_click=adicionar_nota)
    btn_remover_nota = ft.ElevatedButton('Excluir Notas Selecionadas', on_click=remover_notas)
    
    lista_notas_view = ft.Column()

    # Função para alterar o tema
    def alterar_tema(e):  
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = 'Alterar o tema para escuro'  # Correção aqui
            page.bgcolor = ft.Colors.WHITE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema claro'  # Correção aqui
            page.bgcolor = ft.Colors.BLACK

        page.update()  # Atualiza a página

    # Botão para mudar o tema
    btn_tema = ft.IconButton(    
        icon=ft.icons.WB_SUNNY_OUTLINED,  # Ícone
        tooltip='Alterar o tema',  # Aparece quando passar o mouse
        on_click=alterar_tema  # Ação de clique
    )    

    # Layout da interface
    page.add(
        ft.Column([ 
            nome_aluno_field,
            nota_field_1,
            nota_field_2,
            nota_field_3,
            btn_adicionar_nota, 
            btn_tema  # Botão para alterar tema adicionado aqui
        ]),
        mensagem_erro,
        btn_remover_nota,
        lista_notas_view
    )

# Inicia o aplicativo
ft.app(target=main)
