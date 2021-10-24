from app.Models import Model

class Tags(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'users'
        self.fillable = [
            'name',
        ]