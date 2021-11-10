from app.Controllers import Controller
from app.Models import Users


class LoginController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._users = Users()

    def create(self):
        callback_url = self._request.args.get('callback_url') or ""
        return self._render_template("auth/login.html", callback_url=callback_url)
    
    def autenticate(self):
        username = self._request.form['username']
        password = self._request.form['password']

        authUser = self._users.select().where('username', username).andWhere('password', password).first()
        
        if 'id' in authUser:
            self._session['user'] = authUser
            next_page = self._request.form['callback_url']
            return self._redirect("/{}".format(next_page))
    
        self._flash('Failed to perform login for ' + self._request.form['username'] + '!')
        return self._redirect('/login')
    
    def destroy(self):
        self._session['user'] = None
        self._flash('Session ended!')
        
        return self._redirect('/login')
