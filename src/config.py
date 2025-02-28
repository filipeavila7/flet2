import flet as ft

def chamar(page: ft.Page):
    page.title = 'configuração'
    page.window.height = 800
    page.window.width = 800
    page.theme_mode = ft.ThemeMode.DARK
    page.window.resizable = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.center()

    def alterar_tema(e):  
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = 'Alterar o tema para escuro'  # Correção aqui
            page.bgcolor = ft.Colors.WHITE
           # t.bgcolor = ft.Colors.BLACK
           # t.color = ft.Colors.WHITE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema claro'  # Correção aqui
            page.bgcolor = ft.Colors.BLACK
           # t.bgcolor = ft.Colors.WHITE
           # t.color = ft.Colors.BLACK

        page.update()  # Atualiza a página

    # Botão para mudar o tema
    btn_tema = ft.IconButton(    
        icon=ft.icons.WB_SUNNY_OUTLINED,  # Ícone
        tooltip='Alterar o tema',  # Aparece quando passar o mouse
        on_click=alterar_tema  # Ação de clique
    )    



    

