from app.Controllers.Controller import Controller


class LoginController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def create(self):
        callback_url = self._request.args.get('callback_url') or ""
        return self._render_template("login.html", callback_url=callback_url)