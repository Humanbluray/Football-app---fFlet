import flet as ft
from result import MatchDetails, Matches


def view_handler(page):
    return {
            '/': ft.View(
                route='/',
                controls=[
                    MatchDetails(page)
                ]
            ),
            '/matches': ft.View(
                route='/matches',
                controls=[
                    Matches(page)
                ]
            )

    }
