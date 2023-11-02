
from flask import *  

import json


# python .\app\app.py

app = Flask(__name__) # se inicializa una app

@app.route('/')
def index():
    #SE PUEDEN CREAR DICCIONARIOS PARA RENDERIZAR CÓDIGO, se colocan como segundo argumento en render_template
    data={
        'title': 'Bienvenido a teCuido'
    }
    
    return render_template('index.html', data= data)

@app.route('/', methods=['POST'])
def info():
    if request.method== 'POST':
        
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        tipoV= request.form['tipoV'] ### TIpo vehículo
        valorA= request.form['valorA']
        AsistenciaVial_VL = request.form.get('AsistenciaVial_VL', 'NO eligio asistencia vial para vehiculos livianos')
        casaConductor= request.form.get('casaConductor', 'NO eligio casa conductor')
        planRenta_VL= request.form.get('planRenta_VL', 'NO eligio planta renta')
        aeroAmbulancia= request.form.get('aeroAmbulancia', 'NO eligio aero ambulancia')
        asistenciaVial_VP= request.form.get('asistenciaVial_VP', 'NO eligio asistencia vial para vehiculos pesados')
        poliza = request.form['poliza']

        data={
            'marca': marca,
            'modelo': modelo,
            'ano': ano,
            'tipoV': tipoV,
            'valorA': valorA,
            'AsistenciaVial_VL': AsistenciaVial_VL,
            'planRenta_VL': planRenta_VL,
            'aeroAmbulancia': aeroAmbulancia,
            'asistenciaVial_VP': asistenciaVial_VP,
            'poliza': poliza,
            'casaConductor': casaConductor

        }

        with open('datos.json', 'w') as file: # como primera instancia toma el nombre que tomará el archivo y como segundo qué pasará allí, se coloca w de Write, lo que quiere decir que enviará a escribir unformación

            json.dump(data, file) # dumb se implementa para guardar datos en un archivo json, toma como primer argumento el diccionario y como segungo argumento envía ese diccionario dentro de datos.json
            
        print(jsonify(data))
        return jsonify(data)
        
        
        
    
if __name__ == '__main__': #se rectifica que se esté en el archivo donde se va a lanzar la app
    app.run(debug=True, port=8080)


    


