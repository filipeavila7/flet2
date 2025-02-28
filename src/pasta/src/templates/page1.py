import flet as ft 


class Page1:
    def __init__(self, page: ft.Page):
        self.page = page
        page.theme_mode = ft.ThemeMode.DARK


    def construir(self):
        return ft.Column([
        ft.Text('Bem vindo a tela 1'),
        ft.ElevatedButton('Tela 2', on_click=lambda _: self.page.go('/tela2')),
                
            ])