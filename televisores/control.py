class Control:
    def __init__(self):
        self.tv = None
    
    def enlazar(self, tv):
        self.tv = tv
        self.tv.setControl(self)
    
    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        if self.tv.estado and (self.tv.canal < 120 ):
            self.tv.canal += 1
    def canalDown(self):
        if self.tv.estado and (self.tv.canal > 1):
            self.tv.canal -= 1    
    def volumenUp(self):
        if self.tv.estado and (self.tv.volumen < 7):
            self.tv.volumen += 1
    def volumenDown(self):
        if self.tv.estado and (self.tv.volumen > 0):
            self.tv.volumen -= 1
    
    def setCanal(self,canal):
       if self.tv.getEstado() and (1 <= canal <= 120 ):
           self.tv.canal = canal
    def setVolumen(self,volumen):
       if self.tv.getEstado() and (0 <= volumen <= 7 ):
           self.tv.volumen = volumen

    def setTv(self,tv):
        self.tv = tv 
    def getTv(self):
        return self.tv