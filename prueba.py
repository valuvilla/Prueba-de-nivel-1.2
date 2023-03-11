class Nodo:
    def __init__(self):
        self.info = None
        self.sig = None

class Polinomio:
    def __init__(self):
        self.primero = None

class datoPolinomio:
    def __init__(self):
        self.coeficiente = None
        self.exponente = None
    
    def __str__(self):
        return str(self.coeficiente) + "x^" + str(self.exponente)
    
    def __repr__(self):
        return str(self.coeficiente) + "x^" + str(self.exponente)
    
    def __add__(self, otro):
        if self.exponente == otro.exponente:
            return datoPolinomio(self.coeficiente + otro.coeficiente, self.exponente)
        else:
            return None
        
    def __sub__(self, otro):
        if self.exponente == otro.exponente:
            return datoPolinomio(self.coeficiente - otro.coeficiente, self.exponente)
        else:
            return None
        
    def __mul__(self, otro):
        return datoPolinomio(self.coeficiente * otro.coeficiente, self.exponente + otro.exponente)
    

# Example
p1 = Polinomio()
p1.primero = Nodo()
p1.primero.info = datoPolinomio(2, 3)
p1.primero.sig = Nodo()
p1.primero.sig.info = datoPolinomio(3, 2)
p1.primero.sig.sig = Nodo()
p1.primero.sig.sig.info = datoPolinomio(4, 1)
p1.primero.sig.sig.sig = Nodo()
p1.primero.sig.sig.sig.info = datoPolinomio(5, 0)
    

 




    