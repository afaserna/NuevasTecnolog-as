
Nombre = str (input ("ingrese el nombre del empleado: "))
Salario= int (input ("ingrese el salario: "))

numeroH_Extras = int (input("ingrese las horas extras: "))
valor_hora= (Salario / 30)
Valor_extra = (valor_hora * 0.35)+ valor_hora
total_Extras = Valor_extra * numeroH_Extras

if (numeroH_Extras==0):
    Valor_extra =0

h_trabajadas = int (input ("ingrese el total de horas trabajadas: "))

neto_pagar = ((h_trabajadas*valor_hora)+Valor_extra)

print ("nombre", Nombre, "\nsalario:", Salario, "\nnumero extras:", numeroH_Extras, 
           "\nValor hora:", valor_hora, "\nvalor hora extra:", Valor_extra,
           "\nTotal extras:", total_Extras, 
           "\nhoras trabajadas:", h_trabajadas, "\nneto a pagar:", neto_pagar)
   

