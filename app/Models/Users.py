from app.Models import Model

class Users(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'users'
        self.fillable = [
            'name',
            'email',
            'username',
            'password',
        ]