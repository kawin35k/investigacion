from clase_persona import persona

def main():

    lista_personas=[]
    a=persona()
    #a.carga_persona("asd","321")
    quiero=True
    while (quiero==True):
        NyA=input("ingrese nombre y apellido: ")
        cuil=input("ingresa cuil: ")
        #areaExperto=int(input("ingrese area expero: "))
        a.carga_persona(NyA,cuil)
        lista_personas.append(a)
        opcion=int(input("agregar otra persona: \n  1_SI\n  2_NO\n"))
        if (opcion!=1):
            quiero=not quiero
    print(lista_personas[0].mostrar_datos()) #funciona

if __name__=='__main__':
    main()