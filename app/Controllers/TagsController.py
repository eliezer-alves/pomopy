from app.Controllers import Controller
from app.Models import Tags, Colors


class TagsController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._tags = Tags()

    def index(self):
        userId = self._session['user']['id']
        tags = self._tags.select().where('users_id', userId).get()
        return self._render_template("tags/index.html", tags = tags)

    def create(self):
        colors = Colors().all()
        return self._render_template("tags/create.html", colors = colors)

    def store(self):
        attributes = {
            'name': self._request.form['name'],
            'color': self._request.form['color'],
            'users_id': self._session['user']['id'],
        }
        if not self._tags.create(attributes)['id']:
            self._flash('Failed to register!')
            self._redirect('/tags/create')

        return self._redirect('/tags')
    
    def edit(self, id):
        tag = self._tags.find(id)
        return self._render_template("tags/edit.html", tag = tag)
    
    def update(self):
        attributes = {
            'id': self._request.form['id'],
            'name': self._request.form['name'],
            'color': self._request.form['color'],
        }
        if not self._tags.update(attributes)['id']:
            self._flash('Failed to edit!')
            self._redirect('/tags/edit/{}'.format(self._request.form['id']))

        return self._redirect('/tags')
    
    def delete(self, id):
        self._tags.delete(id)
        return self._redirect('/tags')