import flet as ft 


class Page2:
    def __init__(self, page: ft.Page):
        self.page = page
        page.theme_mode = ft.ThemeMode.LIGHT


    def construir(self):
        def button_clicked(e):
            t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
            self.page.update()

        t = ft.Text()
        tb1 = ft.TextField(label="Standard")
        tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
        tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
        tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
        tb5 = ft.TextField(label="With an icon", icon=ft.Icons.EMOJI_EMOTIONS)
        b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
        
        return ft.Column([
            ft.Text('Bem vindo a tela 2'),
            t, tb1, tb2, tb3, tb4, tb5, b,
            ft.ElevatedButton('Tela 1', on_click=lambda _: self.page.go('/tela1'))
            ])