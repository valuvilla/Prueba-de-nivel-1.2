class Nodo (object):
    """clase nodo simplemente enlazado."""
    info, sig = None, None

aux = Nodo( )
aux.info = "Primer nodo"
palabra = input('Ingrese una palabra: ')	
naux = aux
while (palabra == ""):
    nodo = Nodo( )
    nodo.info = palabra
    naux.sig = nodo
    naux = nodo
    palabra - input('Ingrese una palabra: ')

while (aux is not None):
    print(aux.info)
    aux = aux.sig

class datoPolinomio(object):
    """Clase dato operaciones."""

    def _init_(self, valor, termino):
        """Crea un dato polinomio con valor y termino."""
        self.valor = valor
        self.termino = termino



class Polinomio(object):
    """Clase operaciones."""

    def _init_(self):
        """Crea un polinomio del grado cero."""
        self.termino_mayor = None
        self.grado = -1

    def _str_(self):
        """Muestra el polinomio."""
        aux = self.termino_mayor
        pol = ''
        if (aux is not None):
            while(aux is not None):
                signo = '' 
                if(aux. info.valor > 0):
                    signo += '+'
                pol += signo + str(aux.info.valor)+"x^"+str(aux.info.termino)
                aux = aux.sig
        return pol
    
    # Add a polynomial
    def add(self, other):
        """Add two polynomials."""
        paux = Polinomio()
        mayor = self if (self.grado > other.grado) else other 
        for i in range(0, mayor.grado+1):
            total = self.obtener_valor(i) + other.obtener_valor(i)
            if(total != 0):
                paux.agregar_termino(i, total)
        return paux
    
    # Subtract a polynomial
    def sub(self, other):
        """Subtract two polynomials."""
        paux = Polinomio()
        mayor = self if (self.grado > other.grado) else other 
        for i in range(0, mayor.grado+1):
            total = self.obtener_valor(i) - other.obtener_valor(i)
            if(total != 0):
                paux.agregar_termino(i, total)
        return paux
    
    # Multiply a polynomial
    def mul(self, other):
        """Multiply two polynomials."""
        paux = Polinomio()
        for i in range(0, self.grado+1):
            for j in range(0, other.grado+1):
                total = self.obtener_valor(i) * other.obtener_valor(j)
                if(total != 0):
                    paux.agregar_termino(i+j, total)
        return paux
    
    # Divide a polynomial
    def div(self, other):
        """Divide two polynomials."""
        paux = Polinomio()
        for i in range(0, self.grado+1):
            for j in range(0, other.grado+1):
                total = self.obtener_valor(i) / other.obtener_valor(j)
                if(total != 0):
                    paux.agregar_termino(i+j, total)
        return paux
    
    # Get the value of a polynomial
    def obtener_valor(self, termino):
        """Get the value of a polynomial."""
        aux = self.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if(aux is not None):
            return aux.info.valor
        return 0
    


    
class operaciones(object):
    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino y su valor al operaciones. """
        polinomio=Polinomio()
        aux = Nodo( )
        dato = datoPolinomio()
        dato.valor = valor
        dato.termino = termino
        aux.info = dato
        aux.sig = None

        # comparo el termino con el grado del polinomio
        if(termino > polinomio.grado):
            # si es mayor, lo agrego al principio
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino

        else:
            actual=polinomio.termino_mayor
            while(actual.sig is not None and actual.sig.info.termino > termino):
                actual=actual.sig
            aux.sig=actual.sig
            actual.sig=aux
    


    
    def eliminar_termino(polinomio, termino):
        """Elimina un termino del operaciones."""
        aux = operaciones.termino_mayor
        if(aux is not None):
            if(aux.info.termino == termino):
                operaciones.termino_mayor = aux.sig
                del aux
            else:
                while(aux.sig is not None and aux.sig.info.termino != termino):
                    aux = aux.sig
                if(aux.sig is not None):
                    aux.sig = aux.sig.sig
                    del aux.sig

    def determinar_si_existee_termino(polinomio, termino):
        """Determina si existe un termino en el operaciones."""
        # consultar si el resultado es distinto de cero para determinar si el polinomio tiene ese término o no
        aux = operaciones.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if(aux is not None):
            return True
        return False
        

    def modificar_termino(polinomio, termino, valor):
        """Modifica el valor de un termino del operaciones."""
        aux = operaciones.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    def obtener_valor (polinomio, termino):
        """Devuelve el valor de un termino del operaciones."""
        aux = operaciones.termino_mayor
        while(aux is not None and aux. info.termino > termino):
            aux = aux.sig
        if(aux is not None and aux.info.termino == termino): 
            return aux.info.valor 
        else:
            return 0

    def mostrar (polinomio):
        """Muestra el operaciones."""
        aux = operaciones.termino_mayor
        pol = ''
        if (aux is not None):
            while(aux is not None):
                signo = '' 
                if(aux. info.valor > 0):
                    signo += '+'
                pol += signo + str(aux.info.valor)+"x^"+str(aux.info.termino)
                aux = aux.sig
        return pol

    def sumar(polinomio1, polinomio2):
        """Suma dos polinomios y devuelve el resultado."""
        paux = Polinomio()
    
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2 
        for i in range(0, mayor.grado+1):
            total = operaciones.obtener_valor(polinomio1, 1) + operaciones.obtener_valor (polinomio2, 1)
            if(total != 0):
                operaciones.agregar_termino(paux, i, total)
        return paux
    
    def restar(polinomio1, polinomio2):
        """Resta dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2 
        for i in range(0, mayor.grado+1):
            total = operaciones.obtener_valor(polinomio1, 1) - operaciones.obtener_valor (polinomio2, 1)
            if(total != 0):
                operaciones.agregar_termino(paux, i, total)
        return paux


    def multiplicar(polinomio1, polinomio2):
        """Multiplica dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino + pol2.info. termino
                valor = pol1.info.valor * pol2.info. valor
                if(operaciones.obtener_valor (paux, termino) != 0):
                    valor += operaciones.obtener_valor (paux, termino)
                    operaciones.modificar_termino(paux, termino, valor)
                else:
                    operaciones.agregar_termino (paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def dividir(polinomio1, polinomio2):
        """"Divide dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino - pol2.info. termino
                valor = pol1.info.valor / pol2.info. valor
                if(operaciones.obtener_valor (paux, termino) != 0):
                    valor += operaciones.obtener_valor (paux, termino)
                    operaciones.modificar_termino(paux, termino, valor)
                else:
                    operaciones.agregar_termino (paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux