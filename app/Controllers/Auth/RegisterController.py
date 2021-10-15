from app.Controllers.Controller import Controller


class RegisterController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def create(self):
        return self._render_template("register.html")