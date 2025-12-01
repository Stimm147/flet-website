import flet as ft


def main(page: ft.Page):

    page.title = "Moja strona Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.INDIGO,
        font_family="Verdana",
    )

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_btn.icon = ft.Icons.LIGHT_MODE
            theme_btn.text = "Zmień na Jasny"
            status_text.value = "Aktualny motyw: Ciemny 🌙"
            status_text.color = ft.Colors.BLUE_200
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_btn.icon = ft.Icons.DARK_MODE
            theme_btn.text = "Zmień na Ciemny"
            status_text.value = "Aktualny motyw: Jasny ☀️"
            status_text.color = ft.Colors.INDIGO

        page.update()

    theme_btn = ft.ElevatedButton(
        text="Zmień na Ciemny",
        icon=ft.Icons.DARK_MODE,
        on_click=toggle_theme,
        style=ft.ButtonStyle(
            padding=20,
        ),
    )

    # Stylizowany tekst
    status_text = ft.Text(
        value="Aktualny motyw: Jasny ☀️",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.INDIGO,
        text_align=ft.TextAlign.CENTER,
    )

    card = ft.Container(
        content=ft.Column(
            [ft.Text("Witaj w Flet!", size=30), status_text, ft.Divider(), theme_btn],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=50,
        border_radius=15,
        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
        border=ft.border.all(2, ft.Colors.OUTLINE),
        shadow=ft.BoxShadow(
            blur_radius=10, color=ft.Colors.SHADOW, offset=ft.Offset(0, 5)
        ),
        width=400,
    )

    page.add(card)


ft.app(target=main)
