import math
from flask import Flask, render_template, request
import forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key='clave_secreta'
csrf=CSRFProtect()

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

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat, nom, ape, email = 0, "", "", ""
    alumno_clas = forms.UserForm(request.form)
    
    if request.method == 'POST' and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data 
        
    return render_template("alumnos.html", form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)

@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    form = forms.CinepolisForm(request.form)
    total = 0.0
    error_msg = ""
    precio_boleta = 12000

    if request.method == 'POST':
        if form.validate():
            nom = form.nombre.data
            comp = form.compradores.data
            bol = form.boletas.data
            tiene_cineco = form.cineco.data == 'si'

            max_permitido = comp * 7
            
            if bol > max_permitido:
                error_msg = f"No se pueden comprar más de 7 boletas por persona. El máximo para {comp} compradores es {max_permitido}."
            else:
                subtotal = bol * precio_boleta
                descuento = 0.0

                if bol > 5:
                    descuento = 0.15
                elif 3 <= bol <= 5:
                    descuento = 0.10 
                
                total = subtotal * (1 - descuento)

                if tiene_cineco:
                    total = total * 0.90
        else:
            pass

    return render_template('cinepolis.html', form=form, total=total, error=error_msg)

if __name__ =='__main__':
    csrf.init_app(app)
    app.run(debug=True) #cuando se guarde o genere un cambio en el proyecto, va a ser visible en el navegador gracias a debug=True

