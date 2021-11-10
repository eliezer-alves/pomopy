from app.Models import Model

class Colors(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'colors'
        self.fillable = [
            'name',
            'hexadecimal',
        ]