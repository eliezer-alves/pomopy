from app.Controllers import Controller
from app.Models import Cycles, Tags


class CyclesController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._cycles = Cycles()

    def index(self):
        return

    def store(self):
        # return self._jsonify(self._request.json)

        attributes = {
            'duration_in_minutes': self._request.json['duration_in_minutes'],
            'status': 0,
            'tags_id': self._request.json['tags_id'],
            'tasks_id': self._request.json['tasks_id'],
            'users_id': self._session['user']['id'],
        }
        # print(attributes)
        # return self._jsonify(attributes)

        return self._jsonify(self._cycles.create(attributes))
    
    def update(self):
        return
    
    def delete(self, id):
        self._cycles.delete(id)
        return self._redirect('/tags')