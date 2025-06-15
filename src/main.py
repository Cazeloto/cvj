import flet as ft

def main(page: ft.Page):
     page.window.always_on_top = True
     page.window.full_screen = False
     page.window.height = 400
     page.window.max_height = 400
     page.bgcolor = "#b895c4" 
     
     row1 = ft.ResponsiveRow(
            width = 300,
            height = 50,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
            ft.Image(src = "logo.jpeg"),
            ]       
     )                     
               
     row2 = ft.Row(
            width = 300,
            height = 50,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                        ft.Text(value = "Controle de Giras",
                        font_family = "Book Antiqua",
                        size = 25,
                        weight = ft.FontWeight.BOLD,
                        color = "white",
                        text_align = ft.TextAlign.CENTER
                        )
            ]              
    )                   
    
     btn1 = ft.ElevatedButton(text = "Primeiro Botao")
     page.add(row1, row2, btn1)
     page.update() 


if __name__ =='__main__':
    
    ft.app(target=main, port=9876, view=ft.AppView.WEB_BROWSER)
#ft.app(main, view = ft.WEB_BROWSER, port=8080)