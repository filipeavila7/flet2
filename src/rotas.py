# aula de rotas

import flet as ft
#import tarefa as tf

def main(page: ft.Page):
    page.title = 'Rota de fuga'

   # tarefa = tf.Tarefa()
   

    def muda_rota(route):
        page.views.clear()
        page.views.append(
                ft.View(
                    '/',
                    [
                            ft.AppBar(title = ft.Text('Aplicativo web com flet'),
                                      bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST),

                            ft.ElevatedButton('Visitar loja', on_click = lambda _: page.go('/Loja')),          
                            ft.ElevatedButton('Visitar contato', on_click = lambda _: page.go('/Contato'))          
                    ],
                )
        )
        if page.route == '/Loja':
            page.views.append(
                ft.View(
                    '/Loja',
                    [
                            ft.AppBar(title = ft.Text('Loja'),
                                      bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST),

                            ft.ElevatedButton('inicio', on_click = lambda _: page.go('/')
                                              
                                              )
                            
                    ],
                )
            )


        if page.route == '/Contato':
            page.views.append(
                ft.View(
                    '/Contato',
                    [
                            ft.AppBar(title = ft.Text('Contato'),
                                      bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST),

                            ft.ElevatedButton('inicio', on_click = lambda _: page.go('/')
                                              
                                              )
                            
                    ],
                    #tarefa
                )
            )
        page.update()

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = muda_rota
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main, view = ft.AppView.WEB_BROWSER)