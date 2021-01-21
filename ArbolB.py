
'''
clases importadas 
'''
from Nodo2 import NodoAVL
class ArbolAVL:
    '''
    clase de arbol AVL
    '''
    root=NodoAVL
    #constructor
    def __init__(self):
        self.root=None
    #metodos----------
    def getRoot(self):
        return self.root
    def search(self, node,value):
        """
        docstring
        """
        if(self.root is None):
            return None
        elif(node.dato==value):
            return node
        elif(node.dato<value):
            self.search(node.hder,value)
        else:
            self.search(node.hizq,value)
    
    def obtnerFE(self,node):
        if node is None:
            return -1
        else:
            return node.fe
    @staticmethod
    def max(a,b):
        """
        docstring
        """
        if(a>b):
            return a
        else:
            return b
       
    #----rotacion simple izquierda
    def rotationLeftS(self,node):
        aux1=node.hizq
        node.hizq=aux1.hder
        aux1.hder=node
        node.fe=max(self.obtnerFE(node.hizq),self.obtnerFE(node.hder))+1
        aux1.fe=max(self.obtnerFE(aux1.hizq),self.obtnerFE(aux1.hder))+1

        return aux1
    def rotationRightS(self,node):
        aux1=node.hder
        node.hder=aux1.hizq
        aux1.hizq=node
        node.fe=max(self.obtnerFE(node.hizq),self.obtnerFE(node.hder))+1
        aux1.fe=max(self.obtnerFE(aux1.hizq),self.obtnerFE(aux1.hder))+1

        return aux1
    
    def rotationLeftD(self,node):
        #aux=NodoAVL
        node.hizq=self.rotationRightS(node.hizq)
        aux=self.rotationLeftS(node)
        return aux

    def rotatioRightD(self,node):
        node.hder=self.rotationLeftS(node.hder)
        aux=self.rotationRightS(node)
        return aux
    
    #insertar
    def Insert(self,node,subnode):
        npadre=subnode
        if(node.dato<subnode.dato):
            if(subnode.hizq==None):
                subnode.hizq=node
            else:
                subnode.hizq=self.Insert(node,subnode.hizq)
                if((self.obtnerFE(subnode.hizq)-self.obtnerFE(subnode.hder))==2):
                    if(node.dato<subnode.hizq.dato):
                        npadre=self.rotationLeftS(subnode)
                    else:
                        npadre=self.rotationLeftD(subnode)

        elif(node.dato>subnode.dato):
            if(subnode.hder==None):
                subnode.hder=node
            else:
                subnode.hder=self.Insert(node,subnode.hder)
                if((self.obtnerFE(subnode.hder)-self.obtnerFE(subnode.hizq))==2):
                    if(node.dato>subnode.hder.dato):
                       npadre=self.rotationRightS(subnode)
                    else:
                        npadre=self.rotatioRightD(subnode)
        else:
            print("dato duplicado")
        if((subnode.hizq==None) and (subnode.hder!=None)):
            subnode.fe=subnode.hder.fe+1
        elif((subnode.hder == None) and (subnode.hizq!=None)):
            subnode.fe=subnode.hizq.fe+1
        else:
            subnode.fe=max(self.obtnerFE(subnode.hizq),self.obtnerFE(subnode.hder))+1
        return npadre
        
    def insertN(self,value):
        nodo=NodoAVL(value)
        if(self.root is None):
            self.root=nodo
        else:
            self.root=self.Insert(nodo,self.root)
  

    def preOrden(self,node):
        if(node is not None):
            print(node.dato)
            self.preOrden(node.hizq)
            self.preOrden(node.hder)


    


