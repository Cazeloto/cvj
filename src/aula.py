import flet as ft
def main(page: ft.Page):
  mensagem = ft.Text(value="Olá Mundo")
  page.add(mensagem)

  page.bgcolor = "green"
  page.bgcolor = '#B12B12'
  page.bgcolor = ft.Colors.YELLOW_900
  
  page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
  page.vertical_alignment = ft.MainAxisAlignment.START
  #page.padding = ft.padding.symmetric(vertical=100, horizontal=30)
  #page.padding = ft.padding.only(left=10, top=20, right=100, bottom=50)
  #page.padding = ft.padding.all(200)
  page.spacing = 10
  page.title = "Primeira serioApp"


  page.add(
    ft.Text(value = "Olá Mundo"),
    ft.Container(ft.Text(value = "Olá Mundo"), bgcolor = "black")
    )
  page.update()


ft.app(target = main, view=ft.WEB_BROWSER)  







#class App: 
#    def __init__(self,page: ft.Page):
#        
#        pass
#        
#ft.app(target=App) 
  