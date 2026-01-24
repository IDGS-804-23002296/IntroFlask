import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') #ruta por la cual establecemos la pagina a la cual queremos visitar
def index():
    titulo="IDGS804 - Intro Flask"
    listado=['Vianney','Uriel']
    return render_template('index.html', title=titulo, listado=listado)

@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')

@app.route('/saludo2', methods=['GET', 'POST'])
def saludo2():
    resultado = None
    if request.method == 'POST':
        x1 = float(request.form.get('num1'))
        y1 = float(request.form.get('num2'))
        x2 = float(request.form.get('num3'))
        y2 = float(request.form.get('num4'))
        
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        resultado = round(dist, 2)
        
    return render_template('saludo2.html', resultado=resultado)

@app.route('/operasBas', methods=['GET', 'POST'])
def operasBas():
        res=None
        if request.method == 'POST':
            n1=request.form.get('num1')
            n2=request.form.get('num2')
            msj=''

            if request.form.get('operacion') == 'Sumar':
                res=float(n1)+float(n2)
                msj='El resultado de la suma es:'
            if request.form.get('operacion') == 'Restar':
                res=float(n1)-float(n2)
                msj='El resultado de la resta es:'
            if request.form.get('operacion') == 'Multiplicar':
                res=float(n1)*float(n2)
                msj='El resultado de la multiplicación es:'
            if request.form.get('operacion') == 'Dividir':
                res=float(n1)/float(n2)
                msj='El resultado de la división es:'

        return render_template('operasBas.html', msj=msj, res=res)

@app.route('/resultado', methods=['GET', 'POST'])
def resul():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1>La suma es: {float(n1)+float(n2)}</h1>"



@app.route('/hola')
def func():
    return "Hola Mundo - Hola pequeñuelos"

@app.route("/user/<string:user>") #Parametro tipo String
def user(user):
    return f'Hola, {user}'

@app.route("/numero/<int:n>") #Parametro tipo entero
def numero(n):
    return f'<h1>Número: {n}</h1>'

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola {username}, tu id es: {id}</h1>"

@app.route("/suma/<float:n1>/float:n2") #Parametro tipo float
def suma(n1,n2):
    return f"<h1>la suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func2(parm="Juan"):
    return f"<h1>Hola {parm}</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
            <label for "name">Name:</label>
            <input type ="text" id="name" name="name" required>
            </br>
            <label for "name">apaterno:</label>
            <input type ="text" id="name" name="name" required>
            </br>
            <input type= "submit" value="Submit">
        </form>
'''

@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    resultado = None
    if request.method == 'POST':
        x1 = float(request.form.get('num1'))
        y1 = float(request.form.get('num2'))
        x2 = float(request.form.get('num3'))
        y2 = float(request.form.get('num4'))
        
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        resultado = round(dist, 2)
        
    return render_template('distancia.html', resultado=resultado)

if __name__ =='__main__':
    app.run(debug=True) #cada que guarde o genere un cambio en el proyecto, va a ser visible en el navegador gracias a debug=True

