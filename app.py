from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
db = sqlite3.connect('data.db', check_same_thread=False)

#rutas
@app.route('/', methods=['GET']) #significa la ruta raiz
def index():
    return render_template('index.html')

@app.route('/saludo/<nombre>/<int:edad>') #nombre de la ruta
def saludar(nombre, edad):
    numeros=[1,2,3,4,5,6]
    return render_template('saludo.html', name=nombre, age=edad, numbers=numeros)

@app.route('/contacto', methods=['GET', 'POST']) 
def contacto():
    #OBTENIENDO FOMRULARIO DE CONTACTO
    if request.method== 'GET':
        return render_template('contacto.html')
    
    nombres=request.form.get('nombres')
    email=request.form.get('email')
    celular=request.form.get('celular')
    observacion=request.form.get('observacion')
    return 'guardando informacion '+ nombres
    #guardando informacion de contacto

@app.route('/sumar') 
def sumar():
    suma=2+2
    return 'la suma de 2 + 2 es = '+str(suma)

@app.route('/usuarios')
def usuarios():
    usuarios = db.execute('select * from usuarios')

    usuarios = usuarios.fetchall()

    return render_template('usuarios/listar.html', usuarios=usuarios)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuarios():
    if request.method == 'GET':
        return render_template('usuarios/crear.html')

    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    email = request.form.get('email')
    password = request.form.get('password')

    cursor = db.cursor()
    cursor.execute("""insert into usuarios(
            nombres,
            apellidos,
            email,
            password
        )values (?,?,?,?)
    """, (nombres, apellidos, email, password))

    db.commit()

    return redirect(url_for('usuarios'))


@app.route('/usuarios/eliminar', methods=['GET','POST'])
def eliminar_usuarios():
    if request.method == 'GET':
        return render_template('usuarios/eliminar.html')
    id = request.form.get('id')
    cursor = db.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?',(id))
    db.commit()
    return redirect(url_for('usuarios'))

@app.route('/usuarios/editar', methods=['GET','POST'])
def editar_usuarios():
    if request.method == 'GET':
        return render_template('usuarios/editar.html')
    id = request.form.get('id')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    passw = request.form.get('password')
    cursor = db.cursor()
    cursor.execute("""
    UPDATE usuarios SET 
    nombres = ?, 
    apellidos = ?, 
    email = ?, 
    password = ? 
    WHERE id = ?
     """,(name,lastname,email,passw,id))
    db.commit()
    return redirect(url_for('usuarios'))

@app.route('/usuarios/editar/<int:id>', methods=['GET','POST'])
def boton_editar(id):
    if request.method == 'GET':

        return render_template('usuarios/editar.html')

@app.route('/usuarios/eliminar/<int:id>', methods=['GET','POST'])
def boton_borrar(id):
    if request.method == 'GET':

        return render_template('usuarios/eliminar.html')

app.run(debug=True, port=5100)





