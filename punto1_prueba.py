from colorama import Fore, Style



Nombre = str (input ("ingrese el nombre del empleado: "))
Nro_hijos= int (input ("ingrese el numero de hijos: "))
Valor_hora = 10000
Horas_trabajadas = int (input("ingrese numero de horas trabajadas por semana: "))
Valor_extra = (Valor_hora * 0.35)+Valor_hora


if Nro_hijos >= 3:
    bonificacion = (Valor_hora)*(Nro_hijos*10)
else:
    bonificacion = Valor_hora (Nro_hijos*5)
    
    
if Horas_trabajadas > 47:
    cantidad_extras = Horas_trabajadas-47
    
else: 
    cantidad_extras = 0
    Valor_extra = 0
    
if Horas_trabajadas >= 1:  
    valor_Hsemana= 47 *Valor_hora   
    devengado = ((Horas_trabajadas-cantidad_extras)*Valor_hora)+(cantidad_extras*Valor_extra)
    neto= (devengado)+(bonificacion)
    print ("Nombre:" , Nombre, "\nNúmero de hijos:", Nro_hijos, "\nBonificación por hijos:", bonificacion, 
           "\nValor hora:", Valor_hora, "\nHoras trabajadas:", Horas_trabajadas,
           "\nValor horas semana:", valor_Hsemana, 
           "\nHoras extras:", cantidad_extras, "\nValor de las extras:", Valor_extra,
           "\nDevengado:", devengado, "\nNeto a pagar:", neto)
   
    print(f"{Fore.RED}Será posible sacar un cinco{Style.RESET_ALL}")
    
else: 
    print ("trabaje vago")     

