from app.Controllers import Controller


class DashboardController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def index(self):
        return self._render_template("index.html")