import flet as ft


APPBAR_BG_COLOR = "#50b8e7"
MAIN_PAHE_BG_COLOR = "#b9e2f5"
BG_COLOR = "#84cdee"

GRADIENT_STYLE = ft.TextStyle(size=40, weight=ft.FontWeight.BOLD,
                 foreground=ft.Paint(gradient=ft.PaintLinearGradient((100, 10), (10, 100), ["#50b8e7", "#edf7fc"])),)


def main(page: ft.Page):
    page.fonts = {
        "Kalnia": "https://fonts.googleapis.com/css2?family=Kalnia&display=swap"
    }

    page.title = "MoneyHoney"
    page.window_height = 700
    page.window_width = 450

    dlg = ft.AlertDialog(
        title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU,
                              on_click=open_dlg),
        title=ft.Text("Welcome", font_family="Kalnia"),
        center_title=True,
        bgcolor=APPBAR_BG_COLOR,
    )

    main_page = ft.Container(
                bgcolor=MAIN_PAHE_BG_COLOR,
                border=ft.border.all(10, ft.colors.WHITE10),
                content=ft.Column(
                                  [
                                    ft.Row(
                                           [ft.Text(size=45,
                                                    font_family="Kalnia",
                                                    spans=[
                                                        ft.TextSpan(text="MONEY",
                                                                    style=GRADIENT_STYLE,),
                                                            ])
                                            ],
                                           alignment="center"),
                                    ft.Row(
                                           [ft.Text(weight="bold",
                                                    font_family="Kalnia",
                                                    size=45,
                                                    spans=[
                                                        ft.TextSpan(text="TRANSFER",
                                                                    style=GRADIENT_STYLE,),
                                                            ]),
                                            ],
                                           alignment="center"),
                                    ft.Row([ft.Text(),]),
                                    ft.Row(
                                           [ft.Text(value="Lorem ipsum dolor sit amet,",
                                                    weight="bold",
                                                    size=16,),
                                            ],
                                           alignment="center"),
                                    ft.Row(
                                           [ft.Text(value="consectetur adipiscing elit,",
                                                    weight="bold",
                                                    size=16,),
                                            ],
                                           alignment="center"),
                                    ft.Row(
                                           [ft.Text(value=" sed do eiusmod tempor incididunt u",
                                                    weight="bold",
                                                    size=16,),
                                            ],
                                           alignment="center"),
                                    ft.Row([ft.Text(),]),
                                    ft.Row([ft.Text(),]),
                                    ft.Row(
                                        [ft.ElevatedButton(text="REGISTER NOW",
                                                           width=300,
                                                           height=50,
                                                           bgcolor="white",
                                                           color="black",
                                                           elevation=100,
                                                           on_click=lambda _: page.go("/register")), ],
                                        alignment="center"),
                                    ],
                                alignment="center"),
                width=700,
                height=550,
                border_radius=ft.border_radius.all(5),
    )


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    appbar,
                    main_page,
                ],
                bgcolor=BG_COLOR,
                padding=15
            )
        )
        if page.route == "/register":
            page.views.append(
                ft.View(
                    "/register",
                    [
                        appbar,
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


ft.app(target=main)
