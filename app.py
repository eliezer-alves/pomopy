from flask import Flask, render_template, request, redirect, session, flash


app = Flask(__name__)
app.secret_key = 'LP2'
# import routes

class Usuario:
    def __init__(self, username, nome, password):
        self._username = username
        self._nome = nome
        self._password = password

usuario = Usuario('admin', 'Administrador', 'admin')
usuarios = {
    usuario._username: usuario,
}

def session_valid():
    if 'user_logged' not in session or session['user_logged'] == None:
        return False
    return True

# _______________________________________________________________________________________
@app.route("/")
@app.route("/index")
def index():
    if not session_valid():
        return redirect('/login?callback_url=')

    return render_template("index.html")


# _______________________________________________________________________________________
@app.route("/login")
def login():
    callback_url = request.args.get('callback_url') or ""
    return render_template("login.html", callback_url=callback_url)


# _______________________________________________________________________________________
@app.route("/auth", methods=['POST'])
def auth():

    if request.form['username'] in usuarios:
        if usuarios[request.form['username']]._password == request.form['password']:
            session['user_logged'] = request.form['username']
            flash(request.form['username'] + ' logou com sucesso!')
            next_page = request.form['callback_url']
            return redirect("/{}".format(next_page))
    
    flash('Falha ao realizar login para ' + request.form['username'] + '!')
    return redirect('/login')


# _______________________________________________________________________________________
@app.route("/logout")
def logout():

    session['user_logged'] = None
    flash('Sessão finalizada!')
    
    return redirect('/login')



if __name__ == '__main__':
	app.run(debug=True)