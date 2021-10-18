from app.Controllers import Controller
from app.Models import Usuario



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

        if not self._usuario.create(attributes)['id']:
            self._flash('Falha ao realizar o cadastro!')
            self._redirect('/register')

        self._flash('Cadastro realizado com sucesso!')
        return self._redirect('/login')