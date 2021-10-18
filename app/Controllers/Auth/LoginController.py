from app.Controllers import Controller
from app.Models import Usuario


class LoginController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._usuario = Usuario()

    def create(self):
        callback_url = self._request.args.get('callback_url') or ""
        return self._render_template("login.html", callback_url=callback_url)
    
    def autenticate(self):
        username = self._request.form['username']
        password = self._request.form['password']
        authUser = self._usuario.select().where('username', username).andWhere('password', password).get()
        print(authUser)
        if 'id' in authUser:
            self._session['user_logged'] = self._request.form['username']
            self._flash(self._request.form['username'] + ' logou com sucesso!')
            next_page = self._request.form['callback_url']
            return self._redirect("/{}".format(next_page))
    
        self._flash('Falha ao realizar login para ' + self._request.form['username'] + '!')
        return self._redirect('/login')
    
    def destroy(self):
        self.session['user_logged'] = None
        self.flash('Sessão finalizada!')
        
        return self._redirect('/login')
        