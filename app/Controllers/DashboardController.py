from app.Controllers import Controller
from app.Models import Tags, Tasks


class DashboardController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def index(self):
        userId = self.user()['id']
        tags = Tags().all()
        tasks = Tasks().select().where('users_id', userId).get()
        return self._render_template("index.html", tags = tags, tasks = tasks)