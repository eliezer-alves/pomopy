from app.Controllers import Controller
from app.Models import Guilds


class GuildsController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._guilds = Guilds()

    def index(self):
        guilds = self._guilds.select().where('users_id', 1).get()
        return self._render_template("guilds/index.html", guilds = guilds)

    def create(self):
        return self._render_template("guilds/create.html")

    def store(self):
        attributes = {
            'name': self._request.form['name'],
            'description': self._request.form['description'],
            'users_id': self._session['user']['id']
        }
        if not self._guilds.create(attributes)['id']:
            self._flash('Failed to register!')
            self._redirect('/guilds/create')

        return self._redirect('/guilds')
    
    def edit(self, id):
        guild = self._guilds.find(id)
        return self._render_template("guilds/edit.html", guild = guild)
    
    def update(self):
        attributes = {
            'id': self._request.form['id'],
            'name': self._request.form['name'],
            'description': self._request.form['description'],
        }
        if not self._guilds.update(attributes)['id']:
            self._flash('Failed to edit!')
            self._redirect('/guilds/edit/{}'.format(self._request.form['id']))

        return self._redirect('/guilds')
    
    def delete(self, id):
        self._guilds.delete(id)
        return self._redirect('/guilds')