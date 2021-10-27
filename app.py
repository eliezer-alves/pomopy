from flask import Flask, render_template, request, redirect, session, flash

from app.Controllers import LoginController, RegisterController, DashboardController, TasksController, TagsController

app = Flask(__name__)
app.secret_key = 'LP2'

teste = 19

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
    if 'user' not in session or session['user'] == None:
        return False
    return True

# _______________________________________________________________________________________
@app.route("/")
@app.route("/index")
def index():
    if not session_valid():
        return redirect('/login?callback_url=')

    return DashboardController().index()


# _______________________________________________________________________________________
@app.route("/login")
def login():
    return LoginController().create()

# _______________________________________________________________________________________
@app.route("/auth", methods=['POST'])
def auth():
    return LoginController().autenticate()

# _______________________________________________________________________________________
@app.route("/logout")
def logout():
    return LoginController().destroy()


# USER___________________________________________________________________________________
@app.route("/register")
def register():
    return RegisterController().create()

@app.route("/user/store", methods=['POST'])
def storeUser():
    return RegisterController().store()


# TASKS__________________________________________________________________________________
@app.route("/tasks")
def tasks():
    if not session_valid():
        return redirect('/login?callback_url=tasks')
    return TasksController().index()


@app.route("/tasks/create")
def createTask():
    if not session_valid():
        return redirect('/login?callback_url=tasks')
    return TasksController().create()

@app.route("/tasks/store", methods=['POST'])
def storeTask():
    return TasksController().store()

@app.route("/tasks/delete")
def deleteTask():
    return TasksController().delete()

# TAGS__________________________________________________________________________________
@app.route("/tags")
def tags():
    if not session_valid():
        return redirect('/login?callback_url=tags')
    return TagsController().index()


@app.route("/tags/create")
def createTag():
    if not session_valid():
        return redirect('/login?callback_url=tags')
    return TagsController().create()

@app.route("/tags/store", methods=['POST'])
def storeTag():
    return TagsController().store()
    



if __name__ == '__main__':
	app.run(debug=True)