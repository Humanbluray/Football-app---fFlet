import flet as ft
from dotenv import load_dotenv
import os
from supabase import create_client
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# datas
datas_matches = {
    "home": "",
    "away": "",
    "compet": "",
    "level": "",
    "heure": "",
    "statut": "",
    "logo_home": "",
    "logo_away": "",
}


class MatchBox(ft.Container):
    def __init__(self, home: str, away: str, compet: str, level: str, date: str,
                 statut: str, heure: str, logo_home: str, logo_away: str):
        super().__init__(
            height=70,
            width=400, padding=ft.padding.only(top=2, bottom=2, left=10, right=10),
            border_radius=10,
            border=ft.border.all(1, color="#ebebeb")
        )
        self.compet = compet
        self.level = level
        self.entente = ft.Text(f"{self.compet}-{self.level}", size=10, font_family="Poppins Regular", color="grey")
        self.home = home
        self.home2 = ft.Text(self.home, size=14, font_family="Poppins Medium")
        self.date = date
        self.away = away
        self.away2 = ft.Text(self.away, size=14, font_family="Poppins Medium")
        self.statut = statut
        self.statut2 = ft.Text(self.statut, size=12, font_family="Poppins Medium")
        self.heure = heure
        self.heure2 = ft.Text(self.heure[0: 5], size=16, font_family="Poppins Medium")
        self.logo_home = logo_home
        self.logo_home2 = ft.Image(src=f"logos/{self.logo_home}", height=30, width=30)
        self.logo_away = logo_away
        self.logo_away2 = ft.Image(src=f"logos/{self.logo_away}", height=30, width=30)
        self.content = ft.Column(
            [
                self.entente,
                ft.Row(
                    [
                        ft.Row([self.home2, self.logo_home2], spacing=1),
                        self.heure2,
                        ft.Row([self.logo_away2, self.away2], spacing=1),
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.on_click = self.go_match_details

    def go_match_details(self, e):
        global datas_matches
        datas_matches["home"] = self.home
        datas_matches["away"] = self.away
        datas_matches["compet"] = self.compet
        datas_matches["level"] = self.level
        datas_matches["heure"] = self.heure
        datas_matches["statut"] = self.statut
        datas_matches["logo_home"] = self.logo_home
        datas_matches["logo_away"] = self.logo_away
        self.page.go('/')


class Matches(ft.UserControl):
    def __init__(self, page):
        super(Matches, self).__init__()
        self.page = page
        self.donnees = ft.Column()
        self.remplir()

    def remplir(self):
        datas = supabase.table("matches").select("*").execute()
        details = list(datas)[0][1]
        for row in details:
            logo_dom = supabase.table("teams").select("logo").eq("short", str(row["home"])).execute()
            logo_home = list(logo_dom)[0][1][0]['logo']
            logo_ext = supabase.table("teams").select("logo").eq("short", str(row["away"])).execute()
            logo_away = list(logo_ext)[0][1][0]['logo']

            self.donnees.controls.append(
                MatchBox(
                    home=row['home'],
                    away=row['away'],
                    compet=row['compet'],
                    level=row['level'],
                    date=row['date'],
                    statut=row['statut'],
                    heure=row['heure'],
                    logo_home=logo_home,
                    logo_away=logo_away
                )
            )

    def build(self):
        return ft.Container(
            content=self.donnees
        )


class MatchDetails(ft.UserControl):
    def __init__(self, page):
        super(MatchDetails, self).__init__()
        self.page = page
        global datas_matches
        self.back = ft.IconButton(ft.icons.KEYBOARD_ARROW_LEFT_OUTLINED, icon_size=24, on_click=lambda e: self.page.go('/matches'))
        self.notif = ft.IconButton(ft.icons.NOTIFICATIONS_NONE, icon_size=24)
        self.chat = ft.IconButton(ft.icons.CHAT_BUBBLE_OUTLINE, icon_size=24)
        self.entete = ft.Container(
            content=ft.Row(
                [
                    self.back,
                    ft.Row([self.notif, self.chat])
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        self.ligue = ft.Text(f"{datas_matches['compet'].upper()} - {datas_matches['level'].upper()}", size=16, font_family="Poppins Thin")
        self.horaire = ft.Text(str(datas_matches["heure"])[0:5], size=24, font_family="Poppins Medium")
        self.statut = ft.Container(
            bgcolor=ft.colors.BLACK87,
            padding=ft.padding.only(left=10, right=10, top=3, bottom=3),
            content=ft.Text(datas_matches["statut"], size=12, font_family="Poppins Regular", color="white")
        )
        self.home_stack = ft.Stack(
            controls=[
                ft.CircleAvatar(radius=33, bgcolor=ft.colors.TEAL_500),
                ft.CircleAvatar(
                    right=3, bottom=3,
                    radius=30, bgcolor="white",
                    content=ft.Image(src=f"logos/{datas_matches['logo_home']}", height=40, width=40)
                )
            ]
        )
        self.home_name = ft.Text(datas_matches["home"].upper(), size=12, font_family='Poppins Medium')
        self.away_stack = ft.Stack(
            controls=[
                ft.CircleAvatar(radius=33, bgcolor=ft.colors.TEAL_500),
                ft.CircleAvatar(
                    right=3, bottom=3,
                    radius=30, bgcolor="white",
                    content=ft.Image(src=f"logos/{datas_matches['logo_away']}", height=40, width=40)
                )
            ]
        )
        self.away_name = ft.Text(datas_matches["away"].upper(), size=12, font_family='Poppins Medium')
        self.info_tab = ft.Tab(
            text="Preview",
            icon=ft.icons.STADIUM,
            content=ft.Column(
                [
                    ft.Text("avant'match", size=14, font_family="Poppins Bold")
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        self.compo_tab = ft.Tab(
            text="Compos",
            icon=ft.icons.PERSON,
            content=ft.Column(
                [
                    ft.Text("Compositions", size=14, font_family="Poppins Bold")
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        self.analyse_tab = ft.Tab(
            text="Datas",
            icon=ft.icons.BAR_CHART,
            content=ft.Column(
                [
                    ft.Text("Analyses", size=14, font_family="Poppins Bold")
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        self.tab = ft.Tabs(
            animation_duration=500,
            indicator_color=ft.colors.TEAL_500,
            label_color=ft.colors.TEAL_500,
            unselected_label_color=ft.colors.BLACK87,
            selected_index=0,
            divider_color="teal",
            scrollable=True,
            tabs=[self.info_tab, self.compo_tab, self.analyse_tab]
        )

    def build(self):
        return ft.Container(
            ft.Column(
                [
                    self.entete, ft.Divider(height=5),
                    self.ligue,
                    ft.Row(
                        [
                            ft.Column([self.home_stack, self.home_name], spacing=1, horizontal_alignment="center"),
                            ft.Column([self.horaire, self.statut], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.Column([self.away_stack, self.away_name], spacing=1, horizontal_alignment="center"),
                        ], alignment=ft.MainAxisAlignment.SPACE_AROUND
                    ),
                    ft.Divider(height=5, color="transparent"),
                    ft.Container(
                        # alignment="center",
                        padding=ft.padding.only(left=10, right=10),
                        expand=True, height=600,
                        content=self.tab
                    )

                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ), expand=True, height=800
        )
