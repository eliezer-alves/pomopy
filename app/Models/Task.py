from app.Models import Model

class Task(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'tasks'
        self.fillable = [
            'name',
            'description',
            'user_id'
        ]