import flet as ft
import asyncio
import asyncpg

# Função para buscar dados do PostgreSQL
async def buscar_nomes(filtro):
    conn = await asyncpg.connect(
        user='postgres',
        password='PM@rcia01',
        database='CVJ',
        host='localhost'
    )
    rows = await conn.fetch(
        "SELECT con_nome FROM consulente WHERE con_nome ILIKE $1 LIMIT 10",
        f"%{filtro}%"
    )
    await conn.close()
    return [r['con_nome'] for r in rows]

# Função principal Flet
def main(page: ft.Page):
    page.title = "Filtro Dinâmico PostgreSQL"
    page.vertical_alignment = ft.MainAxisAlignment.START

    nome_selecionado = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)
    entrada = ft.TextField(label="Digite um nome", autofocus=True, on_change=lambda e: asyncio.run(atualizar_lista(e.control.value)))
    lista_resultados = ft.Column(visible=False)

    async def atualizar_lista(filtro):
        if not filtro:
            lista_resultados.visible = False
            lista_resultados.controls.clear()
            await page.update_async()
            return

        nomes = await buscar_nomes(filtro)
        lista_resultados.controls.clear()

        for nome in nomes:
            item = ft.ListTile(
                title=ft.Text(nome),
                on_click=lambda e, n=nome: selecionar_nome(n)
            )
            lista_resultados.controls.append(item)

        lista_resultados.visible = bool(nomes)
        await page.update_async()

    def selecionar_nome(nome):
        nome_selecionado.value = f"Selecionado: {nome}"
        lista_resultados.visible = False
        entrada.value = nome
        page.update()

    page.add(entrada, lista_resultados, nome_selecionado)

# Executar Flet app
ft.app(target=main)
