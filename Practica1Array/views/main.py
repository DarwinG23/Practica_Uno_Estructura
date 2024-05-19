import sys
sys.path.append('../')
from controls.atencionControl import AtencionControl
from controls.servidorControl import ServidorControl
from controls.tda.queque.queque import QueQue
from controls.tda.array.array import Array




atencion = AtencionControl()
servidor = ServidorControl()
array = Array(5)

atencion._atencion._dia = "05/17/2024"
atencion._atencion._tiempo = "2:30"
atencion._atencion._calificacion = "Bueno"
atencion._atencion._motivo = "Consulta"
#atencion.save

array._addData(atencion._atencion)

# array.print
# print(array._getFirst_())
# print(array.getData(0))

atencion._atencion._dia = "05/17/2024"
atencion._atencion._tiempo = "1:15"
atencion._atencion._calificacion = "Normal"
atencion._atencion._motivo = "Tratamiento"
# atencion.save

array._addData(atencion._atencion)

# array.print





#cola.print


servidor._servidor._nombre = "Juan"
servidor._servidor._cedula = "123456789"
servidor._servidor._atenciones = array
servidor.save


#servidor.merge(0)

#print(servidor._list().getData(1))

#servidor._servidor = None

# arrayDos = Array(5)
# arrayDos = arrayDos.deserializar(servidor._servidor._atenciones.serializable)

# arrayDos.print



# atencion._atencion = None