import flet as ft
import psycopg2
from psycopg2 import sql

# Database connection - update with your credentials
DB_CONFIG = {
    "dbname": "CVJ",
    "user": "postgres",
    "password": "PM@rcia01",
    "host": "localhost",
    "port": "5432"
}

def fetch_names(filter_text=""):
    """Fetch names from PostgreSQL database with optional filter"""
    conn = psycopg2.connect(**DB_CONFIG)
    
    try:
        with conn.cursor() as cursor:
            query = sql.SQL("SELECT con_codigo as ID, con_nome as nome FROM consulente")
            if filter_text:
                query = sql.SQL("{} WHERE con_nome ILIKE %s").format(query)
                cursor.execute(query, (f"%{filter_text}%",))
            else:
                cursor.execute(query)
            
            return cursor.fetchall()
    finally:
        conn.close()

def main(page: ft.Page):
    page.title = "Name Browser"
    page.window_width = 400
    page.window_height = 500
    
    # Create dialog (popup)
    dialog = ft.AlertDialog(
        title=ft.Text("Details"),
        content=ft.Text("hhhhh"),
        actions=[
            ft.TextButton("OK", on_click=lambda e: close_dialog(e)),
        ]
    )
    
    def close_dialog(e):
        dialog.open = False
        page.update()
    
    def show_name_details(e):
        name_id = e.control.data
        conn = psycopg2.connect(**DB_CONFIG)
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT con_nome FROM consulente WHERE con_codigo = %s", (name_id,))
                name = cursor.fetchone()[0]
                dialog.content.value = f"Selected: {name}"
                dialog.open = True
                page.update()
        finally:
            conn.close()
    
    def update_name_list():
        names = fetch_names(filter_input.value)
        name_list.controls.clear()
        
        for name_id, name in names:
            name_list.controls.append(
                ft.ListTile(
                    title=ft.Text(name),
                    on_click=show_name_details,
                    data=name_id  # Store ID for the click handler
                )
            )
        
        page.update()
    
    # UI Elements
    filter_input = ft.TextField(
        label="Search names",
        on_change=lambda e: update_name_list(),
        expand=True
    )
    
    name_list = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.ALWAYS,
        expand=True
    )
    
    # Initial load
    update_name_list()
    
    # Add elements to page
    page.add(
        ft.Row(
            [
                filter_input,
                ft.IconButton(
                    icon=ft.Icons.SEARCH,
                    on_click=lambda e: update_name_list()
                )
            ]
        ),
        ft.Divider(),
        name_list
    )
    
    page.dialog = dialog

ft.app(target=main)