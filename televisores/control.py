class Control:
    def __init__(self):
        self._tv = None
    
    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)
    
    def turnOn(self):
        self._tv._estado(True)
    def turnOff(self):
        self._tv._estado(False)

    def canalUp(self):
        if self._tv.estado and (self._tv._canal < 120 ):
            self._tv._canal += 1
    def canalDown(self):
        if self._tv.estado and (self._tv._canal > 1):
            self._tv._canal -= 1    
    def volumenUp(self):
        if self._tv.estado and (self._tv._volumen < 7):
            self._tv._volumen += 1
    def volumenDown(self):
        if self._tv.estado and (self._tv._volumen > 0):
            self._tv._volumen -= 1
    
    def setCanal(self,canal):
       if self._estado and (1 <= canal <= 120 ):
           self._tv._canal = canal
    def setVolumen(self,volumen):
       if self._estado and (0 <= volumen <= 7 ):
           self._tv._volumen = volumen

    def setTv(self,tv):
        self._tv = tv 
    def getTv(self):
        return self._tv