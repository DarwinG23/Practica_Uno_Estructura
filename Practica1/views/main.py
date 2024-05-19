import sys
sys.path.append('../')
from controls.atencionControl import AtencionControl
from controls.servidorControl import ServidorControl
from controls.tda.queque.queque import QueQue




atencion = AtencionControl()
servidor = ServidorControl()
cola = QueQue(5)

atencion._atencion._dia = "05/17/2024"
atencion._atencion._tiempo = "2:30"
atencion._atencion._calificacion = "Bueno"
atencion._atencion._motivo = "Consulta"
#atencion.save

cola.queque(atencion._atencion)
atencion._atencion = None

atencion._atencion._dia = "05/17/2024"
atencion._atencion._tiempo = "1:15"
atencion._atencion._calificacion = "Normal"
atencion._atencion._motivo = "Tratamiento"
#atencion.save


cola.queque(atencion._atencion)



atencion._atencion = None

cola.print





#cola.print


servidor._servidor._nombre = "Juan"
servidor._servidor._cedula = "123456789"
servidor._servidor._atenciones = cola
servidor.save

print("deserializar")
#cola.deserializar(cola.serializable).print

servidor._servidor = None



# atencion._atencion = None