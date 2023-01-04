import os
import pandas as pd
from Operaciones import *
from flask import Flask, render_template, request, flash, session
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './Archivos'
app.secret_key = 'Hola'


@app.route('/', methods=['GET', 'POST'])
def index():
    # return "HOLA MUNDO"
    session.pop('_flashes', None)
    data = {
        'titulo': 'Index',
    }
    if request.method == 'GET':
        data = {
            'titulo': 'Index'
        }
        return render_template('index.html', data=data)
    elif request.method == 'POST':
        F = request.files['archivo']
        Filename = secure_filename(F.filename)
        FileNameSplit = Filename.split(".")
        if len(FileNameSplit) > 1:
            Extension = FileNameSplit[len(FileNameSplit)-1]
            if Extension == "csv" or Extension == "xml" or Extension == "xlsx" or Extension == "json":
                F.save(os.path.join(app.config['UPLOAD_FOLDER'], Filename))
                File = pd.read_csv("Archivos/" + Filename)
                data = {
                    'titulo': 'Redes neuronales',
                    'Filename': "Archivos/" + Filename,
                    'Encabezados': File.head() 
                }
                if request.form.get('Lineal') == 'Regresión lineal':
                    data['titulo'] = 'Regresión lineal'
                elif request.form.get('Polinomial') == 'Regresión polinomial':
                    data['titulo'] = 'Regresión polinomial'
                elif request.form.get('Gaussiano') == 'Clasificador Gaussiano':
                    data['titulo'] = 'Clasificador Gaussiano'
                elif request.form.get('Arbol') == 'Clasificador de árboles de decisión':
                    data['titulo'] = 'Clasificador de árboles de decisión'
                return render_template('Operaciones.html', data=data)
            else:
                flash('Extension de archivo no soportada')
                return render_template('index.html', data=data)
        else:
            flash('Archivo incompatible')
            return render_template('index.html', data=data)

@app.route('/Lineal', methods=['GET', 'POST'])
def Lineal():
    Filename = request.form.get('Filename')
    x_name = request.form.get('x_name')
    y_name = request.form.get('y_name')
    File = pd.read_csv(Filename)
    data = {
        'titulo': 'Regresión lineal',
        'Filename': Filename,
        'Encabezados': File.head() ,
        'File': File
    }
    URLS = lineal(x_name,y_name, File)
    return render_template('Lineal.html', data=data, URL1 = URLS[0], URL2 = URLS[1])

@app.route('/Poly', methods=['GET', 'POST'])
def Poly():
    Filename = request.form.get('Filename')
    x_name = request.form.get('x_name')
    y_name = request.form.get('y_name')
    File = pd.read_csv(Filename)
    data = {
        'titulo': 'Regresión polinomial',
        'Filename': Filename,
        'Encabezados': File.head() ,
        'File': File
    }
    URLS = polinomial(x_name,y_name, File)
    return render_template('Poly.html', data=data, URL1 = URLS[0], URL2 = URLS[1])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
