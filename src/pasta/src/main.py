import flet as ft
from templates.page1 import Page1
from templates.page2 import Page2
from templates.page3 import Page3

def main(page: ft.Page):
    page.title = 'meu app de paginas'
    page.window.width = 500  
    page.window.height = 500

    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )

    def rotas(route):
        page.controls.clear()
        if route == '/':
            tela = Page1(page)
        elif route == '/tela2':
            tela = Page2(page)
        elif route == '/tela3':
            tela = Page3(page)
        
        else:
            tela = Page1(page)


        page.add(tela.construir())



    page.on_route_change = lambda e: rotas(e.route)
    page.go('/')
    

ft.app(main)
