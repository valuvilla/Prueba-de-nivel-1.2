from colorama import Fore, Back, Style
from termcolor import colored

class Nodo (object):
    """clase nodo simplemente enlazado."""
    info, sig = None, None


class datoPolinomio(object):
    """Clase dato Polinomio."""

    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y termino."""
        self.valor = valor #coeficiente
        self.termino = termino #exponente

class Polinomio(object):
    """Clase polinomio"""

    def __init__(self):
        """Crea un polinomio del grado cero"""
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino y su valor al polinomio"""
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while (actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(polinomio, termino, valor):
        """Modifica un termino del polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    def eliminar_termino(polinomio, termino):
        """Elimina un termino del polinomio"""
        if (polinomio.termino_mayor is not None):
            if (polinomio.termino_mayor.info.termino == termino):
                polinomio.termino_mayor = polinomio.termino_mayor.sig
            else:
                aux = polinomio.termino_mayor
                while (aux.sig is not None and aux.sig.info.termino != termino):
                    aux = aux.sig
                if (aux.sig is not None and aux.sig.info.termino == termino):
                    aux.sig = aux.sig.sig

    def obtener_valor(polinomio, termino):
        """Devuelve el valor de un termino del polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
        

    def mostrar(polinomio):
        """Muestra el polinomio"""
        aux = polinomio.termino_mayor
        pol=""
        while (aux is not None):
            signo= "+" if aux.info.valor > 0 else ""
            pol = pol + signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
            aux = aux.sig
        print(pol)

    def existe_termino(polinomio, termino):
        """Determina si existe un termino en el polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return True
        else:
            return False

    
    def sumar(polinomio1, polinomio2):
        """Suma dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2 
        for i in range(0, mayor.grado+1):
            total = Polinomio.obtener_valor(polinomio1, i) + Polinomio.obtener_valor (polinomio2, i)
            if(total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux
    

    def restar(polinomio1, polinomio2):
        """Resta dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2 
        for i in range(0, mayor.grado+1):
            total = Polinomio.obtener_valor(polinomio1, i) - Polinomio.obtener_valor (polinomio2, i)
            if(total != 0):
                Polinomio.agregar_termino(paux, i, total)
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
                if(Polinomio.obtener_valor (paux, termino) != 0):
                    valor += Polinomio.obtener_valor (paux, termino)
                    Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino (paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def dividir(polinomio1, polinomio2):
        """"Divide dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        if(polinomio1.grado >= polinomio2.grado):
            pol1 = polinomio1.termino_mayor
            while(pol1 is not None):
                termino = pol1.info.termino - polinomio2.termino_mayor.info.termino
                valor = pol1.info.valor / polinomio2.termino_mayor.info.valor
                Polinomio.agregar_termino(paux, termino, valor)
                pol1 = pol1.sig
        else:
            print("No se puede dividir")
        return paux
    

if __name__ == "__main__":
    # Experimentacion
    polinomio1 = Polinomio()
    polinomio2 = Polinomio()
    polinomio1.agregar_termino(1, 2) # 2x^1
    polinomio1.agregar_termino(2, 3) # 3x^2

    print(colored(("Polinomio 1"), "red"))
    polinomio1.mostrar()

    print(colored(("Obtener valor del Polinomio 1").center(20), "red"))
    print(polinomio1.obtener_valor(2))

    print(colored(("Modificamos por término el valor del polinimio 1 ").center(20), "red"))
    polinomio1.modificar_termino(2, 5)
    polinomio1.mostrar()

    print(colored("Existe el término 2 en el polinomio 1?".center(20), "red"))
    print(polinomio1.existe_termino(2))

    print(colored(("Eliminamos por término el valor del polinimio 1 ").center(20), "red"))
    polinomio1.eliminar_termino(2)
    polinomio1.mostrar()


    polinomio2.agregar_termino(5,3) # 3x^5
    polinomio2.agregar_termino(3,1) # 1x^3

    print(colored(("Polinomio 2"), "blue"))
    polinomio2.mostrar()


    print(colored("Sumamos Polinomio 1 y Polinomio 2".center(20), "green"))
    polinomio3 = Polinomio.sumar(polinomio1, polinomio2)
    polinomio3.mostrar()

    print(colored("Restamos Polinomio 1 y Polinomio 2".center(20), "green"))
    polinomio4 = Polinomio.restar(polinomio1, polinomio2)
    polinomio4.mostrar()

    print(colored("Multiplicamos Polinomio 1 y Polinomio 2".center(20), "green"))
    polinomio5 = Polinomio.multiplicar(polinomio1, polinomio2)
    polinomio5.mostrar()


    polinomio7=Polinomio()
    polinomio7.agregar_termino(1, 2) # 2x^1
    print(colored("Polinomio 7", "yellow"))
    (polinomio7.mostrar())


    print(colored("Dividimos Polinomio 5 y Polinomio 7".center(20), "green"))
    polinomio6 = Polinomio.dividir(polinomio5, polinomio7)
    polinomio6.mostrar()
    print(Back.CYAN + ("Fin del programa").center(20) + Back.RESET)

