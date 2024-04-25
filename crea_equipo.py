from clase_persona import persona
import numpy as np

class CreaEquipo:
    __listaPersonas=None
    __lider=int

    def __init__(self,xcantidad):
        self.__listaPersonas=np.empty(xcantidad,dtype=persona)
        self.__lider
    def crea_manual(self):
        pass

    def crea_automatico(self,xpostulantes,xarea):#se pasa por parametro una lista de personas
        if(len(xpostulantes)<len(self.__listaPersonas)):
            print("LA LISTA NO TIENE LA CANTIDAD DE INTEGRANTES MINIMA...")
        else:
            equipo_habilidad=np.array()
            indice_lider=None
            contador=0
            j=0
            for i in xpostulantes:
                equipo_habilidad=np.concatenate([i.dame_area(xarea)])
            indice_lider=np.where(equipo_habilidad.max())#busca el mayor valor y el indice al que pertenece
            self.__lider=indice_lider[0][0]
            xpostulantes[indice_lider].actualizar_ocupado(True)
            self.__listaPersonas[0]=xpostulantes[indice_lider]
            while((contador<len(self.__listaPersonas))and j<len(xpostulantes)):
                if ((xpostulantes[j].dame_ocupado()==False)and(xpostulantes[j].dame_area(xarea)<=equipo_habilidad.max()/1.5)and(xpostulantes[j].dame_area(xarea)>equipo_habilidad.max()/4)):
                    self.__listaPersonas[contador]=xpostulantes[j]
                    xpostulantes[j].actualizar_ocupado(True)
                    contador+=1
                j+=1
            #SELECCIONAR LIDER, quiza use la funcion .dame_especialidad


