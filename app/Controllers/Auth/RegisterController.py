from app.Controllers import Controller
from app.Models import User



class RegisterController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._usuario = User()

    def create(self):
        return self._render_template("register.html")
    
    def store(self):
        if self._request.form['password'] != self._request.form['check_password']:
            self._flash('Failed to register: passwords do not match!')
            return self._redirect('/register')

        attributes = {
            'name': self._request.form['name'],
            'username': self._request.form['username'],
            'password': self._request.form['password']
        }

        if not self._usuario.create(attributes)['id']:
            self._flash('Failed to register!')
            self._redirect('/register')

        self._flash('Registration performed successfully!')
        return self._redirect('/login')