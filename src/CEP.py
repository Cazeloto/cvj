import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Consulta de CEP - ViaCEP"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 550

    # Campos de entrada e saída
    cep_input = ft.TextField(
        label="Digite o CEP (apenas números)",
        hint_text="Ex: 01001000",
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
        max_length=8,
        width=250,
        text_align=ft.TextAlign.CENTER,
    )

    logradouro_output = ft.Text(value="Logradouro: ", size=16)
    bairro_output = ft.Text(value="Bairro: ", size=16)
    localidade_output = ft.Text(value="Localidade: ", size=16)
    uf_output = ft.Text(value="UF: ", size=16)
    ibge_output = ft.Text(value="IBGE: ", size=16)
    ddd_output = ft.Text(value="DDD: ", size=16)

    # Função para consultar o CEP
    def consultar_cep(e):
        cep = cep_input.value
        if not cep or len(cep) != 8:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, digite um CEP válido com 8 dígitos.", color=ft.colors.WHITE),
                bgcolor=ft.Colors.RED_500,
                open=True,
            )
            page.update()
            return

        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url)
            data = response.json()

            if "erro" in data:
                page.snack_bar = ft.SnackBar(
                    ft.Text("CEP não encontrado.", color=ft.colors.WHITE),
                    bgcolor=ft.colors.ORANGE_500,
                    open=True,
                )
                limpar_campos()
            else:
                logradouro_output.value = f"Logradouro: {data.get('logradouro', 'N/A')}"
                bairro_output.value = f"Bairro: {data.get('bairro', 'N/A')}"
                localidade_output.value = f"Localidade: {data.get('localidade', 'N/A')}"
                uf_output.value = f"UF: {data.get('uf', 'N/A')}"
                ibge_output.value = f"IBGE: {data.get('ibge', 'N/A')}"
                ddd_output.value = f"DDD: {data.get('ddd', 'N/A')}"
                page.snack_bar = ft.SnackBar(
                    ft.Text("CEP consultado com sucesso!", color=ft.colors.WHITE),
                    bgcolor=ft.colors.GREEN_500,
                    open=True,
                )

        except requests.exceptions.ConnectionError:
            page.snack_bar = ft.SnackBar(
                ft.Text("Erro de conexão. Verifique sua internet.", color=ft.colors.WHITE),
                bgcolor=ft.colors.RED_500,
                open=True,
            )
            limpar_campos()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Ocorreu um erro: {ex}", color=ft.colors.WHITE),
                bgcolor=ft.colors.RED_500,
                open=True,
            )
            limpar_campos()
        finally:
            page.update()

    # Função para limpar os campos de saída
    def limpar_campos():
        logradouro_output.value = "Logradouro: "
        bairro_output.value = "Bairro: "
        localidade_output.value = "Localidade: "
        uf_output.value = "UF: "
        ibge_output.value = "IBGE: "
        ddd_output.value = "DDD: "
        page.update()

    # Botão de consulta
    consultar_button = ft.ElevatedButton(
        text="Consultar CEP",
        on_click=consultar_cep,
        icon=ft.Icons.SEARCH,
        width=250,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor={
                #ft.MaterialState.HOVERED: ft.colors.BLUE_700,
                #ft.MaterialState.DEFAULT: ft.colors.BLUE_500,
                
            },
            color=ft.Colors.WHITE
        )
    )

    # Layout da página
    page.add(
        ft.Column(
            [
                ft.Text("Consultar CEP", size=30, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                cep_input,
                consultar_button,
                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                ft.Container(
                    content=ft.Column(
                        [
                            logradouro_output,
                            bairro_output,
                            localidade_output,
                            uf_output,
                            ibge_output,
                            ddd_output,
                        ],
                        spacing=10,
                    ),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.Colors.BLUE_GREY_100,
                    width=300,
                    height=200,
                    alignment=ft.alignment.center_left,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )
    )

# Para rodar a aplicação:
if __name__ == "__main__":
    ft.app(target=main)