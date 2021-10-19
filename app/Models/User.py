from app.Models import Model

class User(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'users'
        self.fillable = [
            'name',
            'username',
            'password'
        ]