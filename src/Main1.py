import flet as ft


def main(page: ft.Page):
        page.window.always_on_top = True
        page.bgcolor = ft.Colors.TRANSPARENT
        page.title = "Flet App"
        page.window.title_bar_hidden = False
        page.window.frameless = False
        page.window.bgcolor = ft.Colors.TRANSPARENT

        page.update()

if __name__ =='__main__':
    ft.app(target   =   main)