import flet as ft
from vues import view_handler


def main(page: ft.Page):
    page.window_width = 400,
    page.window_height = 800
    page.fonts = {
        "Poppins Regular": "fonts/Poppins-Regular.ttf",
        "Poppins Medium": "fonts/Poppins-Medium.ttf",
        "Poppins Bold": "fonts/Poppins-Bold.ttf",
        "Poppins ExtraBold": "fonts/Poppins-ExtraBold.ttf",
        "Poppins Italic": "fonts/Poppins-Italic.ttf",
        "Poppins MediumItalic": "fonts/Poppins-MediumItalic.ttf",
        "Poppins SemiBold": "fonts/Poppins-SemiBold.ttf",
        "Poppins SemiBoldItalic": "fonts/Poppins-SemiBoldItalic.ttf",
        "Poppins Black": "fonts/Poppins-Black.ttf",
        "Poppins BlackItalic": "fonts/Poppins-BlackItalic.ttf",
        "Poppins Light": "fonts/Poppins-Light.ttf",

    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            view_handler(page)[page.route]
        )

    page.on_route_change = route_change
    page.go('/matches')


if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")
