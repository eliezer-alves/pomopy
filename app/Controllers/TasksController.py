from app.Controllers import Controller
from app.Models import Tasks


class TasksController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._tasks = Tasks()

    def index(self):
        tasks = self._tasks.select().where('users_id', 1).get()
        return self._render_template("tasks/index.html", tasks = tasks)

    def create(self):
        return self._render_template("tasks/create.html")

    def store(self):
        attributes = {
            'name': self._request.form['name'],
            'description': self._request.form['description'],
            'users_id': self._session['user']['id']
        }
        if not self._tasks.create(attributes)['id']:
            self._flash('Failed to register!')
            self._redirect('/tasks/create')

        return self._redirect('/tasks')
    
    def edit(self, id):
        task = self._tasks.find(id)
        return self._render_template("tasks/edit.html", task = task)
    
    def update(self):
        attributes = {
            'id': self._request.form['id'],
            'name': self._request.form['name'],
            'description': self._request.form['description'],
        }
        if not self._tasks.update(attributes)['id']:
            self._flash('Failed to edit!')
            self._redirect('/tasks/edit/{}'.format(self._request.form['id']))

        return self._redirect('/tasks')
    
    def delete(self, id):
        self._tasks.delete(id)
        return self._redirect('/tasks')