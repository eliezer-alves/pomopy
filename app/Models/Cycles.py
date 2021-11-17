from app.Models import Model

class Cycles(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'cycles'
        self.fillable = [
            'duration_in_minutes',
            'status',
            'tags_id',
            'tasks_id',
            'users_id',
            'start',
            'end',
        ]