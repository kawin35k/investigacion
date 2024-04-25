import numpy as np
from clase_persona import persona
from crea_equipo import Equipo

equipo1=Equipo(3)

per1=persona()
per1.carga_persona("A","1")
#print(per.mostrar_datos())
per1.ingresa_habilidad(2,4)
#print(per1.dame_habilidades().max()) FUNCIONA
per2=persona()
per2.carga_persona("B","2")
per2.ingresa_habilidad(2,3)
per3=persona()
per3.carga_persona("C","3")
#print(per.mostrar_datos())
per3.ingresa_habilidad(2,5)
per4=persona()
per4.carga_persona("D","4")
per4.ingresa_habilidad(2,8)
per5=persona()
per5.carga_persona("E","5")
per5.ingresa_habilidad(2,10)

listaDePersonas=[per1,per2,per3,per4,per5]
a=[]
#for i in listaDePersonas:   #este for es el de la linea 23 del comulo crea_equipo
 #   a.append(i.dame_area(2))#concatena(agrega) elementos al arreglo
#print(a)
equipo1.crea_automatico(listaDePersonas,2)
print(equipo1.dame_equipo())

#a=2
#perslita=[per1,per2]
#lista=[1,5000,4,3,2,7,8,9,9,5]
#arr=np.array(lista)
#brr=np.empty(a,dtype=int)
#b=np.array(perslita)
#b=np.concatenate((arr,[100]),axis=0)   de esta forma se puede concatenar arreglos
#print(b)
#print(listaArea.max())