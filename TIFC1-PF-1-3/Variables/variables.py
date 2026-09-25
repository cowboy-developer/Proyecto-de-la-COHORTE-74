"""Operadores aritméticos
•	'+' suma.
•	'-' resta.
•	'*' multiplicación.
•	'/' división.
•	'%' residuo.
•	'//' Floor (piso) de una división, es lo mismo que int(un_float). El ceil de a/b es (a+b-1)/b
•	'**' potenciación. La unica que tiene asociatividad de derecha a izquierda
"""
#Ejemplos
a, b = 7, 3
print("a={1}, b={0}".format(b, a))
print("a+b={}".format(a+b))
print("a-b={}".format(a-b))
print("a*b={0}".format(a*b))
print("a/b={0}".format(a/b))#La operacion de división siempre da como resultado un número flotante
print("a%b={}\n".format(a%b))#El residuo de una división

print("Floor de a/b={}".format( int(a/b) ))#castea a int() la división o
print("también funciona a//b={}".format(a//b))# doble / brinda la parte entera de la división
print("Ceil de a/b={}".format( (a+b-1)/b ))#(a+b-1)/b da como resultado el ceil de una división. 
print("a^b={} potenciacion".format(a**b) )

#Operadores de comparación
"""Estos operadores retornan un valor booleano (True o False) si se cumple la condición o no.
•	'<' menor que
•	'>' mayor que
•	'<=' menor o igual que 
•	'>=' mayor o igual que
•	'==' serán iguales?
•	'!=' diferente de
"""

#Ejemplos
x, y = 8, 4
print("{0}<{1}={2}".format(x, y, x<y ))#False
print("{0}>{1}={2}".format(x, y, x>y ))#True
print("{}<={}={}".format(x, y, x<=y ))#False
print("{}>={}={}".format(x, y, x>=y ))#True
print("{}=={}={}".format(x, y, x==y ))#False
print("{}!={}={}".format(x, y, x!=y ))#True


#Operadores lógicos
"""Aquí se utiliza la palabra, en la versión de C++ que yo uso solo funciona con los símbolos.
•	'and' && verifica si más de una condición se cumple
•	'or' || verifica si una o más condiciones se cumplen
•	'not' ! revierte el resultado !True=False, !False=True

Ejemplos:
•	and: Todas las condiciones que estén usando a este operador deberán cumplirse estrictamente para retornar True.
(2<3) and (2>1) and (0==0) #True
(1!=0) and (4<1) #False

•	or: Solo basta con que una condición se cumpla para que retorne True.
('a' == 'a') or (9<0) #True
('a' != 'a') or (9<0) or (-1==1) #False
•	not: Retorna lo contrario. !yes = not; ¡not = yes.
              not False, not True, not('x' != 'y') #(True, False, False)  

"""