from clase_persona import persona
import numpy as np

class Equipo:
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
            equipo_habilidad=None
            habilidades_postulantes=[]
            indice_lider=None
            contador=1#empieza en uno por que el indice 0 ya esta ocupado por el lider
            j=0
            for i in xpostulantes:
                habilidades_postulantes.append(i.dame_area(xarea))#guarda las habilidades
            #for i in listaDePersonas:
            #   a.append(i.dame_area(2))
            equipo_habilidad=np.array(habilidades_postulantes)#casteo o refundicion
            indice_lider=np.where(equipo_habilidad.max())#busca el mayor valor y el indice al que pertenece
            self.__lider=indice_lider[0][0]#para que en caso de haber mas de un indice solo se quede con el primero
            xpostulantes[self.__lider].actualizar_ocupado(True)
            self.__listaPersonas[0]=xpostulantes[self.__lider]
            #el lider del equipo es el primer elemento del arreglo
            while((contador<len(self.__listaPersonas))and j<len(xpostulantes)):#itera hasta que completa el equipo(litsaPersonas) o terminar con los postulantes
                if ((xpostulantes[j].dame_ocupado()==False)and(xpostulantes[j].dame_area(xarea)<=equipo_habilidad.max()/1.5)and(xpostulantes[j].dame_area(xarea)>equipo_habilidad.max()/4)):
                #este if pone como condiciones que la persona este libre y que cumpla con un rango de hanilidad, debe ser menor que el lider para asi aprender de el
                    self.__listaPersonas[contador]=xpostulantes[j]
                    xpostulantes[j].actualizar_ocupado(True)
                    contador+=1
                j+=1
            #SELECCIONAR LIDER, quiza use la funcion .dame_especialidad
    def dame_equipo(self):
        return self.__listaPersonas

