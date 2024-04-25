import numpy as np

class persona:
    #__habilidad=int
    __generaNºregistro=1000
    __NroRegistro=str
    __cuil=str
    __Nyp=str
   # __areaExperto=int
    __area=5
    __planilla=None
    __ocupado=False

    def __init__(self):
        self.__planilla=np.empty(self.__area,dtype=int)
        self.__NroRegistro=str(self.__generaNoregistro)
        @classmethod
        def incrementaNªreg(cls):
            self.__generaNoregistro+=1
    def carga_persona(self,xNyP,xcuil):
        self.__Nyp=xNyP
        self.__cuil=xcuil
      #  self.__areaExperto=xareaExp

    def ingresa_habilidad(self,xarea,xnivel):
        self.__planilla[xarea]=xnivel

  #  def dame_especialidad(self):
   #     return self.__areaExperto
    
    def dame_habilidades(self):
        return self.__planilla 
    def dame_area(self,xarea):
        return self.__planilla[xarea]
    def mostrar_datos(self):
        dic={"Nº registro":self.__NroRegistro,
            "Nombre":self.__Nyp,
             "cuil":self.__cuil,
             "area experto":"vacio",
             "ocupado":self.__ocupado}
        return dic
    def actualizar_ocupado(self,estado):
        self.__ocupado=estado
    def dame_ocupado(self):
        return self.__ocupado

