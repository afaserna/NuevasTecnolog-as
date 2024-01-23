

Nombre_estudiante = str (input ("ingrese el nombre del estudiante: "))
valor_matricula= float (input("ingrese el valor de la matricula: "))
estrato = int (input("ingrese el estrato: "))
recargo = 0
descuento = 0

if estrato ==1 :
    descuento = (valor_matricula*0.4)
elif estrato==2 :   
    descuento = (valor_matricula*0.3)
elif estrato==3 :   
    descuento = (valor_matricula*0.1)
elif estrato==4 :  
    recargo = (valor_matricula*0.1)
elif estrato==5 :  
    recargo = (valor_matricula*0.2) 
elif estrato==6 :  
    recargo = (valor_matricula*0.4)           
else:
    print("Opción no válida.")
    
if estrato <=3:
    neto = valor_matricula-descuento 
elif estrato == 4:
    neto= recargo+valor_matricula
elif estrato == 5:
    neto= recargo+valor_matricula   
elif estrato == 6:
    neto= recargo+valor_matricula
else:
    print("Opción no válida.")           
               
if  estrato >=1 and estrato <=6:
     
    print ("Nombre:" , Nombre_estudiante, "\nvalor matricula:", valor_matricula) 
    print ("\nestrato:", estrato, 
           "\ndescuento:", descuento, "\nrecargo:", recargo, "\nneto a pagar:", neto)    
