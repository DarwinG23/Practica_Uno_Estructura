from flask import Blueprint, jsonify, abort , request, render_template, redirect, make_response
from flask import flash
from controls.servidorControl import ServidorControl
from controls.atencionControl import AtencionControl
from flask_cors import CORS
import time
router = Blueprint('router', __name__)




#CORS(api)
cors = CORS(router, resource={
    r"/*":{
        "origins":"*"
    }
})

#GET: PARA PRESENTAR DATOS
#POST: GUARDA DATOS, MODIFICA DATOS Y EL INICIO DE SESION, EVIAR DATOS AL SERVIDOR

@router.route('/') #SON GETS
def home():
    return render_template('menu.html')


@router.route('/ventanilla') #SON GETS
def ventanilla():
    return render_template('ventanilla.html')


#LISTA SERVIDORES PUBLICOS
@router.route('/servidores') 
def lista_servidor():
    sc = ServidorControl()
    return render_template('ventanilla/servidorPublico.html', lista=sc.to_dic())


#EDITAR SERVIDOR PUBLICO
@router.route('/servidores/editar/<pos>')
def ver_editar(pos):
    inicio = time.time_ns()
    sc = ServidorControl()
    servidor = sc._list().getData(int(pos)-1)
    fin = time.time_ns()
    print("Tiempo de ejecucion: ", fin-inicio)
    return render_template("ventanilla/editar.html", data = servidor)


#VER ATENCIONES DEL SERVIDOR PUBLICO
@router.route('/servidores/atenciones/<pos>')
def ver_atenciones(pos):
    inicio = time.time_ns()
    sc = ServidorControl()
    atenciones = sc._list().getData(int(pos)-1)._atenciones
    fin = time.time_ns()
    print("Tiempo de ejecucion: ", fin-inicio)
    return render_template("ventanilla/atenciones.html",  lista = atenciones.serializable, idServidor = pos) 


#MODIFICAR SERVIDOR PUBLICO
@router.route('/servidores/modificar', methods=["POST"])
def modificar_servidores():
    inicio = time.time_ns()
    sc = ServidorControl()
    data = request.form
    pos = data["id"]
    serividor = sc._list().getData(int(pos)-1)   
    
    # if not "apellidos" in data.keys():
    #     abort(400)
        
    #TODO ...Validar
    sc._servidor = serividor
    sc._servidor._nombre = data["nombre"]
    sc._servidor._cedula = data["cedula"]

    sc.merge(int(pos)-1)
    fin = time.time_ns()
    print("Tiempo de ejecucion: ", fin-inicio)
    return redirect("/servidores", code=302)


#ELIMINAR SERVIDOR PUBLICO
@router.route('/servidores/eliminar/<pos>')
def eliminar_servidor(pos):
    inicio = time.time_ns()
    sc = ServidorControl()
    sc._delete(int(pos)-1)
    fin = time.time_ns()
    print("Tiempo de ejecucion: ", fin-inicio)
    return redirect("/servidores", code=302)

#ELIMINAR ATENCION
@router.route('/servidores/atenciones/eliminar/<idServidor>')
def eliminar_atencion(idServidor):
    inicio = time.time_ns()
    sc = ServidorControl()
    atenciones = sc._list().getData(int(idServidor)-1)._atenciones
    atenciones.dequeque
    servidor = sc._list().getData(int(idServidor)-1)
    servidor._atenciones = atenciones
    sc.merge(int(idServidor)-1)
    fin = time.time_ns()
    print("Tiempo de ejecucion: ", fin-inicio)
    return redirect("/servidores/atenciones/"+idServidor, code=302)


# INGRESAR NUEVA ATENCION
@router.route('/servidores/atenciones/ver/<idServidor>')
def ver_personas(idServidor):
    return render_template('ventanilla/guardar.html', idServidor = idServidor)



@router.route('/servidores/atenciones/guardar/<idServidor>', methods=["POST"])
def guardar_atencion(idServidor):
    inicio = time.time_ns()
    sc = ServidorControl()
    ac = AtencionControl()
    data = request.form
    ac._atencion._dia = data["dia"]
    ac._atencion._tiempo = data["tiempo"]
    ac._atencion._calificacion = data["calificacion"]
    ac._atencion._motivo = data["motivo"]
    ac.save
    atenciones =  sc._list().getData(int(idServidor)-1)._atenciones
    atenciones._top = 5
    fin = time.time_ns()
    print("Tiempo de ejecucion: ", fin-inicio)
    if atenciones.verifyTop == False: 
        
        return redirect("/servidores/atenciones/"+idServidor,code=302,)
    else:
        atenciones.queque(ac._atencion)
        servidor = sc._list().getData(int(idServidor)-1)
        servidor._atenciones = atenciones
        sc._servidor = servidor
        sc.merge(int(idServidor)-1)
        return redirect("/servidores/atenciones/"+idServidor, code=302)




