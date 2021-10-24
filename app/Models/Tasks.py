from app.Models import Model

class Tasks(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'tasks'
        self.fillable = [
            'name',
            'description',
            'users_id',
        ]