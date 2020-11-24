from flask import Flask, render_template
app = Flask(__name__)
#rutas
@app.route('/') #significa la ruta raiz
def index():
    return render_template('index.html')

@app.route('/saludo/<nombre>/<int:edad>') #nombre de la ruta
def saludar(nombre, edad):
    numeros=[1,2,3,4,5,6]
    return render_template('saludo.html', name=nombre, age=edad, numbers=numeros)

@app.route('/contacto') 
def contacto():
    return 'queli'

@app.route('/sumar') 
def sumar():
    suma=2+2
    return 'la suma de 2 + 2 es = '+str(suma)
app.run(debug=True, port=5100)