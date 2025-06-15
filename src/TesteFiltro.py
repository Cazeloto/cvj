import flet as ft
import psycopg2

# --- Configurações do Banco de Dados ---
DB_HOST = "localhost"
DB_NAME = "CVJ"
DB_USER = "postgres"
DB_PASSWORD = "PM@rcia01"
DB_TABLE = "consulente"  # Nome da tabela que contém os nomes
DB_COLUMN_NAME = "con_nome"  # Coluna que contém os nomesfle

def buscar_nomes_do_banco():
    """Busca todos os nomes da tabela no banco de dados."""
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cur = conn.cursor()
        cur.execute(f"SELECT {DB_COLUMN_NAME} FROM {DB_TABLE}")
        nomes = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return nomes
    except psycopg2.Error as e:
        print(f"Erro ao conectar ou buscar dados do PostgreSQL: {e}")
        return []

def main(page: ft.Page):
    page.title = "Filtrar Nomes"

    todos_nomes = buscar_nomes_do_banco()
    lista_filtrada_control = ft.ListView(expand=True)
    nome_selecionado = ft.TextField(label="Nome Selecionado", disabled=True)

    def item_clicado(e):
        nome = e.control.title.
        #nome = e.control.title.value
        nome_selecionado.value = nome
        page.update()

    def atualizar_lista(e):
        texto_filtro = filtro_texto.value.lower()
        lista_filtrada_control.controls.clear()
        for nome in todos_nomes:
            if texto_filtro in nome.lower():
                item_lista = ft.ListTile(
                    title=ft.Text(nome),
                    on_click=item_clicado
                )
                lista_filtrada_control.controls.append(item_lista)
        page.update()

    filtro_texto = ft.TextField(
        label="Filtrar",
        on_change=atualizar_lista,
        expand=True,
    )

    # Inicializa a lista com todos os nomes
    for nome in todos_nomes:
        item_lista = ft.ListTile(
            title=ft.Text(nome),
            on_click=item_clicado
        )
        lista_filtrada_control.controls.append(item_lista)

    page.add(
        filtro_texto,
        lista_filtrada_control,
        nome_selecionado,
    )

if __name__ == "__main__":
    ft.app(target=main)