from flask import Flask, render_template, request, redirect, session, flash

from app.Controllers import LoginController, RegisterController, DashboardController, TasksController, TagsController, GuildsController, CyclesController, ColorsController

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

@app.route("/tasks/edit/<int:id>")
def editTask(id):
    return TasksController().edit(id)

@app.route("/tasks/update", methods=['POST'])
def updateTask():
    return TasksController().update()

@app.route("/tasks/delete/<int:id>")
def deleteTask(id):
    return TasksController().delete(id)




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

@app.route("/tags/edit/<int:id>")
def editTag(id):
    return TagsController().edit(id)

@app.route("/tags/update", methods=['POST'])
def updateTag():
    return TagsController().update()

@app.route("/tags/delete/<int:id>")
def deleteTag(id):
    return TagsController().delete(id)




# COLORS__________________________________________________________________________________
@app.route("/colors")
def colors():
    if not session_valid():
        return redirect('/login?callback_url=colors')
    return ColorsController().index()

@app.route("/colors/create")
def createColor():
    if not session_valid():
        return redirect('/login?callback_url=colors')
    return ColorsController().create()

@app.route("/colors/store", methods=['POST'])
def storeColor():
    return ColorsController().store()

@app.route("/colors/edit/<int:id>")
def editColor(id):
    return ColorsController().edit(id)

@app.route("/colors/update", methods=['POST'])
def updateColor():
    return ColorsController().update()

@app.route("/colors/delete/<int:id>")
def deleteColor(id):
    return ColorsController().delete(id)




# TAGS__________________________________________________________________________________
@app.route("/guilds")
def guilds():
    if not session_valid():
        return redirect('/login?callback_url=guilds')
    return GuildsController().index()

@app.route("/guilds/create")
def createGuild():
    if not session_valid():
        return redirect('/login?callback_url=guilds')
    return GuildsController().create()

@app.route("/guilds/store", methods=['POST'])
def storeGuild():
    return GuildsController().store()

@app.route("/guilds/edit/<int:id>")
def editGuild(id):
    return GuildsController().edit(id)

@app.route("/guilds/update", methods=['POST'])
def updateGuild():
    return GuildsController().update()

@app.route("/guilds/delete/<int:id>")
def deleteGuild(id):
    return GuildsController().delete(id)





# Cycles__________________________________________________________________________________
@app.route("/cycles")
def cycles():
    return CyclesController().index()


@app.route("/cycles/store", methods=['POST'])
def storeCycle():
    return CyclesController().store()

@app.route("/cycles/end", methods=['POST'])
def endCycle():
    return CyclesController().endCycle()

if __name__ == '__main__':
	app.run(debug=True)