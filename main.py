import flet as ft


APPBAR_BG_COLOR = "white"
MAIN_PAGE_BG_COLOR = "white"
BG_COLOR = "white"

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
        # title=ft.Text("Welcome", font_family="Kalnia"),
        center_title=True,
        bgcolor=APPBAR_BG_COLOR,
        # actions=[
        #         ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        #         ft.IconButton(ft.icons.FILTER_3),
        #         ft.PopupMenuButton(
        #             items=[
        #                 ft.PopupMenuItem(text="Item 1"),
        #                 ft.PopupMenuItem(),  # divider
        #                 ft.PopupMenuItem(

        #                 ),
        #             ]
        #         ),
        #     ],
    )

    main_page = ft.Container(
                bgcolor=MAIN_PAGE_BG_COLOR,
                border=ft.border.all(10, ft.colors.WHITE10),
                height=750,
                width=450,
                border_radius=ft.border_radius.all(50),
                expand=True,
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
                                           alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(
                                           [ft.Text(weight="bold",
                                                    font_family="Kalnia",
                                                    size=45,
                                                    spans=[
                                                        ft.TextSpan(text="TRANSFER",
                                                                    style=GRADIENT_STYLE,),
                                                            ]),
                                            ],
                                           alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text(),]),
                                    ft.Row(
                                           [ft.Text(value="Lorem ipsum dolor sit amet,",
                                                    weight="bold",
                                                    size=16,),
                                            ],
                                           alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(
                                           [ft.Text(value="consectetur adipiscing elit,",
                                                    weight="bold",
                                                    size=16,),
                                            ],
                                           alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(
                                           [ft.Text(value=" sed do eiusmod tempor incididunt u",
                                                    weight="bold",
                                                    size=16,),
                                            ],
                                           alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text(),]),
                                    ft.Row([ft.Text(),]),
                                    ft.Row(
                                        [ft.ElevatedButton(text="REGISTER NOW",
                                                           width=300,
                                                           height=50,
                                                           bgcolor="white",
                                                           color="grey",
                                                           elevation=100,
                                                           on_click=lambda _: page.go("/register")), ],
                                        alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(
                                        [ft.ElevatedButton(text="LOGIN",
                                                           width=300,
                                                           height=50,
                                                           bgcolor="white",
                                                           color="grey",
                                                           elevation=100,
                                                           on_click=lambda _: page.go("/login")), ],
                                        alignment=ft.MainAxisAlignment.CENTER),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER),)

    product = ft.Container(
                    bgcolor=MAIN_PAGE_BG_COLOR,
                    border=ft.border.all(10, ft.colors.PINK_300),
                    width=700,
                    height=550,
                    border_radius=ft.border_radius.all(5),
                    expand=True,
                    content=ft.Column(
                        [
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                )
    products = ft.GridView(
        expand=True, max_extent=150, child_aspect_ratio=1,
        controls=[ *[product for i in range(50)] ])

    # VIEWS

    main_page_view = ft.View(
            "/",
            # appbar=appbar,
            controls=[
                main_page,
            ],
            bgcolor=BG_COLOR,
            padding=15
        )

    register_page_view = ft.View(
            "/register",
            # appbar=appbar,
            controls=[
                ft.Container(
                    bgcolor=MAIN_PAGE_BG_COLOR,
                    border=ft.border.all(10, ft.colors.WHITE10),
                    width=700,
                    height=550,
                    border_radius=ft.border_radius.all(50),
                    expand=True,
                    content=ft.Column(
                        [
                            ft.Row([ft.TextField(label="login"),], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([ft.TextField(label="password", password=True),], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([ft.TextField(label="password again", password=True),], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row(
                                [
                                    ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ),
            ],
            bgcolor=BG_COLOR,
        )

    login_page_view = ft.View(
            "/login",
            # appbar=appbar,
            controls = [
                ft.Container(
                    bgcolor=MAIN_PAGE_BG_COLOR,
                    border=ft.border.all(10, ft.colors.WHITE10),
                    width=700,
                    height=550,
                    border_radius=ft.border_radius.all(50),
                    expand=True,
                    content=ft.Column(
                        [
                            ft.Row([ft.TextField(label="login"),], alignment="center"), # type: ignore
                            ft.Row([ft.TextField(label="password", password=True),], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row(
                                [
                                    ft.ElevatedButton("Login", on_click=lambda _: page.go("/profile")),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ),
            ],
            bgcolor=BG_COLOR,
        )

    profile_page_view = ft.View(
            "/profile",
            # appbar=appbar,
            controls=[
                ft.Container(
                    bgcolor=ft.colors.PINK_100,
                    border=ft.border.all(10, ft.colors.PINK),
                    width=700,
                    height=550,
                    border_radius=ft.border_radius.all(5),
                    expand=True,
                    content=ft.Column(
                        [
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ),
                products,
            ],
            bgcolor=BG_COLOR,
        )

    def route_change(route):
        page.views.clear()
        page.views.append(
            main_page_view
        )
        # New page - register
        if page.route == "/register":
            page.views.append(
                register_page_view
            )
        # New page - login
        if page.route == "/login":
            page.views.append(
                login_page_view
            )
        # New page - profile
        if page.route == "/profile":
            page.views.append(
                profile_page_view
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
