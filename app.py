from flask import Flask, render_template, request
app = Flask(__name__)
#rutas
@app.route('/') #significa la ruta raiz
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
app.run(debug=True, port=5100)