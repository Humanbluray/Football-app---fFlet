import flet as ft
from dotenv import load_dotenv
import os
from supabase import create_client
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def remplir_logo(e):
    c.value = f"{b.value}.png"
    c.update()


def create(e):
    data = supabase.table("teams").insert({"name": a.value, "short": b.value, "logo": c.value}).execute()
    print("ok")
    a.value = ""
    b.value = ""
    c.value = ""
    for w in (a, b, c):
        w.update()


a = ft.TextField(label="name")
b = ft.TextField(label="short name", on_change=remplir_logo)
c = ft.TextField(label="logo", disabled=True)
d = ft.ElevatedButton("creer", on_click=create)


def main(page: ft.Page):

    page.add(a, b, c, d)
    page.update()


if __name__ == '__main__':
    ft.app(target=main)


