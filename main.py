import flet as ft
from flet import (
    Page,
    colors,
    AppBar,
    Control
)



if __name__ == "__main__":

    def main(page: Page):
        def check_item_clicked(event):
            e.control.checked = not e.control.checked
            page.update()

        def change_bg(event: ft.ControlEvent):
            if page.bgcolor == ft.colors.BLACK:
                page.bgcolor = ft.colors.WHITE
            else:
                page.bgcolor = ft.colors.BLACK
            page.update()

        page.title = "My Flet App"
        page.padding = 0
        page.bgcolor = ft.colors.BLACK

        body = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )
        page.add(body)

        for i in [ft.icons.ABC_ROUNDED, ft.icons.ACCESSIBILITY_OUTLINED,]:
            body.controls.append(
                ft.Icon(i,
                scale=4,
                )
            )

        page.appbar = ft.AppBar(
                leading=ft.Icon(ft.icons.PALETTE),
                leading_width=40,
                title=ft.Text("MyFirstApp"),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                        ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_bg),
                        ft.IconButton(ft.icons.FILTER_3),
                        ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(text="Item 1"),
                                ft.PopupMenuItem(),  # divider
                                ft.PopupMenuItem(
                                    text="Checked item",
                                    checked=False,
                                    on_click=check_item_clicked
                                ),
                            ]
                        ),
                    ],
        )
        page.update()

    ft.app(target=main, view=ft.WEB_BROWSER)
