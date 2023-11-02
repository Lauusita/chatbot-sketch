

import openai
import os 
import json

with open('datos.json', 'r') as file:
    info = json.load(file)



# python .\app\app.py
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

msg = """quiero que seas  un motor de reglas para calcular las valores de total prima anual, que es el valor que seguro que el cliente debe pagar. Pideme la informacion del vehiculo para calcular el valor de la prima total sumando las siguientes reglas a tener en cuenta, además de la suma de los servicios adicionales ( Asistencia Vial (Vehículos livianos) Casa del Conductor (CMA o CAA), Plan Renta (vehículos livianos), Aero Ambulancia.
Asistencia Vial (Vehículos pesados): Perfecto, ahora te voy a pasar un listado completo de requerimiento con diferentes reglas favor tenerlas encuentas y volver a consultarte con nuevo vehiculo.


Tarifa base para Vehículos De Motor con deducible (1% del v/a) y Límites
1MM/1MM/2,000,000 (Para Uso Personal, Privado y Comercial) / Tasas incluyen
Impuestos.
Año Automóvil Jeep Camioneta Carga/Pesados
2023 2.61% 2.38% 2.38% 2.75%
2022 2.61% 2.38% 2.38% 2.75%
2021 2.61% 2.38% 2.38% 2.93%
2020 2.61% 2.38% 2.38% 3.11%
2019 3.66% 3.34% 3.33% 3.32%
2018 3.90% 3.56% 3.54% 3.54%
2017 4.17% 3.81% 3.78% 3.78%
2016 4.45% 4.06% 3.78% 4.03%
2015 4.75% 4.33% 4.30% 4.30%
2014 5.08% 4.63% 4.60% 4.59%
2013 5.42% 4.94% 4.91% 4.90%
2012 5.78% 5.27% 5.25% 5.24%
Tarifa base para Vehículos De Motor (Cero Deducible) y Límites 1MM/1MM/2,000,000
(Para Uso Personal, Privado y Comercial) / Tasas incluyen Impuestos.
Año Automóvil Jeep Camioneta
2023 2.91% 2.68% 2.68%
2022 2.91% 2.68% 2.68%
2021 2.91% 2.68% 2.68%
2020 2.91% 2.68% 2.68%
Ejemplo cálculo de la prima: Multiplicar el valor asegurado x la tarifa, el resultado sumarlo a la
prima de los servicios adicionales. (ejemplo: Jeep 2023 Limites 1/1/2MM: tarifa base RD$1MM x
2.61% = 26,100.00 + RD$4,599.00 (Servicios adicionales), Prima total RD$30,699.00 Impuestos
incluidos.
4
Prima Mínima Vehículos Livianos RD$17,400.00 Impuestos incluidos (ISC) (Para todos los
casos con daños propios, incluye CMA y Asistencia Vial), para vehículos pesados adicionar
RD$4,640.00 a la prima mínima (RD$17,400.00 ISC)
Deducibles
Daños Materiales: 1% del valor asegurado, mínimo RD$5,000.00 vehículos
livianos, y mínimo RD$10,000.00 vehículos pesados.
Rotura de Cristales: 10% de la perdida, mínimo RD$500.00
Servicios Adicionales
Servicios Adicionales Prima Anual Incluye ISC
Asistencia Vial (Vehículos livianos) RD$1,276.00 I/ISC
Casa del Conductor (CMA o CAA) RD$1,293.40 I/ISC
Plan Renta (vehículos livianos) RD$1,160.00 I/ISC
Aero Ambulancia RD$870.00 I/ISC
Asistencia Vial (Vehículos pesados) RD$5.916.00 I/ISC
Responsabilidad Civil (Auto Exceso)
Categorías Límites Asegurados
RD$ 3,000,000.00 RD$5,000,000.00
Vehículos Convencionales, Todo Terreno
(Jeepetas), Jeeps, Camionetas (Pick-Up) y
Vans
RD$1,500.00 Por
Vehículo
RD$1,810.00 Por
Vehículo
Autobuses de uso Privado (Camión, Minibús,
Autobús)
RD$3,120.00 Por
Vehículo
RD$3,519.00 Por
Vehículo
Observaciones:
 Inspección del vehículo: Para vehículos 0km conduce de salida, y para vehículos usados
se requiere inspección por parte de la aseguradora, para la aceptación de la tasación como
inspección, queda sujeto enviar listado de tasadores autorizados por Banco Motor Crédito.
 Listado de vehículos restringidos: Ver anexo.
 Condicionado General vehículos de motor: Ver anexo.
 Requisitos para inclusión de vehículo:
o Solicitud vía email (Datos personales del cliente: Nombres y apellidos, número de
cedula o RNC, dirección domicilio, teléfonos, email y datos generales del vehículo).
o Copia de matrícula o conduce de salida.
o Copia de cedula o Registro Mercantil.
o Formulario de conocimiento (Persona física y Moral)
o Reporte de inspección o conduce de salida.
 Comisión Intermediación: 17.5%.Información Necesaria: Marca y Modelo del Vehículo, Año del Vehículo, Tipo de Vehículo: Automóvil, Jeep, Camioneta, etc. Valor Asegurado del Vehículo,Servicios Adicionales: Asistencia Vial (Vehículos livianos) Casa del Conductor (CMA o CAA), Plan Renta (vehículos livianos), Aero Ambulancia.
Asistencia Vial (Vehículos pesados)(si se desea),Tipo de Póliza*: Con deducible o cero deducible.No olvides definir opciones de respuesta. Ejemplo tipo tipo de vehículo: Automóvil, Jeep, etc.Si no te ha indicado servicios adicionales, preguntale que si quisiera concer los servicios adicionales. Si responde si, muestrale el listado. Tambien indicale que puede preguntarme por el detalle o conocer mas informacion de los servicios adicionales y le puedo indicar. Indicale el listado de servicios adicionales. Porfavor asegurate que la marca y modelo del vehiculo sea verdadero hasta tu fecha de conocimiento. Si no inidcale que la marca existe.
Proceso de Cálculo:
1. *Revisión de Rechazo*: Verificar tipo de vehículo y combustible. Rechazar si no cumple (ej.: si es camión, jeep, o no usa gasolina).
2. Aplicación de Tarifas*: Basada en el año y tipo de vehículo.
3. Suma de Servicios Adicionales*: Si se requieren, como Asistencia Vial, Aero Ambulancia, etc.
4. Comparación con Prima Mínima*: Ajustar si la prima calculada es menor que la prima mínima.
5. Cálculo con/sin Deducible*: Elegir la tasa correspondiente.
    Ejemplo de Cálculo:
    Para *Toyota Cross 2023, Automóvil, valor asegurado de $700,000, con Asistencia Vial y deducible*:
1.Prima Base*: $700,000 × 2.61% = $18,270.
2.Servicio Adicional*: Asistencia Vial = $1,276.
3.Prima Total*: $18,270 (Prima Base) + $1,276 (Servicio) = $19,546.
Instrucciones para Uso de Prompt en Conversaciones Futuras:
1.Recolección de Datos*: Asegúrate de recopilar toda la información necesaria desde el inicio.
2.Uso de la Tabla de Tarifas*: Consulta la tabla para determinar la tasa aplicable.
3.Cálculos Precisos*: Realiza los cálculos siguiendo los pasos del proceso de cálculo.
4.Verificación y Ajuste*: Asegúrate de comparar con la prima mínima y ajustar si es necesario.
5.Claridad en la Comunicación*: Mantén una comunicación clara y precisa con el usuario, especialmente si la póliza no aplica. Por favor, muéstrame el valor de la prima total anual CALCULADA y muéstrame la información total en formato JSON con todos los datos del vehículo registrados, no me muestres el proceso de cálculo, solamente el JSON y la prima total anual calculada. Realízame el cálculo instantáneamente y no me digas que espere un momento.
"""
messages = [{'role': 'system', 'content': msg }]

while(True):


    content =  "la marca del vehículo es: " + info['marca'] + "\t "+ "el modelo del vehículo es: " +info['modelo']+"\t "+"el año del vehículo es: " + info['ano']+"\t "+"el tipo de vehículo es: " + info['tipoV']+"\t "+ "el valor asegurado del vehículo es: " +info['valorA']+"\t "+ "a continuación, los servicios adicionales: la asistencia vial del vehículo: " +info['AsistenciaVial_VL']+"\t "+ ", la planta de renta : " +info['planRenta_VL'] +"\t "+ "el aeroambulancia del vehículo es: " +info['aeroAmbulancia'] + "la asistencia vial del vehículo es: " +info['asistenciaVial_VP'] +"\t "+  ", la casa del conductor del vehículo es: "+info['casaConductor']+"\t "+ "y la póliza de motor del vehículo es: " +info['poliza']+"\t " + "\n" 
    
    

    messages.append({'role': 'user', 'content':  content})
    response = openai.ChatCompletion.create(model='gpt-4', messages=messages)

    print(response.usage)
    print('-----------------------------------------------------')
    print(response.choices[0].message.content)
    break






