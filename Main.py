from Nodo2 import NodoAVL
from ArbolB import ArbolAVL

def main():
    '''
    main donde se crea la instansiacion del objeto
    '''
    a=ArbolAVL()
    a.insertN(3)
    a.insertN(2)
    a.insertN(4)
    a.insertN(5)
    a.insertN(6)
 
    a.preOrden(a.getRoot())

	

if __name__== "__main__":
	main()