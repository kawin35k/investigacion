import numpy as np

class persona:
    #__habilidad=int
    __generaNºregistro=1000
    __Nºregistro=str
    __cuil=str
    __Nyp=str
    __areaExperto=int
    __area=5
    __planilla=np

    def __init__(self):
        self.__planilla.empty(self.__area,dtype=int)
        self.__Noregistro=str(self.__generaNoregistro)
        @classmethod
        def incrementaNªreg(cls):
            self.__generaNoregistro+=1
    def carga_persona(self,xNyP,xcuil,xareaExp):
        self.__Nyp=xNyP
        self.__cuil
        self.__areaExperto=xareaExp

    def ingresa_habilidad(self,xarea,xnivel):
        self.__planilla[xarea]=xnivel

    def mostrar_datos(self):
        dic={"Nombre":self.__Nyp,
             "cuil":self.__cuil,
             "area experto":self.__areaExperto}
        return dic
    
