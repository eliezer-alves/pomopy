from app.Controllers import Controller
from app.Models import Tags


class TagsController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._tags = Tags()

    def index(self):
        tags = self._tags.all()
        return self._render_template("tags/index.html", tags = tags)

    def create(self):
        return self._render_template("tags/create.html")

    def store(self):
        attributes = {
            'name': self._request.form['name'],
            'color': self._request.form['color'],
        }
        if not self._tags.create(attributes)['id']:
            self._flash('Failed to register!')
            self._redirect('/tags/create')

        return self._redirect('/tags')
    
    def delete(self, id):
        self._tags.delete(id)
        return self._redirect('/tags')