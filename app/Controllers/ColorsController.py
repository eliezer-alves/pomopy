from app.Controllers import Controller
from app.Models import Colors


class ColorsController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._colors = Colors()

    def index(self):
        colors = self._colors.all()
        return self._render_template("colors/index.html", colors = colors)

    def create(self):
        colors = self._colors.all()
        return self._render_template("colors/create.html", colors = colors)

    def store(self):
        attributes = {
            'name': self._request.form['name'],
            'hexadecimal': self._request.form['hexadecimal'],
        }
        if not self._colors.create(attributes)['id']:
            self._flash('Failed to register!')
            self._redirect('/colors/create')

        return self._redirect('/colors')
    
    def edit(self, id):
        color = self._colors.find(id)
        return self._render_template("colors/edit.html", color = color)
    
    def update(self):
        attributes = {
            'id': self._request.form['id'],
            'name': self._request.form['name'],
            'hexadecimal': self._request.form['hexadecimal'],
        }
        if not self._colors.update(attributes)['id']:
            self._flash('Failed to edit!')
            self._redirect('/colors/edit/{}'.format(self._request.form['id']))

        return self._redirect('/colors')
    
    def delete(self, id):
        self._colors.delete(id)
        return self._redirect('/colors')