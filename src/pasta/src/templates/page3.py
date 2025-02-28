import flet as ft

class Page3:
    

    def main(page: ft.Page):
        page.title = "Containers - clickable and not"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.add(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text("Non clickable"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.AMBER,
                        width=150,
                        height=150,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Text("Clickable without Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.GREEN_200,
                        width=150,
                        height=150,
                        border_radius=10,
                        on_click=lambda e: print("Clickable without Ink clicked!"),
                    ),
                    ft.Container(
                        content=ft.Text("Clickable with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.CYAN_200,
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print("Clickable with Ink clicked!"),
                    ),
                    ft.Container(
                        content=ft.Text("Clickable transparent with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
    def construir(self):
        return ft.Column([
        ft.Text('Bem vindo a tela 1'),
        ft.ElevatedButton('Tela 3', on_click=lambda _: self.page.go('/tela3')),
                
            ])
