from app.Models import Model

class Achievements(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'users'
        self.fillable = [
            'name',
            'description',
            'icon',
        ]