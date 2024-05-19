from controls.exception.arrayEmpty import ArrayEmpty
from controls.exception.arrayPositionException import ArrayPositionException
from models.atencion import Atencion


class Array(object):
    def __init__(self, size):
        self.__size = size
        self.__array = [None] * size

    @property
    def _size(self):
        return self.__size

    @_size.setter
    def _size(self, value):
        self.__size = value

    @property
    def _array(self):
        return self.__array

    @_array.setter
    def _array(self, value):
        self.__array = value

    def _isEmpty_(self):
        return self.__array == None or self.__size == 0
    
    def _getFirst_(self):
        if not self._isEmpty_():
            return self.__array[0]
        else:
            return "Array is Empty"
        
    def _getLast_(self):
        if not self._isEmpty_():
            return self.__array[self.__size - 1]
        else:
            return "Array is Empty"
        
    def getData(self, poss):
        if self._isEmpty_():
            raise ArrayEmpty("Array is Empty")
        elif poss < 0 or poss >= self.__size:
            raise ArrayPositionException("Index out of range")
        else:
            return self.__array[poss]
        
    def setData(self, poss, value):
        if self._isEmpty_():
            raise ArrayEmpty("Array is Empty")
        elif poss < 0 or poss >= self.__size:
            raise ArrayPositionException("Index out of range")
        else:
            self.__array[poss] = value

    def _addFirst_(self, value):
        if self._isEmpty_():
            self.__array[0] = value
        else:
            for i in range(self.__size - 1, 0, -1):
                self.__array[i] = self.__array[i - 1]
            self.__array[0] = value

    def _addLast_(self, value):
        if self._isEmpty_():
            self.__array[0] = value
        else:
            self.__array[self.__size] = value

    def _merge(self, value, poss):
        if poss < 0 or poss >= self.__size:
            raise ArrayPositionException("Index out of range")
        else:
            self.__array[poss] = value

    def _delateData_(self, poss):
        if poss < 0 or poss >= self.__size:
            raise ArrayPositionException("Index out of range")
        else:
            for i in range(poss, self.__size - 1):
                self.__array[i] = self.__array[i + 1]
            self.__array[self.__size - 1] = None

    def _addData(self, value):
        for i in range(self.__size):
            if self.__array[i] == None:
                self.__array[i] = value
                break
    
    @property
    def serializable(self):
        aux = []
        for i in range(0, self.__size):
            if self.__array[i] != None:
                aux.append(self.__array[i].serializable)
        return aux
    
    def deserializar(self, dic):
        new_array = Array(len(dic))
        for i in range(0, len(dic)):
            if dic[i] != None:
                atencion = Atencion()
                atencion = atencion.deserializar(dic[i])
                new_array._addData(atencion)
        return new_array
        
     
    @property
    def print (self):
        print("Array:")
        for i in range(self.__size):
            if self.__array[i] != None:
               print(self.__array[i])
    

    def clear(self):
        self.__array = [None] * self.__size
        
    



    @property
    def count(self):
        count = 0
        for i in range(self.__size):
            if self.__array[i] != None:
                count += 1
        return count
    
    def delete(self, poss):
        if poss < 0 or poss >= self.__size:
            raise ArrayPositionException("Index out of range")
        else:
            self.__array[poss] = None
            for i in range(poss, self.__size - 1):
                self.__array[i] = self.__array[i + 1]
            self.__array[self.__size - 1] = None

    
    def __str__(self):
        out = ""
        for i in range(self.__size):
            if self.__array[i] != None:
                out += str(self.__array[i]) + " -> "
        return out
            
    

    
    
        

    



    

   