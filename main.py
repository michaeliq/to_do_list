from flask import Flask, render_template, redirect, url_for, request
import bcrypt

app = Flask(__name__)

#variables
salt = bcrypt.gensalt(8)
tareas = []

@app.route('/', methods=['GET','POST'])
def hogar():
    if request.method == 'GET':
        return render_template('home.html',tareas=tareas)
    elif request.method == 'POST':
        actividad = request.form['actividad']
        #print(actividad)
        crear_tarea(actividad)
        return redirect(url_for('hogar'))

@app.route("/delete/<_id>/")
def tarea_completada(_id):
    global tareas
    nueva_lista = filter(lambda x: True if x['id'].decode()[35:45] != _id else False, tareas)
    print(list(nueva_lista))
    tareas = nueva_lista
    return redirect(url_for('hogar'))

def crear_tarea(tarea):
    tareas.append({'id':bcrypt.hashpw(tarea.encode(),salt),'tarea':tarea})

