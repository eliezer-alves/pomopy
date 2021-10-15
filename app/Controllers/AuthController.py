from . import Controller

class AuthController():

    def login(self):
        callback_url = self._request.args.get('callback_url') or ""
        return self._render_template("login.html", callback_url=callback_url)
