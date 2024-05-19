
from models.atencion import Atencion
from controls.tda.queque.queque import QueQue
from controls.tda.array.array import Array

class Servidor:
    def __init__(self):
        self.__id = 0
        self.__nombre = ""
        self.__atenciones = Array(5)
        self.__cedula = "" 

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value


    @property
    def _atenciones(self):
        return self.__atenciones

    @_atenciones.setter
    def _atenciones(self, value):
        self.__atenciones = value


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value


    

    @property
    def serializable(self):

        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cedula": self.__cedula,
            "atenciones": self.__atenciones.serializable
        }
    
    @classmethod
    def deserializar(self, data):
        servidor = Servidor()
        servidor._id = data["id"]
        servidor._nombre = data["nombre"]
        servidor._cedula = data["cedula"]
        servidor._atenciones = Array(0).deserializar(data["atenciones"])

        return servidor
        
        


    def __str__(self):
        return f'{self._id} - {self._nombre} - {self._cedula} - {self._atenciones}'