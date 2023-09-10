import flet as ft
from flet import (
    UserControl,
    Column,
    Row,
    Container
)


class LoginPage(UserControl):
    """
    Main page for app.
    """
    def __init__(self, *args, **kwargs):
        self.page = kwargs.pop('page', None)
        super().__init__(*args, **kwargs)

    def build(self):
        self.first_row = Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=ft.icons.WB_CLOUDY),
                ft.IconButton(icon=ft.icons.WB_CLOUDY),
                ft.IconButton(icon=ft.icons.WB_CLOUDY),
            ],

        )
        self.second_row = Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    password=True,
                    autofocus=True,
                    label="Password",
                    on_focus=lambda _: print("FOCUSED"),
                    border=ft.InputBorder.OUTLINE,
                    focused_border_color=ft.colors.CYAN_ACCENT,
                    border_color=ft.colors.INDIGO_900,
                    border_radius=100,
                    border_width=5,
                )
            ],
        )
        # self.third_row = Row(
        #     alignment=ft.MainAxisAlignment.CENTER,
        #     controls=[
        #         ft.TextField(
        #             password=True,
        #             autofocus=True,
        #             label="Email",
        #         )
        #     ],
        # )
        self.fourth_row = Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.FilledButton(
                    text="LOGIN",
                    on_click=lambda _: self.page.go('/register'),
                    on_long_press=lambda _: print("LOONG PRESS"),
                    icon=ft.icons.ADD_TASK_OUTLINED,
                    icon_color=ft.colors.TEAL_ACCENT_100,
                    )
            ],
        )
        self.column = Column(
                controls=[self.first_row, self.second_row, self.fourth_row],
                width=350, # Ширина контейнера
                height=300,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        self.column_colored = Container(
            bgcolor=ft.colors.BLUE_500,
            content=self.column,
            border=ft.border.all(50, ft.colors.BLUE_700), # Ширина и цвет обводки контейнера
        )

        return self.column_colored

class MainPage(UserControl):
    """
    Main page for displaying and add notes.
    """
    def build(self):
        return


def main(page: ft.Page):

    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # делает на странице всё по центру горизонтально
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER # делает на странице всё по центру вертикально

    def route_change(route):
        page.views.clear()
        page.views.append(ft.View(route='/', controls=[LoginPage({'page': page}),],
                              vertical_alignment=ft.MainAxisAlignment.CENTER,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER))
        if page.route == "/register":
            page.views.append(
                ft.View(
                    "/register",
                    [
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                    bgcolor="white",
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.update()


ft.app(target=main, view=ft.AppView.FLET_APP)
