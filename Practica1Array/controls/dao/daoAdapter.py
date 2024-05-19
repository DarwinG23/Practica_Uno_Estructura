from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List
from controls.tda.array.array import Array
import os.path

import json
import os

T = TypeVar('T')
class DaoAdapter(Generic[T]):
    atype: Type[T]

    def __init__(self, atype: Type[T]):
        self.atype = atype
        self.lista =  Array(10)              
        self.file = atype.__name__.lower()+".json"
        self.URL = os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))) + "/data/"

    def _list(self):
        if os.path.isfile(self.URL+self.file):
            f = open(self.URL+self.file, "r")
            datos = json.load(f)
            print("clear")
            self.lista.clear   
            for data in datos:
                a = self.atype.deserializar(data) 
                self.lista._addData(a)
        return self.lista
    
    def __transform__(self):
        aux = "["
        for i in range(0, self.lista._size):
            if i < self.lista._size - 1 and self.lista.getData(i) != None and self.lista.getData(i+1) != None:
                aux += str(json.dumps(self.lista.getData(i).serializable)) + ","
            elif self.lista.getData(i) != None:
                aux += str(json.dumps(self.lista.getData(i).serializable))
        aux += "]"

        return aux
    
    def to_dic(self):
        aux = []
        self._list()
        for i in range(0, self.lista._size):
            if self.lista.getData(i) != None:
               aux.append(self.lista.getData(i).serializable)

        return aux
    
    def _save_json(self, data):
        name = self.atype.__name__
        with open("../files/"+ name + ".json", "w") as outfile:
            json.dump(data, outfile, indent=4)

    def read_json(self):
        if os.path.exists("../files/persona.json"): #si existe el archivo
            with open("../files/persona.json") as file: #abrir archivo
                data = json.load(file)
                self.lista = None
                return self.lista.dicToList(data)
        else:
           return self.__lista

    

    def _save(self, data) -> T:
        self._list()
        self.lista._addData(data) 
        data._id = self.lista.count
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()
        self.lista.clear

    def _delete(self, pos) -> T:
        self._list()
        self.lista.delete(pos)
        self.lista.print
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()


    def _merge(self, data: T, pos) -> T:
        data._id = pos + 1
        self._list()
        self.lista.print
        self.lista._merge(data, pos)
        self.lista.print
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()
     