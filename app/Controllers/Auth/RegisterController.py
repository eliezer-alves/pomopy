from app.Controllers import Controller
from app.Models import Usuario
import sys



class RegisterController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._usuario = Usuario()

    def create(self):
        return self._render_template("register.html")
    
    def store(self):
        attributes = {
            'name': self._request.form['name'],
            'username': self._request.form['username'],
            'password': self._request.form['password']
        }

        self._usuario.create(attributes)

        return self._usuario.query