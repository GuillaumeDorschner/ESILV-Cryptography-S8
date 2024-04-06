import pytermgui as ptg
from .utils import SignUp, Login

CONFIG = """
config:
    InputField:
        styles:
            prompt: dim italic
            cursor: '@72'
    Label:
        styles:
            value: dim bold

    Window:
        styles:
            border: '60'
            corner: '60'

    Container:
        styles:
            border: '96'
            corner: '96'
"""

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)


def showDialog(manager, title, content):
    modal = ptg.Window(
        title,
        ptg.Label(content),
        ptg.Button("OK", onclick=lambda *_: manager.close()),
        box=ptg.boxes.DOUBLE,
    ).center()

    manager.add(modal)
    manager.focus(modal)


def display_result(manager, result):
    content_lines = []

    title = f"{result.get('operation')} {'SUCCESSFUL' if result.get('success') else 'FAILED'}"

    for key, value in result.items():
        content_lines.append(f"[bold]{key}: [/]{value}")

    content = "\n".join(content_lines)

    showDialog(manager, title, content)


def login(manager):
    for window in manager._windows:
        window.close()
    fields = {
        "Username": ptg.InputField("Username: ", placeholder="Username"),
        "Password": ptg.InputField(
            "Password: ", placeholder="Password", is_password=True
        ),
    }

    def handle_login(*_):
        try:
            username = fields["Username"].value
            password = fields["Password"].value

            if not username or not password:
                raise ValueError("Username and password cannot be empty.")

            data = Login(username, password)

            display_result(manager, data)
        except Exception as e:
            showDialog(manager, "Login Failed", "error: " + str(e) + " occurred.")

    login_window = ptg.Window(
        "[bold]Login[/bold]",
        *fields.values(),
        ptg.Button("Login", onclick=handle_login),
        ptg.Button("Back", onclick=lambda *_: main_menu(manager)),
        box=ptg.boxes.SINGLE,
        width=40,
    )
    manager.layout.add_slot("Body")
    manager.add(login_window.center())
    manager.focus(login_window)


def signup(manager):
    for window in manager._windows:
        window.close()
    fields = {
        "Username": ptg.InputField("Username: ", placeholder="Username"),
        "Password": ptg.InputField(
            "Password", placeholder="Password", is_password=True
        ),
    }

    def handle_signup(*_):
        try:
            username = fields["Username"].value
            password = fields["Password"].value

            data = SignUp()

            if not username or not password:
                raise ValueError("Username and password cannot be empty.")

            display_result(manager, data)
        except Exception as e:
            showDialog(manager, "Signup Failed", "error: " + str(e) + " occurred.")

    signup_window = ptg.Window(
        "[bold]Signup[/bold]",
        *fields.values(),
        ptg.Button("Signup", onclick=handle_signup),
        ptg.Button("Back", onclick=lambda *_: main_menu(manager)),
        box=ptg.boxes.SINGLE,
        width=40,
    )
    manager.layout.add_slot("Body")
    manager.add(signup_window.center())
    manager.focus(signup_window)


def main_menu(manager):
    for window in manager._windows:
        window.close()

    manager.layout.add_slot("Body")

    menu = ptg.Window(
        ptg.Button("Login", onclick=lambda *_: login(manager)),
        ptg.Button("Sign Up", onclick=lambda *_: signup(manager)),
        ptg.Button("Quit", onclick=lambda *_: manager.stop()),
        box=ptg.boxes.SINGLE,
        width=30,
    )

    manager.add(menu.center())


def main():
    with ptg.WindowManager() as manager:
        main_menu(manager)


if __name__ == "__main__":
    main()
