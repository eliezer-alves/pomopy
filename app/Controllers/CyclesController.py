from app.Controllers import Controller
from app.Models import Cycles, Tags


class CyclesController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._cycles = Cycles()

    def index(self):
        userId = self.user()['id']
        cycles = self._cycles.getCyclesFromUser(userId)
        return self._render_template("cycles/index.html", cycles = cycles)

    def store(self):
        attributes = {
            'duration_in_minutes': self._request.json['duration_in_minutes'],
            'status': 0,
            'tags_id': self._request.json['tags_id'],
            'tasks_id': self._request.json['tasks_id'],
            'users_id': self.user()['id'],
            'start': self.datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        }

        return self._jsonify(self._cycles.create(attributes))
    
    def endCycle(self):
        attributes = {
            'id': self._request.json['id'],
            'status': 1,
            'end': self.datetime.today().strftime('%Y-%m-%d'),
        }

        return self._jsonify(self._cycles.update(attributes))
    
    def delete(self, id):
        self._cycles.delete(id)
        return self._redirect('/tags')