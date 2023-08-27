class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None
        _numTV += 1
    
    def setMarca(self,marca):
        self._marca = marca
    def getMarca(self):
        return self._marca
    
    def setCanal(self,canal):
        if self._estado and (1 <= canal <= 120 ):
            self._canal = canal
    def getCanal(self):
        return self._canal
    
    def setPrecio(self,precio):
        self._precio = precio
    def getPrecio(self):
        return self._precio

    def setVolumen(self,volumen):
        if self._estado and (0 <= volumen <= 7 ):
            self._volumen = volumen
    def getVolumen(self):
        return self._volumen
    
    def setControl(self,control):
        self._control = control
    def getControl(self):
        return self._control
    
    @classmethod
    def setNumTV(self,numTV):
        self._numTV = numTV
    @classmethod
    def getNumTV(self):
        return self._numTV
    
    def getEstado(self):
        return self._estado

    def turnOn(self):
        self._estado = True
    def TurnOff(self):
        self._estado = False
    
    def canalUp(self):
        if self._estado and (self._canal < 120):
            self._canal += 1
    def canalDown(self):
        if self._estado and (self._canal > 1):
            self._canal -= 1
    def volumenUp(self):
        if self._estado and (self._volumen < 7):
            self._volumen += 1
    def volumenDown(self):
        if self._estado and (self._volumen > 0):
            self._volumen -= 1
    
            

